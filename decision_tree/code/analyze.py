from classifier import Classifier
import numpy
import pandas as pd

#prepare data
data = numpy.load("data.npz")
train = data['train']
test = data['test']
labels = data['labels']

#create classifier
clf = Classifier()
clf.TreeClassifier()
clf.load_data(training=train,labels=labels,test=test)
results = clf.predict()


df = pd.read_csv("pair&average.csv",sep='\t')
def TF(x):
    if x == 0:
        return False
    else:
        return True
results = [TF(x) for x in results]
TF = pd.Series(results)
df['Need_normalize'] = TF
newdf = df[df['Need_normalize']==True]

#output DataFrame
newdf.to_csv("Need_Normalize_part.csv")