# **General Analysis of Normalization Part**

## DIR: data/
Several data sets scraped from [Bloomberg](www.bloomberg.com) range from Year 2015-2017(unfortunately, my ip is banned from
this website due to scraping too frequently.)

## DIR: code/
This file contains the code to vectorize the word using Word2Vec model. Also it implements
tri-gram to group several tokens and compare all trigrams with currency samples based on
similarity scores. Through implementing a DecisionTree classifier, this part can automatically
decide which part of the corpus need to be normalized. Though, the result still is not 
good enough due the input dimension and ambiguity of word vectors. (In next several weeks, we are gonna
improve the algorithm.) Till now, the results can be seen in [Need_Normalize_part.csv](https://github.com/yfmaBrandeis/CSLinguistics-131aFP/blob/master/analysis/code/Need_Normalize_part.csv).

