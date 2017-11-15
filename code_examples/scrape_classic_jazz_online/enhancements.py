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

mp3_links_from_website = {}  # Create a blank list. We'll add to this as we go.

for link in links_from_website:
    link_url = link['href']
    link_text = link.text

    if link_url.endswith('.mp3'):
        mp3_links_from_website[link_url] = link_text

for url, title in mp3_links_from_website.items():
    print(f'Looking at "{title}" (which is from the URL "{url}")...')
