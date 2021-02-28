# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 16:06:54 2021

@author: Administrator
"""

def slide_window(x,width,increment):
    '''
    take the window width and the window increment as inputs and should produce a 
    sequence of overlapping lists from the input list.
    input item: x ,width and increment
    input type: list and int
    output: list
    
    '''
    assert isinstance(x,list)
    assert isinstance(width,int)
    assert isinstance(increment,int)
    assert width>0
    assert increment>0
    
    result=[]
    for i in range(0,len(x),increment):
        if i<=len(x)-width:
            result.append(x[i:i+width])
    return result
    