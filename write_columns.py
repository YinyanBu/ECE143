# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 11:22:11 2021

@author: Administrator
"""

def write_columns(data,fname):
    '''
    write 3 formula to three columns to a comma-separated file
    input item: data and fname
    input type: list and string
    output: None
    
    '''
    assert isinstance(data,list)
    assert isinstance(fname,str)
    for i in data:
        assert isinstance(i,(int,float))
    f=open(fname,'w')
    for i in data:
        f.write('{:.2f},{:.2f},{:.2f}\n'.format(i,i**2,(i+i**2)/3))
    f.close()
        
    