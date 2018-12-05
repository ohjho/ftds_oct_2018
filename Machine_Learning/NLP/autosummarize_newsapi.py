# Preliminary
import requests, json, re
import nltk, string
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from functools import reduce

# News API
# account: jho.yvr+newsapi@gmail.com
api_key = '94728df306c14086ad303cc26ddf3eab'
base_url = 'https://newsapi.org/v2/'
params_ini = {
    'apiKey': api_key
}

def GetJson(url, params):
    data = requests.get(url, params = params)
    if data.status_code == 200:
        return json.loads(data.text)
    else:
        return None

def getHeadline( optdict = None, verbose = 0):
    url = base_url + 'top-headlines?'
    params = params_ini
    if optdict != None:
        for key in optdict:
            params[key] = optdict[key]

    if verbose:
        print(f'Searching for headline with these params \n {params}')

    return GetJson(url, params)

def getSearch( search_term , optdict = None, verbose = 0):
    url = base_url + 'everything?'
    params = params_ini
    if search_term != '':
        params['q'] = search_term
    if optdict != None:
        for key in optdict:
            params[key]= optdict[key]

    if verbose:
        print(f'Searching for {search_term} with these params \n{params}')

    return GetJson(url, params)

def GetAllHeadlines():
    params_dict = {
        'country': 'ca',
        'pageSize': 100,
        'category': 'business',
        'language': 'en'
    }
    data = getHeadline( params_dict, verbose = 1)

    # params_dict = {
    #     'domains' : 'scmp.com',
    #     'sortBy': 'publishedAt',
    #     'language': 'en',
    #     'pageSize': 100
    # }
    # data = getSearch('', params_dict, verbose =1)

    if data is None:
        print('Error with the API!')
        return None
    else:
        all_headlines = ''
        for arti in data['articles']:
            title = arti['title']
            if title[-1] != '.':
                title = title + '.'
            all_headlines +=  title + ' '
        return all_headlines

def ParseText( inTxt ):
    word_tok = word_tokenize( inTxt )
    sent_tok = sent_tokenize( inTxt )

    my_stopwords = set( stopwords.words('english') + list(string.punctuation) )
    my_words = [ w for w in word_tok if w not in my_stopwords]
    return my_words, sent_tok

def SimpleSummarize( lWords, lSent, withScore = False):
    word_freq = {}
    for w in lWords:
        if w not in word_freq.keys():
            word_freq[w] = 1
        else:
            word_freq[w] += 1

    word_freq_sort = sorted( word_freq.items() , key = lambda kv: kv[1], reverse= True)
    most_freq = word_freq_sort[0][1]
    word_freq_score = { k: v/ most_freq for k,v in word_freq_sort}

    sent_scored = {}
    for sent in lSent:
        iscore = 0
        for w in word_tokenize(sent):
            if w in word_freq_score.keys():
                iscore += word_freq_score[w]
        sent_scored[sent] = iscore

    sent_sorted = sorted( sent_scored.items(), key = lambda kv: kv[1], reverse = True)
    if not withScore:
        sent_sorted = [k for k,v in sent_sorted]

    return sent_sorted

def Main():
    raw = GetAllHeadlines()
    l_words, l_sent = ParseText( raw )
    scored_headlines = SimpleSummarize( l_words, l_sent, withScore = False)

    n_top = 10
    print( f'\nHere are the Top {n_top} Headlines\n----------------------------------\n')
    for hl in scored_headlines[ : n_top]:
        print(f'{hl}\n')

Main()
