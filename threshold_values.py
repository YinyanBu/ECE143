# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 19:30:20 2021

@author: Administrator
"""
import heapq
def threshold_values(seq,threshold=1):
    '''
    threshold those values based upon their frequency and value.
    input item: seq,threshold
    input type: list,int
    output: dict
    
    '''
    assert isinstance(seq,list)
    assert isinstance(threshold,int)
    assert threshold>0
    classify=dict()
    for i in seq:
        if classify.get(i)==None:
            classify[i]=1
        else:
            classify[i]=classify[i]+1
    assert threshold<=len(classify.keys())
    belong_one=[]
    for key,value in classify.items():
        if key.count('0')<=key.count('1'):
            belong_one.append(value)
    topbig=heapq.nlargest(threshold, belong_one)
    list1=[]
    for i in range(len(topbig)-1):
        for key,value in classify.items():
            if key.count('0')<=key.count('1'):
                if value==topbig[i]:
                    list1.append(key)
    list2=[]
    for key,value in classify.items():
        if key.count('0')<=key.count('1'):
            if value==topbig[-1]:
                list2.append(key)
    winner=heapq.nsmallest((threshold-len(list1)), list2)
    final=list1+winner
    for key,value in classify.items():
        if key in final:
            classify[key]=1
        else:
            classify[key]=0
    return classify
                
                
    
            
    
    