from sklearn import tree
from sklearn.svm import SVC

class Classifier:
    def __init__(self):
        print("Classifier created!")
        self.training_set = []
        self.labels = []
        self.test_set = []

    def TreeClassifier(self):
        self.clf = tree.DecisionTreeClassifier()

    def SvcClassifier(self):
        self.clf = SVC()

    def load_data(self,training,labels,test):
        self.training_set = training
        self.labels = labels
        self.test_set = test
        self.train()

    def train(self):
        self.clf.fit(self.training_set,self.labels)

    def predict(self):
        return self.clf.predict(self.test_set)