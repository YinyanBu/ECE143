# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 15:41:10 2021

@author: Administrator
"""
import random
def get_sample(nbits=3,prob=None,n=1):
    '''
    return a list n of random samples from a finite probability mass function defined 
    by a dictionary with keys defined by a specified number of bits.
    input item: nbits,prob,n
    input type: int
    output: list
    
    '''
    assert isinstance(nbits,int)
    assert nbits>0
    assert isinstance(n,int)
    assert n>0
    assert isinstance(prob,dict)
    for i in prob.values():
        assert 0<=i<=1
    assert sum(prob.values())==1
    assert len(prob.values())==2**nbits
    for j in prob.keys():
        assert len(j)==nbits
    weights=list(prob.values())
    population=list(prob.keys())
    result=random.choices(population,weights,k=n)
    return result
    
    