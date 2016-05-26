#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
print "Taining Data"
clf = SVC(kernel="rbf")

print "Before Train"
clf.fit(features_train[:len(features_train)/100],labels_train[:len(labels_train)/100])
print "Before Prediction"
pred = clf.predict(features_test)

print "After Prediction"

acc= accuracy_score(pred,labels_test)

print "Accuracy value is:",acc
#########################################################
### your code goes here ###

#########################################################


