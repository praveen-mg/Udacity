#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
import math
import numpy as np
### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
#print data_dict
data_dict.pop( 'TOTAL', 0 )
names = data_dict.keys()
print "Total number of names",len(names)
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)
print "Length of data",len(data)
print data
max_bonus =0
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )
    if bonus > max_bonus:
        max_bonus = bonus

    
for key,val in data_dict.iteritems():
    if(val['bonus'] == max_bonus):
        print "Person with Max bonus",key
        
print "Bonus outlier", max_bonus

name_outlier = []
for key,val in data_dict.iteritems():
    if ((val['bonus'] =="NaN") or (val['salary'] =="NaN")):
        continue
    if((val['bonus'] > 5000000) and (val['salary'] > 1000000)):
        name_outlier.append(key)


print "Name of people with outlier",name_outlier

#print data_dict['CORDES WILLIAM R']
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

### your code below



