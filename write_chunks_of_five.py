# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 12:16:19 2021

@author: Administrator
"""

def write_chunks_of_five(words,fname):
    '''
    Using corpus of 10,000 common English words to create a new file that consists of 
    each consecutive non-overlapping sequence of five lines merged into one line.
    input item: words and fname
    input type: list and string
    output: None
    
    '''
    assert isinstance(words,list)
    assert isinstance(fname,str)
    for i in words:
        assert isinstance(i,str)
    f=open(fname,'w')
    for num,element in enumerate(words):
        if (num%5)==4:
            f.write('{}\n'.format(element))
        else:
            f.write('{} '.format(element))
    f.close()
    