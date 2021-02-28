# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def compute_sum_to_n(n):
    '''
    computes the sum of all non-negative integers up to and including a specified value n
    parameter item: n
    type item: int

    '''
    assert isinstance(n,int)
    assert n >= 0
    sum=0
    number=0
    while number<=n:
        sum=sum+number
        number=number+1
    return sum

