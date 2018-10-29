# account: jho.yvr+newsapi@gmail.com
api_key = '94728df306c14086ad303cc26ddf3eab'
import requests, json

base_url = 'https://newsapi.org/v2/'
params_ini = {
    'apiKey': api_key
}

def getheadline( country = 'hk', category = None, sources = None, q = None, pageSize = 20):
    url = base_url + 'top-headlines?'
    params = params_ini
    params['country'] = country
    params['pageSize'] = pageSize
    
    data = requests.get(url, params = params)
    if data.status_code == 200:
        return json.loads(data.text)
    else:
        return None

def printHeadlines(country = 'hk', category = None, sources = None, q = None, pageSize = 20):
    data = getheadline(country = country, category = None, sources = None, q = None, pageSize = pageSize)
    
    if data is None:
        print("Can't load headlines")
    else:
        print("Getting you headlines from NewsAPI.org!!!\n\n")
        for i in data['articles']:
            pdata = [i['source']['name'], i['title'], i['url']]
            print(" | ".join(pdata))
        print("\n\n---End of Headlines---\n")
        
printHeadlines(country= 'us',pageSize=3)