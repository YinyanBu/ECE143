# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:49:47 2021

@author: Administrator
"""

def fibonacci(n):
    '''
    compute the first n Fibonacci numbers.
    input item: n
    input type: int
    output: list
    
    '''
    assert isinstance(n,int)
    assert n>0
    count=0
    x=1
    y=1
    while count<n:
        yield x
        x,y=y,x+y
        count=count+1
        