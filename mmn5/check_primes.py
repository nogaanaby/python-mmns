# -*- coding: utf-8 -*-
"""
Student: Noga Anaby
ID: 318298296
Assignment no. 5
Program: primes_check.py

This program gets very large integers and calculates whether they are prime numbers or not
"""
import math
import random
import powers


def odd(k):
    ''' returns the "even degree" of the given integer k '''
    if k%2==0:
        return odd(k//2)
    else:
        return k

def even(k):
    ''' returns the "odd part" of the given integer k '''
    s=int(math.log2(k))
    while k%(2**s)!=0:
        s-=1
    else:
        return s

def get_even_odd_parts(n):
    ''' returns a dictionary which has both the "odd part" and the "even degree" of the given integer n '''
    return {"t":odd(n),"s":even(n)};


def is_probubly_prime(n, num_iterations):
    ''' retruns True if the given integer n has big changce of being a prime number'''
    s=even(n-1)
    t=odd(n-1)
    lap=num_iterations
    #run num_iterations times to increase accuracy
    while lap>0:
        if(is_suspected_prime(n,t,s)==False):
            return False
        lap-=1
    return True


def is_suspected_prime(n,t,s):
    ''' retruns True if the given n integer might be a prime number'''
    a=random.randint(2,n-1)
    d=powers.modular_power(a,t,n)
    if d==1 or d==(n-1):
        return True
    for i in range(1,s):
        d=powers.modular_power(d,2,n)
        if d==(n-1):
            return True
    return False

def main():    
    f = open("input_ex1.txt", "r")
    output=""
    #iterates throght every line in the text file to calculate whether the current number is a prime number or not
    for x in f:
      x=int(x)
      if(is_probubly_prime(x,10)):
          output+=str(x)+" is prime\n"
      else:
          output+=str(x)+" is not prime\n"
    f.close()
    
    o = open("output_ex1.txt", "w")
    o.write(output)
    o.close()

main()




