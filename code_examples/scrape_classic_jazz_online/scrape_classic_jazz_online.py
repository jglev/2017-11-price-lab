# =============================================================================
# Import libraries
# =============================================================================

from bs4 import BeautifulSoup  # For scraping/parsing HTML
import os  # For interacting with our filesystem
from pathlib import Path  # For interacting with our filesystem
# import re  # For the bonus "regular expressions" approach below.
import requests  # For opening HTML connections
import time  # For pausing between downloads

# =============================================================================
# Settings
# =============================================================================

url_of_page_to_scrape = 'http://www.jazz-on-line.com/artists/Ida_Cox.htm'
# See also, e.g.:
# http://www.jazz-on-line.com/artists/Mahalia_Jackson.htm
# http://www.jazz-on-line.com/artists/Django_Reinhardt.htm
# http://www.jazz-on-line.com/artists/Dave_Brubeck.htm
# http://www.jazz-on-line.com/artists/Ella_Fitzgerald.htm

directory_to_save_music_to = os.path.join('music', 'downloaded_files')

number_of_seconds_to_wait_between_downloads = 1.0

# =============================================================================
# Create the music directory if it doesn't already exist
# =============================================================================

Path(directory_to_save_music_to).mkdir(parents=True, exist_ok=True)

# =============================================================================
# Scrape the webpage
# =============================================================================

# Open a connection to the webpage:
connection_to_webpage = requests.get(url_of_page_to_scrape)

website_html_data = connection_to_webpage.text

website_parsed_data = BeautifulSoup(website_html_data, 'html.parser')

# Get all links of the type we're looking for (any links ('<a>...</a>' that
# end in '.mp3'):
links_from_website = website_parsed_data.find_all('a')

# Let's get just the MP3 links. Here are *two ways* to do this:

# Option 1: A "for loop:"
mp3_links_from_website = []  # Create a blank list. We'll add to this as we go.

for link in links_from_website:
    link_url = link['href']

    if link_url.endswith('.mp3'):
        mp3_links_from_website.append(link_url)

# Option 2: A wildcard search.
# I'm including this as a bonus because we won't have time to cover "regular
# expressions", which are a way to search for patterns of text (see
# regular-expressions.info to learn more about this approach).
# The take home message: what you would normally think of as a wildcard search
# (like '*.mp3') looks like this in regular expressions: '.*\.mp3'
# This approach also uses a 'list comprehension' for-loop:

# mp3_links_from_website = [link['href'] for link in
#                           website_parsed_data.find_all(
#                                   'a', href=re.compile('.*\.mp3'))]

# =============================================================================
# Now that we have the URLs for the files, download them
# =============================================================================


# Define a function that saves a file, given a URL:
def download_and_save_file(
        url_to_download,
        place_to_download_to=directory_to_save_music_to):

    # Get the filename from the URL ('example.mp3' from http://...example.mp3)
    filename_of_file_in_url = os.path.basename(url_to_download)

    # 'Open a connection' to the file we're going to save to:
    with open(
            os.path.join(place_to_download_to, filename_of_file_in_url),
            "wb") as file:
        # Create an HTTP connection to the file:
        http_connection = requests.get(url_to_download)

        # Save the file:
        file.write(http_connection.content)

        # Close the HTTP connection:
        http_connection.close()


# Now let's use our function on each of the MP3s, pausing between each download
# (as a way of 'rate-limiting' our download):
for mp3_link in mp3_links_from_website:
    print(f'Downloading {mp3_link}...')  # Give ourselves a message.
    download_and_save_file(mp3_link)  # Download the file.
    # Pause before moving on in the loop:
    time.sleep(number_of_seconds_to_wait_between_downloads)
