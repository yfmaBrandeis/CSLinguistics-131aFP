import json
from nltk.tokenize import word_tokenize,sent_tokenize
from gensim.models import Word2Vec
from nltk import ngrams
from random import randint
import pandas as pd


symbols = ['$','£','€','¥','fr']
numbers = ['1.00','100','200.34','600,000']
scales = ['hundred','thousand','million','bn','tn','']

currency_samples = [(s,n,sc) for s in symbols for n in numbers for sc in scales]

def data_prep(file):
    # reading data from file (usually a json format)
    data = json.load(open(file))
    news = [''.join(item["news_body"]) for item in data if "news_body" in item.keys()]
    news = '\n'.join(news)
    return news


def tokenize(s):
    # special format which is close to corpus.sents()
    l = [word_tokenize(sent) for sent in sent_tokenize(s)]
    l.extend(currency_samples)
    return l

def group_tokens(s):
    s = word_tokenize(s)
    return list(ngrams(s,3))


def train(s):
    # training input : sentences
    model = Word2Vec(s,min_count=1)
    return model


def word_score(model,word1,word2):
    # return similarity
    return model.wv.similarity(word1,word2)


def mean(l):
    mean = 0
    for i in l:
        mean += i
    return mean/len(l)


def group_score(model,fgram1,fgram2,method = "pair"):
    scores = []
    if method == "max":
        target = set(fgram2)
        for word1 in fgram1:
            similarity = 0
            del_word = ""
            for word2 in target:
                if word_score(model,word1,word2)>similarity:
                        similarity = word_score(model,word1,word2)
                        del_word = word2
            scores.append(similarity)
            target.remove(del_word)
    elif method == "average":
        for word1 in fgram1:
            for word2 in fgram2:
                try:
                    scores.append(word_score(model,word1,word2))
                except:
                    pass
    elif method == 'pair':
        for i in range(len(fgram1)):
            try:
                scores.append(word_score(model,fgram1[i],fgram2[i]))
            except:
                pass
    return mean(scores)


def evaluate(model,fgram,method = 'pair'):
    i = randint(0,len(currency_samples)-1)
    score = group_score(model,fgram,currency_samples[i],method)
    return score


def get_scores(model,fgrams,method='pair'):
    score_vec = [evaluate(model,fgram,method) for fgram in fgrams]
    return score_vec


if __name__ == "__main__":
    fp = "../data/BiggerData.json"
    news = data_prep(fp)
    tokens = tokenize(news)
    model = train(tokens)
    fgrams = group_tokens(news)
    pair_scores = get_scores(model,fgrams)
    average_scores = get_scores(model,fgrams,'average')
    f_s_dict = {'group_tokens':fgrams,'pair_score':pair_scores,'average_score':average_scores,'first_token':[item[0] for item in fgrams]}
    df = pd.DataFrame(data=f_s_dict)
    df.to_csv("pair&average.csv", sep='\t', encoding='utf-8',index = False)
