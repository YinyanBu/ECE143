# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 18:28:28 2021

@author: Administrator
"""

def gather_values(x):
    '''
    Generate a new dictionary with bitstrings as keys and with values as lists that 
    contain the corresponding mapped values from map_bitstring.
    input item: x
    input type: list
    output: dict
    
    '''
    assert isinstance(x,list)
    result=dict()
    for i in x:
        result[i]=[]
    for j in x:
        if j.count('0')>j.count('1'):
            result[j].append(0)
        else:
            result[j].append(1)
    return result
     