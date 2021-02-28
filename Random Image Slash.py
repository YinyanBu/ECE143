# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:19:22 2021

@author: Administrator
"""

import numpy as np
import random

def gen_rand_slash(m=6,n=6,direction='back'):
    '''
    
    input:m,n,direction
    input type:int,int,string
    output:numpy.ndarray
    
    '''
    assert isinstance(m,int)
    assert m>1
    assert isinstance(n,int)
    assert n>1
    assert isinstance(direction,str)
    assert direction=='back' or direction=='forward'
    
    if direction=='back':
        result=np.zeros((m,n))
        loc_m=random.choice(range(m-1))
        loc_n=random.choice(range(n-1))
        length=random.choice(range(2,min(m-loc_m-1,n-loc_n-1)+2))
        for i in range(length):
            if loc_m>=m or loc_n>=n:
                break
            result[loc_m][loc_n]=1
            loc_m+=1
            loc_n+=1
    else:
        result=np.zeros((m,n))
        loc_m=random.choice(range(m-1))
        loc_n=random.choice(range(1,n))
        length=random.choice(range(2,min(m-loc_m-1,loc_n)+2))
        for i in range(length):
            if loc_m>=m or loc_n<0:
                break
            result[loc_m][loc_n]=1
            loc_m+=1
            loc_n-=1
    return result
            
        
        
    