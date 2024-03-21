from dotenv import dotenv_values
from urllib.request import urlopen
import requests
import re

CONFIG = dotenv_values('.env')
BING_API_KEY = CONFIG['BING_API_KEY']
#prep the query url
SEARCH_TERM = 'what is the best gaming gpu'
URL = f'https://api.bing.microsoft.com/v7.0/search'
PARAMS = {'q': SEARCH_TERM, 'textDecorations': True, 'textFormat': 'HTML'}
HEADERS =  { 'Ocp-Apim-Subscription-Key': BING_API_KEY }


response = requests.get(url=URL, params=PARAMS, headers=HEADERS) #fetch
print(response.status_code)
search_results = response.json()

def iterate_over_results(results: list[dict[str]]) -> list[dict[str]]:
    return list(map(lambda url: 
               {
                   'id': url['id'],
                   'name': url['name'],
                   'url': url['url'],
                   'body': None,
                   'metadata':  {
                                    'datePublished': url['datePublishedDisplayText'] if 'datePublishedDisplayText' in url.keys() else None, 
                                    'dateLastCrawled': url['dateLastCrawled']
                                }
                }, results))

resources = iterate_over_results(search_results['webPages']['value'])
single_url = urlopen(resources[0]['url'])
page = single_url.read()#read the html object and get all html of the page
print(page)