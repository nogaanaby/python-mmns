# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


        
def main():
    listInt=[]
    flag=True
    
    while flag:
        getInp=int(input("enter int: "))
        for x in listInt:
            if x==getInp:
                flag=False
                break
            
        listInt.append(getInp)
        listInt.sort()
        if flag:
            print(listInt)
        
        

main()