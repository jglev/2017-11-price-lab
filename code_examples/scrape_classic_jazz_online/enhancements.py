# =============================================================================
# Download from multiple pages:
# =============================================================================

# Create a list of pages:
url_of_page_to_scrape = [
        'http://www.jazz-on-line.com/artists/Ida_Cox.htm',
        'http://www.jazz-on-line.com/artists/Mahalia_Jackson.htm',
        'http://www.jazz-on-line.com/artists/Django_Reinhardt.htm',
        'http://www.jazz-on-line.com/artists/Dave_Brubeck.htm',
        'http://www.jazz-on-line.com/artists/Ella_Fitzgerald.htm']

# Wrap everything in a 'for loop' over url_of_page_to_scrape. Possibly put
# everything into a function, and then run a 'for loop' over *that.*

# =============================================================================
# Save the file using the filename from the website
# =============================================================================

# Amend the for loop for MP3 URLs to have song names:

mp3_links_from_website = {}  # Create a blank dictionary.
# We'll add to this as we go.

# for link in links_from_website:
for link_number in range(0, len(links_from_website)):
    link = links_from_website[link_number]

    link_url = link['href']
    link_text = link.text

    if link_url.endswith('.mp3'):
        mp3_links_from_website.update({
                link_number: {
                        'link_text': link_text,
                        'link_url': link_url}})

for url, title in mp3_links_from_website.items():
    print(f'Looking at "{link_text}" (which is from the URL "{link_url}")...')

# =============================================================================
# Create a pandas dataframe from the above:
# =============================================================================

import pandas

link_dataframe = pandas.DataFrame.from_dict(mp3_links_from_website).transpose()

list(link_dataframe.columns)
list(link_dataframe.link_text)
