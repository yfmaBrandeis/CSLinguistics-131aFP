import json
from nltk.tokenize import word_tokenize,sent_tokenize
from gensim.models import Word2Vec
from nltk import ngrams
from normalization import Normalizer

normalizer = Normalizer()

symbols = list(normalizer.abbreviationDict.keys()).append

def data_prep(file):
    # reading data from file (usually a json format)
    data = json.load(open(file))
    news = [''.join(item["news_body"]) for item in data if "news_body" in item.keys()]
    news = '\n'.join(news)
    return news


def tokenize(s):
    # special format which is close to corpus.sents()
    return [word_tokenize(sent) for sent in sent_tokenize(s)]


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


def group_score(model,fgram1,fgram2,method = "max"):
    scores = []
    if method == "max":
        target = set(fgram2)
        for word1 in fgram1:
            similarity = 0
            del_word = ""
            for word2 in target:
                try:
                    if word_score(model,word1,word2)>similarity:
                        similarity = word_score(model,word1,word2)
                        del_word = word2
                except:
                    pass
            scores.append(similarity)
            target.remove(del_word)
    elif method == "average":
        for word1 in fgram1:
            for word2 in fgram2:
                scores.append(word_score(model,word1,word2))
    return mean(scores)


currency_samples = [['$',"100",'million'], ['$','100.54',''], ['USD','1.234',''] ,\
                    ['JPY','1000000',''], ['$', '26','billion'], ['$','2.45','trillion']]


if __name__ == "__main__":
    fp = "../data/BiggerData.json"
    news = data_prep(fp)
    tokens = tokenize(news)
    model = train(tokens)
    fgrams = group_tokens(news)
