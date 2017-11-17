"""Download Library Locations for a given OCLC ID Number."""

# =============================================================================
# Import libraries
# =============================================================================

import logging  # For outputting information to the user.
import pandas
import requests  # For making HTML requests
import networkx  # For network mapping
import matplotlib.pyplot as plt  # For drawing plots

# =============================================================================
# Load configuration settings from a file called config.py
# =============================================================================

import config
# We can now get access to our oclc_wskey varible from that file with
# config.oclc_wskey

# =============================================================================
# Other settings
# =============================================================================

oclc_institution_codes = {
    "RBN": "Brown University Library",
    "ZCU": "Columbia University Libraries",
    "COO": "Cornell University Library",
    "DRB": "Dartmouth College Library",
    "NDD": "Duke University Libraries",
    "HLS": "Harvard University Libraries",
    "JHE": "Johns Hopkins University Libraries",
    "MYG": "Massachusetts Institute of Technology Libraries",
    "PUL": "Princeton University Library",
    "STF": "Stanford University",
    "YUS": "Yale University Library",
    "CGU": "University of Chicago Library"
}

# =============================================================================
# Define API query URL
# =============================================================================

# The API we'll be using is the WorldCat Search Library Catalog URLs API
# https://www.oclc.org/developer/develop/web-services/worldcat-search-api/library-catalog-url.en.html

parameters_for_api = {
        "frbrGrouping": "off",
        "format": "json",
        "maximumLibraries": "100",
        "wskey": config.oclc_wskey}

comma_separated_oclc_institutions = ','.join(
        oclc_institution_codes.keys())


class ErrorWithAPI(Exception):
    pass


def create_api_request(
        item_identifier,
        comma_separated_institution_codes=comma_separated_oclc_institutions,
        api_request_parameters=parameters_for_api):
    """Given an item ID and some OCLC institution symbols, query the OCLC
    WorldCat Search Library Catalog URLs API"""

    print(f'Running API query for item ID "{item_identifier}"...')

    # This should NOT have a trailing slash ('/') at the end:
    api_base_url = ('http://www.worldcat.org/webservices/catalog/content/'
                    'libraries/isbn/')

    # Update the static api parameters to include the (dynamic) DOI:
    api_request_parameters = api_request_parameters.copy()
    api_request_parameters['oclcsymbol'] = comma_separated_institution_codes

    # Add the item identifier to the URL, so that it looks like this:
    api_url = f'{api_base_url}/{item_identifier}'

    api_response = requests.get(
            api_url,
            params=api_request_parameters)

    # We'll check the status code below: Possible codes are:
    # 200: Successful request
    # 400: Bad/malformed request
    # 500: Server error
    if api_response.status_code != 200:
        raise ErrorWithAPI(
                f'Problem contacting API: We received Status Code '
                '{api_response.status_code}. The full response text is '
                'below: {api_response.text}')

    logging.info(f'Returning query results from URL "{api_response.url}"')

    return api_response


# =============================================================================
# Run the queries for some item IDs
# =============================================================================

# Create some empty dataframes, which we'll fill in below.
library_holdings = pandas.DataFrame()
api_responses = pandas.DataFrame()

item_ids = [
        '0439708184',  # Harry Potter and the Sorcerer's Stone
        '0439064872',  # Harry Potter And The Chamber Of Secrets
        '0439136369',  # Harry Potter and the Prisoner of Azkaban
        '0393089053',  # The Odyssey (brand new edition)
        '0393089088'  # The Red Book
        ]
# api_response_parsed = create_api_request('0393089053').json()

for item_id in item_ids:
    api_response = create_api_request(item_id)
    # api_response.text  # Look at the api response json

    # Parse the JSON from the API, turning it into a dictionary:
    api_response_parsed = api_response.json()

    # api_response_parsed.keys()  # Take a look at the keys in the api response
    if 'totalLibCount' in api_response_parsed:
        api_response_parsed['totalLibCount']  # See the total library count

    api_responses = api_responses.append({
            'item_id': item_id,
            'json_response': api_response.text},
            ignore_index=True)

    # Find out which libraries have the item, and save them to a dataframe:
    message_in_case_there_are_no_libraries = (
            'The response from the API indicates that there are no libraries '
            'that hold this item. Skipping it and moving on to the next '
            'item...')

    if 'library' in api_response_parsed:
        for library in api_response_parsed['library']:
            # If we didn't get an error message in the json itself:
            if('diagnostic' in api_response_parsed['library'][0] and
               api_response_parsed['library'][0]['diagnostic']['message'] ==
               'Holding not found'):
                print(message_in_case_there_are_no_libraries)
            else:
                oclc_symbol_of_library = library["oclcSymbol"]
                print(f'Adding {oclc_symbol_of_library} to the dataframe...')

                library_holdings = library_holdings.append({
                        'item_id': item_id,
                        'institution_id': oclc_symbol_of_library},
                        ignore_index=True)
    else:
        print(message_in_case_there_are_no_libraries)

# =============================================================================
# Save to a CSV
# =============================================================================

library_holdings.to_csv(
        config.csv_output_to_save,  # Where to save the file
        index=False  # Don't include row numbers in the CSV
        )

api_responses.to_csv(
        # Where to save the file:
        f'{config.csv_output_to_save}_API_responses.csv',
        index=False  # Don't include row numbers in the CSV
        )

# =============================================================================
# Explore the data
# =============================================================================

# See the number of libraries for each item, by grouping by item ID:
counts_by_item_id = library_holdings.groupby('item_id').count()

# Add 0-count items back into counts_by_item_id:
for item_id in item_ids:
    if item_id not in list(library_holdings['item_id'].unique()):
        counts_by_item_id.loc[item_id] = 0

# Treat library_holdings as an "edge list," and make a network graph out of it:

library_network = networkx.from_pandas_dataframe(
        library_holdings,
        source='institution_id',
        target='item_id')

# library_network.number_of_nodes()
# list(library_network.nodes)
# library_network.number_of_edges()
# list(library_network.edges)

plt.axis('off')  # Turn off X- and Y-axes in the general plot settings

graph_node_positions = networkx.spring_layout(library_network)

networkx.draw_networkx(
        library_network,  # The network
        graph_node_positions,  # Node positions
        node_color='orange',
        node_size=800,
        alpha=0.4  # Transparency of the nodes
        )
