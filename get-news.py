import requests
import sys
import numpy as np

def download_news(token):
    sources = requests.get(
        f'https://newsapi.org/v2/sources?apiKey={token}&language=en'
    ).json()
    sources_id_list = [source['id'] for source in sources['sources']]
    sources_joined = ','.join(sources_id_list)
    # you can't get more than 100 headlines on free subscription anyway
    headlines = requests.get(
        f'https://newsapi.org/v2/top-headlines?apiKey={token}&sources={sources_joined}&perPage=100'
    )

    sources_with_headlines = {id:[] for id in sources_id_list}
    for headline in headlines.json()['articles']:
        source_id = headline['source']['id']
        sources_with_headlines[source_id].append(headline['title'])
    sources_with_headlines_flat = []
    for id, headlines in sources_with_headlines.items():
        row = [id]
        row.extend(headlines)
        sources_with_headlines_flat.append(row)

    pad = len(max(sources_with_headlines_flat, key=len))
    data_with_nan = []
    for i in sources_with_headlines_flat:
        data_with_nan.append(i + [None]*(pad-len(i)))
    data_with_nan = np.array(data_with_nan)
    print(data_with_nan.transpose())

if __name__ == "__main__":
    download_news(
        token=sys.argv[1]
    )