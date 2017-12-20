import pandas as pd
import random
import numpy
# This program randomly select 200 negative samples and 100 positive samples in
# this large corpus。
df = pd.read_csv("pair&average.csv",sep='\t')

condition1 = df['average_score']>0.9
condition2 = df['pair_score']>0.9
condition3 = df['first_token'] == '$'
condition4 = df['first_token'] != '$'

positive = df[condition1 & condition2 & condition3]
negative = df[condition1 & condition2 & condition4]

pos_indices = list(positive.index)
neg_indices = list(negative.index)

pos_indices = random.sample(pos_indices,200)
neg_indices = random.sample(neg_indices,100)

neg_df = df.iloc[neg_indices,[0,3]]
pos_df = df.iloc[pos_indices,[0,3]]
test = df.iloc[list(df.index),[0,3]].values

neg = neg_df.values
pos = pos_df.values
train = numpy.append(neg,pos,axis=0)
labels = [0 for i in range(200)]
labels.extend([1 for i in range(100)])
numpy.savez('data.npz',train = train,labels = labels,test = test)
