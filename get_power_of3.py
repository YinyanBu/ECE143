# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 22:16:35 2021

@author: Administrator
"""

def get_power_of3(n):
    '''
    construct any number between 1 and 40 with {1,3,9,27}
    input item: n
    input type: int
    output type: list
    '''
    assert isinstance(n,int)
    assert n >= 1 and n <= 40
    import itertools
    all = itertools.product([0,1,-1], repeat=4)
    a = list(all)
    for i in a:
        if (1*i[0]+3*i[1]+9*i[2]+27*i[3]) == n:
            break
    result=list(i)
    return result