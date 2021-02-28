# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 21:07:49 2021

@author: Administrator
"""

class Interval(object):
         def __init__(self,a,b):
             """
             :a: integer
             :b: integer
             """
             assert a<b
             assert isinstance(a,int)
             assert isinstance(b,int)
             self._a = a
             self._b = b
         def __repr__(self):
             return 'Interval('+str(self._a)+','+str(self._b)+')'
         def __eq__(self,other):
             assert isinstance(self,Interval)
             assert isinstance(other,Interval)
             return self._a==other._a and self._b==other._b
         def __lt__(self,other):
             pass
         def __gt__(self,other):
             pass
         def __ge__(self,other):
             pass
         def __le__(self,other):
             pass
         def __add__(self,other):
             assert isinstance(self,Interval)
             assert isinstance(other,Interval)
             a1=self._a
             a2=other._a
             b1=self._b
             b2=other._b
             if self==other:
                 return self
             elif (b1<=a2 or b2<=a1):
                 list=[]
                 list.append(self)
                 list.append(other)
                 return list
             else:
                 if (a1<=a2 and b1<=b2):
                     return Interval(a1,b2)
                 elif (a1<=a2 and b2<=b1):
                     return Interval(a1,b1)
                 elif (a1>=a2 and b1>=b2):
                     return Interval(a2,b1)
                 elif (a1>=a2 and b2>=b1):
                     return Interval(a2,b2)
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
             