# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 09:51:10 2021

@author: Administrator
"""

import pandas as pd

def split_count(x):
    '''
    take column as input and output the Pandas dataframe.
    input:x
    input type:pd.Series
    output:pd.Dataframe

    '''
    assert isinstance(x,pd.Series)
    
    a=x.str.split(', ').apply(pd.Series)
    b=a[0]
    for i in range(1,a.shape[1]):
        b=b.append(a[i],ignore_index=True)
    result=b.value_counts(ascending=True)
    result=result.to_frame()
    result.rename(columns={0: 'count'}, inplace=True)
    return result
    
    
    