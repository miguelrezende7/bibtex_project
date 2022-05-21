from textwrap import indent
import requests
import json
from requests.exceptions import HTTPError


class GetFromApi():
    def __init__(self):
        pass
        
    def url_ieee(search_words):
        token = 'njjgum9jmk4unbad2jyqdn7r'
        url = f'https://ieeexploreapi.ieee.org/api/v1/search/articles?querytext={search_words}&apikey={token}'
        # url= https://ieeexploreapi.ieee.org/api/v1/search/articles?querytext=BIG+DATA&apikey=njjgum9jmk4unbad2jyqdn7r
        return url

    def get_from_api(url):

        # url = GetFromApi.url_ieee(self, search_words)

        try:
            response = requests.get(url)
            response.raise_for_status()
            jsonResponse = response.json()

        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
            return {}
        except Exception as err:
            print(f'Other error occurred: {err}')
            return {}

        # print(jsonResponse)
        # print('\n\n\n')

        return jsonResponse

    def formated_ieee_dict_from_api(json_file):

        api_dict_list = []
        for article in json_file['articles']:
            author_name = ''
            keywords = ''

            for author in article['authors']['authors']:
                author_name += author['full_name']+','

            author_name = author_name[:-1]
            keywords = ",".join(article['index_terms']['ieee_terms']['terms'])

            api_dict_list.append({'author': author_name, 'title': article.get('title', 'empty'), 'keywords': keywords,
                                  'abstract': article.get('abstract', 'empty'), 'year': article.get('publication_year', 'empty'), 'type_publication': 'article',
                                  'doi': article.get('doi', 'empty'), 'book_journal': article.get('publication_title', 'empty')})

        return api_dict_list
