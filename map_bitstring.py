# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 17:58:39 2021

@author: Administrator
"""

def map_bitstring(x):
    '''
    takes a list of bitstrings and maps each bitstring to 0 if the number of 0s in 
    the bitstring strictly exceeds the number of 1s. Otherwise, map that bitstring to 1.
    input item: x
    input type: list
    output: dict
    
    '''
    assert isinstance(x,list)

    result=dict()
    for i in x:
        if i.count('0')>i.count('1'):
            result[i]=0
        else:
            result[i]=1
    return result