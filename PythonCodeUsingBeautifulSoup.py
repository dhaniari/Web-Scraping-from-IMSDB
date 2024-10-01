import requests
from bs4 import BeautifulSoup

# Base URL of IMSDb
url = 'https://www.imsdb.com/'

# Get the list of movie scripts
response = requests.get(url + 'scripts/')
soup = BeautifulSoup(response.content, 'html.parser')

# Extract links to individual movie script pages
script_links = []
for link in soup.find_all('a', href=True):
    if '/Movie Scripts/' in link['href']:
        script_links.append(url + link['href'])

# Visit each script page and extract the script text
for link in script_links[:10]:  # Limiting to 10 scripts for example
    script_response = requests.get(link)
    script_soup = BeautifulSoup(script_response.content, 'html.parser')
    
    # Extract the script content (this varies depending on site structure)
    script_content = script_soup.find('pre').get_text()
    
    # Save the script to a local file
    title = link.split('/')[-1].replace('.html', '').replace('-', ' ')
    with open(f'{title}.txt', 'w') as f:
        f.write(script_content)

    print(f"Saved script: {title}")
