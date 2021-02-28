# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:44:18 2021

@author: Administrator
"""

from urllib.request import urlopen
u='https://storage.googleapis.com/class-notes-181217.appspot.com/google-10000-english-no-swears.txt'
response = urlopen(u)
words = [i.strip().decode('utf8') for i in response.readlines()]

def get_average_word_length(words):
    '''
    Compute the average length of the words.
    input:words
    input type:list
    output:float

    '''
    assert isinstance(words,list)
    for i in words:
        assert isinstance(i,str)
    assert len(words)!=0
    
    sum=0
    for i in words:
        sum=sum+len(i)
    average=sum/len(words)
    return average
    
def get_longest_word(words):
    '''
    get the longest word.
    input:words
    input type:list
    output:string

    '''
    assert isinstance(words,list)
    for i in words:
        assert isinstance(i,str)
    assert len(words)!=0
    
    longest=''
    for i in words:
        if len(i)>len(longest):
            longest=i
    return longest

def get_longest_words_startswith(words,start):
    '''
    get the longest word that starts with a single letter.
    input:words,start
    input type:list,string
    output:string

    '''
    assert isinstance(start,str)
    assert len(start)==1
    assert start.isalpha()==True
    assert isinstance(words,list)
    for i in words:
        assert isinstance(i,str)
    assert len(words)!=0
    
    longest=''
    for i in words:
        if i[0]==start:
            if len(i)>len(longest):
                longest=i
    return longest

def get_most_common_start(words):
    '''
    get the most common starting letter.
    input:words
    input type:list
    output:string

    '''
    assert isinstance(words,list)
    for i in words:
        assert isinstance(i,str)
    assert len(words)!=0
    
    common_list=dict()
    for i in words:
        if i[0] not in common_list.keys():
            common_list[i[0]]=1
        else:
            common_list[i[0]]=common_list[i[0]]+1      
    most_common=''
    most=0
    for j in common_list.keys():
        if common_list[j]>most:
            most=common_list[j]
            most_common=j
    return most_common

def get_most_common_end(words):
    '''
    get the most common ending letter.
    input:words
    input type:list
    output:string

    '''
    assert isinstance(words,list)
    for i in words:
        assert isinstance(i,str)
    assert len(words)!=0
    
    common_list=dict()
    for i in words:
        if i[-1] not in common_list.keys():
            common_list[i[-1]]=1
        else:
            common_list[i[-1]]=common_list[i[-1]]+1      
    most_common=''
    most=0
    for j in common_list.keys():
        if common_list[j]>most:
            most=common_list[j]
            most_common=j
    return most_common
        
                
                
                
                
                
                
                
                
                
                
            
    
    
    
    
    
    
    
    
    
    
    