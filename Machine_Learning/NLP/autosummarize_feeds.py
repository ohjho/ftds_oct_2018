# Preliminary
import requests, json, re, feedparser
import nltk
import pandas as pd
import numpy as np

from bs4 import BeautifulSoup
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import WordNetLemmatizer
from newspaper import Article

def GetArticleRSS( lRSS , getSummary = True, verbose = 0 ):
    posts = []
    for url in lRSS:
        if verbose:
            print(f'Getting feed from {url}...')
        feed = feedparser.parse(url)

        for post in feed.entries:
            if verbose:
                print(f' Saving {post.title}: article length {len(post.content[0].value)}, summary length {len(post.summary)}')

            content = post.content[0].value
            if getSummary:
                content = post.summary

            posts.append([post.title, post.link, content])

    df = pd.DataFrame(posts, columns=['title', 'link', 'content'])
    return df

def GetNewsRSS( lRSS, verbose =0, max_articles = 100):
    posts = []
    art_count = 0

    if verbose:
        print(f'Getting you {max_articles} articles...')

    for rss_index, url in enumerate(lRSS):
        if verbose:
            print(f'Getting feed from {url}...')
        feed = feedparser.parse(url)

        for post in feed.entries:
            if verbose:
                print(f' Saving {post.title}: {post.link}')

            art_count += 1

            post_url = post.link
            content = Article(post_url)
            content.download()
            content.parse()
            content.nlp()
            posts.append([post.title, post_url, content.text, content.summary])

            if art_count >= max_articles:
                break

    df = pd.DataFrame(posts,
            columns=['title', 'link', 'content', 'baseline_summary'])
    return df

def GetZenArticles():
    raw_rss = [
        'https://zennist.typepad.com/zenfiles/atom.xml'
    ]
    return GetNewsRSS( raw_rss, verbose = 1, max_articles = 1)

def cleanText( inTxt ):
    soup = BeautifulSoup(inTxt, 'html.parser')
    raw = soup.get_text()
    raw = raw.replace(u'\xa0', u' ')
    raw = raw.replace(u'\n', u' ')
    return raw

def getTok( inTxt ):
    our_stopwords = set( stopwords.words('english') + list(punctuation))

    # Make the words to lower
    txt = inTxt.lower()

    # Remove None Alphabetic Characters
    txt_nd = re.sub('[^A-za-z]', ' ', txt)

    wtok = [w for w in word_tokenize( txt_nd) if w not in our_stopwords]
    stok = sent_tokenize( txt)

#     # stemming
#     stemmer = PorterStemmer()
#     for i in range(len(wtok)):
#         wtok[i] = stemmer.stem( wtok[i])

    # lemmatize
    lemmatizer = WordNetLemmatizer()
    for i in range(len(wtok)):
        wtok[i] = lemmatizer.lemmatize( wtok[i])

    return wtok, stok

def GetCorpus():
    feeds = GetZenArticles()
    feeds['clean_content'] = feeds['content'].apply(lambda x : cleanText(x))
    feeds['word_tok'] = feeds['clean_content'].apply( lambda x : getTok(x)[0] )
    feeds['sent_tok'] = feeds['clean_content'].apply( lambda x : getTok(x)[1] )
    return feeds

def SimpleSummarize( lWords, lSent, withScore = False, n_top = 10):
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

    n_top = min( n_top, len(sent_sorted))
    return sent_sorted[: n_top]

def SummarizeCorpus( dfCorpus , withScore = False, n_top = 10):
    outdf = dfCorpus
    outdf['summary'] = outdf.apply(
        lambda x: SimpleSummarize(x.word_tok, x.sent_tok, withScore = withScore, n_top = n_top),
        axis = 1
        )

    return outdf

def Main():
    dfCorpus = GetCorpus()
    dfSummary = SummarizeCorpus( dfCorpus, withScore = False, n_top = 3)
    show_basline = True

    print( f'\nHere are our feeds summary Headlines\n----------------------------------\n')
    for index, row in dfSummary.iterrows():
        print(f'Title: {row.title}')
        print(f'Summary:\n {" ".join(row.summary)}\n')
        if show_basline:
            print(f'Summary by the newspaper package: \n{row.baseline_summary}\n')

Main()
