#!/usr/bin/python

import pandas as pd
import numpy
from itertools import chain
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    #print predictions.tolist()
    error = net_worths - predictions 
    
    
    error = error * error
    
    df = pd.DataFrame({'predictions':predictions.tolist(),'ages':ages.tolist(),'net worth':net_worths.tolist(),'error':error.tolist()})
    df_sorted= df.sort('error', ascending=False).reset_index(drop=True)   
    df_cleaned = df_sorted.ix[9:]
    #print df
    length = len(numpy.array(df_cleaned['ages']))
    print ages
    print "Sorted Age"
    age_cleaned = numpy.reshape(list(chain.from_iterable(df_cleaned['ages'].tolist())),(length,1))
    #age_cleaned = age_cleaned.tolist()
    #length = len(numpy.array(df_cleaned['ages']))
    #age_cleaned = numpy.reshape(numpy.array(df_cleaned['ages']),(length, 1))
    #print "Length of age",len(age_cleaned)
    #print age_cleaned
    
    net_worth_cleaned = numpy.reshape(list(chain.from_iterable(df_cleaned['net worth'].tolist())),(length,1))
    error_cleaned = numpy.reshape(list(chain.from_iterable(df_cleaned['error'].tolist())),(length,1))
    print net_worth_cleaned
    cleaned_data = zip(age_cleaned,net_worth_cleaned,error_cleaned)

    ### your code goes here

    
    return cleaned_data
