from dotenv import dotenv_values
import requests
from bs4 import BeautifulSoup

CONFIG = dotenv_values('.env')
BING_API_KEY = CONFIG['BING_API_KEY']

#prep the query url
SEARCH_TERM = 'what is the best gaming gpu'
URL = f'https://api.bing.microsoft.com/v7.0/search'
PARAMS = {'q': SEARCH_TERM, 'textDecorations': True, 'textFormat': 'HTML'}
HEADERS =  { 'Ocp-Apim-Subscription-Key': BING_API_KEY }

#helper functions:
def iterate_over_results(results: list[dict[str]]) -> list[dict[str]]: #extracts only the relevant objects with the body being empty for now as it will be updated later on
    return list(map(lambda url: #extract relevant info for each of the url
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


# TO DO: We would still have to deal with embedded stuff like imagine a website that has mathematical formulas
# TO DO: We also have to deal with encoding and decoding the text as it may be out of the ASCII 
# TO DO: Package these into batches within the body, i.e. [batch of 50, batch of 50, batch of 50]


try: 
    response = requests.get(url=URL, params=PARAMS, headers=HEADERS) #fetch
except:
   raise Exception('There was an error fetching from the BING API check over the url string')
else:
    search_results = response.json()

    resources = iterate_over_results(search_results['webPages']['value']) # pass in a batch of fetched url's to our helper func for extraction

    try:
        response_url = requests.get(resources[0]['url']) #fetching the data 
    except:
        raise Exception(f'There was an error fetching from the url')
    else:
        soup = BeautifulSoup(response_url.content, 'html.parser')

        def relevant_doc_links() -> list[dict[str]]:
            return None

        def clean_text(txt: str) -> str:
            return [char.strip for char in txt]
        out = (soup.get_text().split()) # this is probably better since the support vector has the cap of 50 w
        print(out)


        # print(soup.get_text()) #get's only the text of the document, and 


        # print(soup.find_all('p'))
    


    