# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:36:27 2020

@author: User
"""

def main():
    
    m = open("output_ex1.txt", "r")
    t = open("output_ex1_correct.txt", "r")
    
    to=t.read()
    mo=m.read()
    for x in to:
        print("ok: ", to==mo)
    

    t.close()
    m.close()
    

main()