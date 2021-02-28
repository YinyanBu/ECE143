# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 19:43:45 2021

@author: Administrator
"""

from fractions import Fraction

class Rational:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        assert isinstance(x,int)
        assert isinstance(y,int)
    def __repr__(self):
        result=Fraction(self.x,self.y)
        if result._denominator==1:
            return '%d'%result._numerator
        return '%d/%d'%(result._numerator,result._denominator)
    def __float__(self):
        return float(self.x/self.y)
    def __int__(self):
        return int(self.x/self.y)
    def __add__(self, other):
        addsum=Fraction(self.x,self.y)+Fraction(other.x,other.y)
        return Rational(Fraction(addsum)._numerator,Fraction(addsum)._denominator)
    def __sub__(self, other):
        subsum=Fraction(self.x,self.y)-Fraction(other.x,other.y)
        return Rational(Fraction(subsum)._numerator,Fraction(subsum)._denominator)
    def __mul__(self, other):
        if not isinstance(other,(int,float)):
            product=Fraction(self.x*other.x,self.y*other.y)
            return Rational(product._numerator,product._denominator)
        product=Fraction(self.x,self.y)*Fraction(other)
        return Rational(Fraction(product)._numerator,Fraction(product)._denominator)
    def __truediv__(self, other):
        if not isinstance(other,(int,float)):
            divid=Fraction(other.x,other.y)/Fraction(self.x,self.y)
            return Rational(Fraction(divid)._numerator,Fraction(divid)._denominator)
        divid=Fraction(self.x,self.y)/Fraction(other)
        return Rational(Fraction(divid)._numerator,Fraction(divid)._denominator)
    def __rtruediv__(self, other):
        if not isinstance(other, (int,float)):
            divid=Fraction(other.x,other.y)/Fraction(self.x,self.y)
            return Rational(Fraction(divid)._numerator,Fraction(divid)._denominator)
        result1=Fraction(self.x, self.y)
        result2=Fraction(other)
        divid=result2/result1
        return Rational(Fraction(divid)._numerator,Fraction(divid)._denominator)
    def __neg__(self):
        return Rational(-self.x,self.y)
    def __lt__(self, other):
        result1=Fraction(self.x,self.y)
        result2=Fraction(other.x, other.y)
        if result2<result1:
            return False
        elif result1<result2:
            return True
        else:
            return NotImplemented
    def __eq__(self, other):
        if self.x==other.x:
            if self.x==other.x:
                return True 
        else:
            return False
            
def square_root_rational(x,abs_tol=Rational(1,1000)):
    '''
    takes an input rational number x and returns the square root of to 
    absolute precision abs_tol.
    input:x,abs_tol
    input type:Rational
    output:Rational
    '''
    assert isinstance(x,Rational)
    assert isinstance(abs_tol,Rational)
    assert float(x)>0
    
    low_bound=0
    high_bound=float(x)
    mid=(low_bound+high_bound)/2
    while abs(float((mid*mid-float(x))))>float(abs_tol):
        if mid*mid<float(x):
            low_bound=mid
        else:
            high_bound=mid
        mid=(low_bound+high_bound)/2.0
    return mid
    
    
    