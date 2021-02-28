# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:55:37 2021

@author: Administrator
"""
import pandas as pd
from pandas.api.types import CategoricalDtype
def add_month_yr(x):
    '''
    create a dataframe column month-yr with ID as row-index.
    input:x
    input type:pd.Dataframe
    output:pd.Dataframe
    '''
    
    assert isinstance(x,pd.DataFrame)
    
    dict_month={'1':'Jan','2':'Feb','3':'Mar','4':'Apr','5':'May','6':'Jun',
                '7':'Jul','8':'Aug','9':'Sep','10':'Oct','11':'Nov','12':'Dec'}
    a=x['Timestamp']
    b=a.str.split('/| ',expand=True).rename(columns={0:'month',1:'day',2:'year',3:'time'})
    list_month=[dict_month[x] for x in b['month']]
    b['month']=list_month
    b['month-yr']=b.apply(lambda i:i.month+'-'+i.year,axis=1)
    x['month-yr']=b['month-yr']
    return x

def fix_categorical(x):
    '''
    take the dataframe column and then return the same dataframe with an updated 
    column othat does the sorting.
    input:x
    input type:pd.Dataframe
    output:pd.Dataframe
    '''
    
    assert isinstance(x,pd.DataFrame)
    a=CategoricalDtype(categories=['Sep-2017', 'Jan-2018', 'Feb-2018', 'Mar-2018',
                                   'Apr-2018','Sep-2018','Oct-2018','Jan-2019'],ordered=True)
    x['month-yr']=x['month-yr'].astype(a)
    return x