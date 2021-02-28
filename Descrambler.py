# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 19:40:49 2021

@author: Administrator
"""

import itertools
import collections

def descrambler(w, k):
    '''

    input item: w,k
    input type: string,tuple
    output: list
    
    '''

    assert isinstance(w, str)
    assert w.isalpha()
    assert isinstance(k, tuple)
    assert len(k)>0
    assert len(w)>0
    for i in w:
        assert i.islower()
    sum=0
    for j in k:
        assert isinstance(j,int)
        assert j > 0
        sum=sum+j
    assert len(w)==sum
    
    a=list(w)
    b=dict()
    for i in a:
        if b.get(i)==None:
            b[i]=1
        else:
            b[i]=b[i]+1
    
    #open txt and convert to dict 
    line=[]
    with open('/tmp/google-10000-english-no-swears.txt') as f:
        for i in f.readlines():
            line.append(i.strip('\n'))
    words=dict(zip(line, range(len(line))))
    
    #permuate and combine
    d=[[] for _ in range(len(k))]
    perm=dict()
    for i in range(len(k)):
        perm[i]=itertools.permutations(a, k[i])
        for j in perm[i]:
            ele=''.join(j)
            if ele in words and ele not in d[i]:
                d[i].append(ele)
    comb=itertools.product(*d)
    
    #output result
    for i in comb:
        check=''
        output=''
        for j in range(len(i)):
            check=check+i[j]
            if j !=len(i)-1:
                output=output+i[j]+' '
            else:
                output=output+i[j]
            if collections.Counter(check)==b: 
                yield output
        
    
                
    
    
    
    