#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
from sklearn.metrics import accuracy_score,precision_score,recall_score
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn import tree
from sklearn import cross_validation
data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]
clf = tree.DecisionTreeClassifier()



data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)
#print data

#print labels
"""
print "over fit"
clf.fit(features,labels)

pred = clf.predict(features)

score = accuracy_score(pred,labels)

true_positive =0

print len(pred)
print len(labels)
for i,val in enumerate(pred):
    if val == 1:
        if labels[i] == 1:
            true_positive = true_positive + 1
            
print "True Positive",true_positive
    
print "Accuracy Score:",score

"""
feature_train, feature_test, label_train, label_test = cross_validation.train_test_split(
     features, labels, test_size=0.3, random_state=42)
     
    
clf.fit(feature_train,label_train)

pred = clf.predict(feature_test)
true_positive =0
#if all pred becomes zero
for i,val in enumerate(pred):
    if val == 1:
        if label_test[i] == 1:
            true_positive = true_positive + 1
            
print "True Positive",true_positive
            
"""        
for i,val in enumerate(pred):
    if val == 1:
        pred[i] = 0
        
"""
        
score = accuracy_score(pred,label_test)
print "Prediction"
print pred
print "Accuracy Score:",score

print "Precision Score",precision_score(pred,label_test)
print "Recall Score",recall_score(pred,label_test)

### it's all yours from here forward!  


