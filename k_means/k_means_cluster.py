#!/usr/bin/python 

""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
import math
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

from sklearn.cluster import KMeans
from sklearn import preprocessing

def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
#print data_dict[]

    #print "Min stock:", val['exercised_stock_options']
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)

value_stock = []
value_salary = []
for key,val in data_dict.iteritems():
    if (not math.isnan(float(val['exercised_stock_options']))):
        
        value_stock.append(float(val['exercised_stock_options']))
    if (not math.isnan(float(val['salary']))):
        value_salary.append(float(val['salary']))
        if val['salary'] == 200000:
            print "Value is available"
#print value
print "Minimum stock Value:",min(value_stock)
print "Maximum stock Value:",max(value_stock)

print "Minimum salary:", min(value_salary)
print "Maximum salary:", max(value_salary)
value_array_stock  = numpy.array([min(value_stock),1000000.,max(value_stock)])
value_array_salary = numpy.array([min(value_salary),200000.,max(value_salary)])
#value_salary_array = numpy.array([])
#print "Arg of Salary:",value_salary_array.argwhere(200000)
scaler = preprocessing.MinMaxScaler()
train_minmax_stock = scaler.fit_transform(value_array_stock)
print train_minmax
train_minmax_salary = scaler.fit_transform(value_array_salary)
print train_minmax_salary 
k_means = KMeans(n_clusters=2)

#k_means.fit(features)
#pred = k_means.predict(features)
### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
#feature_3 = "total_payments"
poi  = "poi"
features_list = [poi,feature_1, feature_2]
data = featureFormat(data_dict, features_list )
#print data
poi, finance_features = targetFeatureSplit( data )
#print finance_features
k_means.fit(finance_features)
pred = k_means.predict(finance_features)
### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
#print data_dict
for f1, f2 in finance_features:
    plt.scatter( f1, f2)
plt.show()
scaler = preprocessing.MinMaxScaler()

    
#salary = numpy.array(salary)
#stock  = numpy.array(stock)

    
#train_minmax = scaler.fit_transform(salary,stock)

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred




### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
    Draw(pred, finance_features, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print "no predictions object named pred found, no clusters to plot"
