# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 09:20:01 2021

@author: Administrator
"""
import os
def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''
    assert isinstance(fname,str)
    assert isinstance(n,int)
    assert n>0
    
    total=os.path.getsize(fname)
    average=total/n
    numof_file=0
    length=0
    name_of_file='{}_00{}.txt'.format(fname,numof_file)
    g=open(name_of_file,'wt')
    
    count=0
    with open(fname,'rt') as f:
        for line in f:
            length=length+len(line)
            if length>average:
                g.close()
                numof_file=numof_file+1
                name_of_file='{}_00{}.txt'.format(fname,numof_file)
                g=open(name_of_file,'wt')
                count=count+1
                length=len(line)
                if numof_file==n-1:
                    average=average**3
            g.write(line)
            
    f.close()
    g.close()
                
            
    
    
    
            
    
            