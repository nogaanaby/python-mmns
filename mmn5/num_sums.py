# -*- coding: utf-8 -*-
"""
Student: Noga Anaby
ID: 318298296
Assignment no. 5
Program: num_sums.py

This program calculates all the factorization options for a given integer
"""

def setData(lineArr):
    ''' return a dictionary which include the integer to factorise and the possible parts
        if the data invalid returns an error'''
    parts=[]
    #iterates throght the line items, if possible cast into integer, if not returns an error
    for item in lineArr:
        item=item.strip()
        if item.isnumeric():
            number=int(item)
            parts.append(number)                 
        else:
            return "Error"
    
    n=parts[0]
    parts=parts[1::]
    if(len(parts)<1):
        return "Error"
    partsCopy=parts.copy()
    #iterates throght the numbers list by nested loop to ensure theres no duplicate numbers in the list
    for number in parts:
        if(number==0):
            return "Error"
        currItem=partsCopy.pop(partsCopy.index(number))
        for checkItem in partsCopy:
            if checkItem==currItem:
                return "Error"   
            
    return {"n":n,"parts":parts}



def num_sums_iterate(n,parts,currentSum):
    ''' returns an integer which represents all the factorization options for a given integer n'''
    count=0
    if currentSum==n and n!=0:
        return 1
    if currentSum>n:
        return 0
    if currentSum<n or n==0:
        #iterates throght every part, to calculate all the possibilities in every point on the tree 
        for nextNum in parts:
            count+= num_sums_iterate(n,parts,currentSum+nextNum)
        return count
    
def num_sums(n,parts):
    ''' returns an integer which represents all the factorization options for a given integer n'''
    return num_sums_iterate(n,parts,0)
    
def main():
    f=open("input_ex2.txt", "r")
    content=""
    #iterates throght every line in the text file to calculate the factorization options
    for line in f:
        lineArr=line.split(" ")
        data=setData(lineArr)
        if data=="Error":
            content+=data+"\n"
        else:
            theSum=num_sums(data["n"],data["parts"])
            content+= str(theSum) +"\n"
    f.close()
    
    o = open("output_ex2.txt", "w")
    o.write(content)
    o.close()

main()
