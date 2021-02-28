# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 17:53:14 2021

@author: Administrator
"""

from time import sleep
import random
from datetime import datetime
import itertools as it
from types import GeneratorType
 
def tracker(p,limit):
    '''
    tracks the output of this producer and ultimately returns the number of odd 
    numbered seconds that have been iterated over.
    input item: p and limit
    input type: generator and int
    output: int
    
    '''
    assert isinstance(p,GeneratorType)
    assert isinstance(limit,int)
    assert limit>0
    count=0
    while count<limit:
        a=next(p)
        b=a.seconds
        if not(b%2==0):
            count=count+1
        c=yield count  # receive from send
        if c:
            limit=c