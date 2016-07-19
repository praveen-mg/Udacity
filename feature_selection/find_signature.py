#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
from sklearn import tree
from sklearn.metrics import accuracy_score
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime

features_train = features_train[:150].toarray()

print len(features_train)

#print len(features_train)

labels_train   = labels_train[:150]


#prediction 
clf = tree.DecisionTreeClassifier()

clf = clf.fit(features_train, labels_train)
pred_train = clf.predict(features_train)
pred_test = clf.predict(features_test)

score_train = accuracy_score(pred_train,labels_train)
score_test = accuracy_score(pred_test,labels_test)
print "Score of train",score_train
print  "Score of test",score_test

#find important feature

#count = 0
#importance = clf.feature_importances_

importances = clf.feature_importances_
importance_list = []

index = 0
val_index = []
print "important values"

for val in importances:
    if val > 0.2:
        importance_list.append(val)
        val_index.append(index)
    index = index+1
        
    
        
#print importance_list,val_index
val = val_index[0]
vocab = vectorizer.get_feature_names()
print "Total number of importane words",len(importance_list)
print "Problem is caused by the words",vocab[val]
### your code goes here



