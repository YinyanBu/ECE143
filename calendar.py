# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:21:36 2021

@author: Administrator
"""

import calendar

def number_of_days(year,month):
    '''
    returns the number of calendar days in a given year and month.
    input item: year and month
    input type: int
    output: int
    
    '''
    assert isinstance(year,int)
    assert isinstance(month,int)
    assert year>0
    assert 1<=month<=12
    c,d=calendar.monthrange(year,month)
    return d

def number_of_leap_years(year1,year2):
    '''
    find the number of leap-years between (including both endpoints) two given years.
    input item: year1 and year2
    input type: int
    output: int
    
    '''
    assert isinstance(year1,int)
    assert isinstance(year2,int)
    assert year1>0
    assert year2>0
    num=calendar.leapdays(year1,year2)
    if calendar.isleap(year2):
        num=num+1
    return num

def get_day_of_week(year,month,day):
    '''
    find the string name of the day of the week on a given month,day, and year.
    input item: year month day
    input type: int
    output: list
    
    '''
    assert isinstance(year,int)
    assert isinstance(month,int)
    assert isinstance(day,int)
    assert year>0
    assert 1<=month<=12
    assert 1<=day<=31
    
    w=calendar.weekday(year,month,day)
    all=['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday', 'Sunday']
    return all[w]
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    