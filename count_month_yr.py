# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 13:58:44 2021

@author: Administrator
"""

import pandas as pd

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

def count_month_yr(x):
    '''
    input:x
    input type:pd.Dataframe
    output:pd.Dataframe

    '''
    assert isinstance(x,pd.DataFrame)
    
    result=x['month-yr'].value_counts()
    result=result.to_frame()
    result.rename(columns={'month-yr':'Timestamp'}, inplace=True)
    result.index.name='month-yr'
    return result
    
    
    