# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 19:34:06 2021

@author: User
"""

def main():
    f = open('input_ex2.txt', 'r')
    lines = f.readlines()
    invalid_syntax = ''
    for line in lines:
        for l in line:
            if l.isalpha():
                lines.remove(line)
                break;
    print(lines)
main()
    
