import requests
import sys

def download_news(token):
    sources = requests.get(
        f'https://newsapi.org/v2/sources?apiKey={token}&language=en'
    ).json()
    sources_id_list = [source['id'] for source in sources['sources']]
    sources_joined = ','.join(sources_id_list)
    # you can't get more than 100 headlines on free subscription anyway
    # so I left default value of headlines per page
    headlines = requests.get(
        f'https://newsapi.org/v2/top-headlines?apiKey={token}&sources={sources_joined}'
    )

if __name__ == "__main__":
    download_news(
        token=sys.argv[1]
    )