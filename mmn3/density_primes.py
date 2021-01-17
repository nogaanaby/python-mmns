# -*- coding: utf-8 -*-
"""
Student: Noga Anaby
ID: 318298296
Assignment no. 3
Program: density_primes.py

This program takes 100000 random numbers between 10^9 and 10^9\2,
and prints the percentage value of the total prime numbers out of them,
Then it prints the approximation of the percentage of the total primes between 1 to 10^9
"""
import math
import random

def is_prime(num):
    """ return true if the given number @num is a prime number and false otherwise """
    if(num%2 == 0):
        if (num != 2):
            return  False
    for i in range(3,int(math.sqrt(num))+1, 2):
        if (num%i == 0):
            return False
    return True

def main():
    max=math.pow(10,9)
    randomList=[random.randint(max/2, max) for i in range(100000)]
    countPrimes=0
    #iterate through all the numbers in the randomList list and count the number of the primes
    for num in randomList:
        if is_prime(num):
            countPrimes+=1
    densityOfprimes = round(countPrimes/100000,4)
    expectedDensity = round(1/math.log(max),4)
    print("density of primes: "+str(densityOfprimes)+"\n"+"expected density: "+str(expectedDensity)+"\n")

main()
