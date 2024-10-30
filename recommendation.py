import requests
import re
from urllib.parse import urlparse
import pandas as pd
import os
from bs4 import BeautifulSoup

def google_search(query, api_key, cse_id, **kwargs):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': query,
        'key': api_key,
        'cx': cse_id
    }
    params.update(kwargs)
    response = requests.get(url, params=params)
    return response.json()

# Your API key and Programmable Search Engine ID
api_key = os.environ.get('GOOGLE_CUSTOM_SEARCH_KEY')
cse_id = os.environ.get('CUSTOM_SEARCH_ENGINE')

def get_page_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        paragraphs = soup.find_all('p')
        content = ' '.join([p.get_text() for p in paragraphs])
        return content
    else:
        return None
    
search_query = 'Top trending tourist spots in Pakistan'

# Example search
results = google_search(search_query, api_key, cse_id, num=4)

content = ''

# Process and print the results
for item in results.get('items', []):
    title = item.get('title', 'No title')
    snippet = item.get('snippet', 'No snippet')
    link = item.get('link', 'No link')
    
    try:
        content += get_page_content(link)
        # print(content)
    except:
        print("Failed to extract content")

spots = pd.read_csv('recommended_spots_updated.csv')

for word in content.split(' '):
    # Do something with each word
    for place in spots['place']:
        if word.lower() == place.lower():
            spots.loc[spots['place'] == place, ' score'] += 1
            print(word)

spots = spots.sort_values(' score', ascending=False).head(10)

#upload the data to the csv file
spots.to_csv('top_rated_sorted.csv', index=False)