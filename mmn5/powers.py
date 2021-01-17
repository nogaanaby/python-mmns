# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 09:59:49 2020

@author: Dani
"""

def modular_power(a,b,n):
    """ computes a**b (mod n) using iterated squaring 
        assumes b is a nonnegative integer"""
    result = 1
    while b>0:
    	if b%2 == 1:
    	    result = (result*a)%n
    	a = (a*a)%n
    	b = b//2
    return result
