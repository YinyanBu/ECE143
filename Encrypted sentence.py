# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:54:22 2021

@author: Administrator
"""
import string
def encrypt_message(message,fname):
    '''
    Given `message`, which is a lowercase string without any punctuation, and `fname` which is the
    name of a text file source for the codebook, generate a sequence of 2-tuples that
    represents the `(line number, word number)` of each word in the message. The output is a list
    of 2-tuples for the entire message. Repeated words in the message should not have the same 2-tuple. 
 
    :param message: message to encrypt
    :type message: str
    :param fname: filename for source text
    :type fname: str
    :returns: list of 2-tuples
    '''
    assert isinstance(message,str)
    assert isinstance(fname,str)
    assert message.islower()
    information=message.replace(' ','')
    assert information.isalpha()
    
    with open(fname,'r') as f:
        line=f.readlines()
    a=message.split()
    location=dict()
    
    for i in range(len(line)):
        b=line[i].translate(str.maketrans('','',string.punctuation))
        b=b.lower()
        b=b.split()
        for j in range(len(b)):
            if b[j] not in location:
                location[b[j]]=[]
                location[b[j]].append((i+1,j+1))
            else:
                location[b[j]].append((i+1,j+1))
    
    c=dict()
    for k in a:
        c[k]=c.get(k,0)+1
        assert c[k]<=len(location[k])
        
    result=[]
    for i in a:
        d=0
        situation=location[i][d]
        while True:
            if situation not in result:
                result.append(situation)
                break
            elif situation in result:
                d=d+1
                situation=location[i][d]
    return result

def decrypt_message(inlist,fname):
    '''
    Given `inlist`, which is a list of 2-tuples`fname` which is the
    name of a text file source for the codebook, return the encrypted message. 
   
    :param message: inlist to decrypt
    :type message: list
    :param fname: filename for source text
    :type fname: str
    :returns: string decrypted message
    '''
    assert isinstance(inlist,list)
    for i in inlist:
        assert isinstance(i,tuple)
        assert len(i)==2
    assert isinstance(fname,str)
    
    with open(fname,'r') as f:
        line=f.readlines()
    location=dict()
    
    for i in range(len(line)):
        b=line[i].translate(str.maketrans('','',string.punctuation))
        b=b.lower()
        b=b.split()
        for j in range(len(b)):
            if b[j] not in location:
                location[b[j]]=[]
                location[b[j]].append((i+1,j+1))
            else:
                location[b[j]].append((i+1,j+1))
    
    result=[]
    for i in inlist:
        for j,k in location.items():
            if i in location[j]:
                result.append(j)
                break
    result=' '.join(result)
    return result
    
    
    
                
        
    