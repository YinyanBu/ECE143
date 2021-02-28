# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 13:28:22 2021

@author: Administrator
"""
from itertools import product
from math import pow
from functools import reduce
import random
def multinomial_sample(n,p,k=1):  
    '''                                                                 
    Return samples from a multinomial distribution.                     
                                                                             
    n:= number of trials                                                
    p:= list of probabilities                                           
    k:= number of desired samples                                       
    '''                         
    assert isinstance(n,int)
    assert n>0
    assert isinstance(p,list)
    assert sum(p)==1
    assert isinstance(k,int)
    assert k>0
         
    all_list=[]
    a=len(p)
    for i in (product(list(range(n+1)), repeat=a)):
        if sum(i)==n:
            i=list(i)
            all_list.append(i)
    b=reduce(lambda x, y: x*y,range(1,n+1))
    
    prob=[]
    for i in all_list:
        c=b
        for j in i:
            if j==0:
                c=c*pow(p[i.index(j)],j)
            else:
                c=c*(pow(p[i.index(j)],j)/(reduce(lambda e,f: e*f,range(1,j+1))))
        prob.append(c)
        
    result=random.choices(all_list,prob,k=k)
    return result
                
    
         
        
         
         
            
         