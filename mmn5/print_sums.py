# -*- coding: utf-8 -*-
"""
Student: Noga Anaby
ID: 318298296
Assignment no. 5
Program: print_sums.py

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



def print_sums_iterate(n,parts,currentSum,concat):
    ''' returns all the factorization options for a given integer n'''
    sequense= ""
    if currentSum==n and n!=0:
        return str(n)+" = "+concat[:len(concat)-3:]+"\n"
    if currentSum>n:
        return ""
    if currentSum<n or n==0:
        #iterates throght every part, to calculate all the possibilities in every point on the tree 
        for nextNum in parts:
          nextStr=str(nextNum)
          sequense+= print_sums_iterate(n,parts,currentSum+nextNum,concat+nextStr+" + " )
    
    return sequense

def print_sums(n,parts):
    '''call the recrusive function and returns all the factorization options for a given integer n'''
    content=print_sums_iterate(n,parts,0,"")
    partstring=str(parts)
    return "%s as sum of %s:\n%s"%(n,partstring,content)

def main():
    f=open("input_ex3.txt", "r")
    content=""
    #iterates throght every line in the text file to calculate the factorization options
    for line in f:
        line=line.strip()
        lineArr=line.split(" ")
        data=setData(lineArr)
        if data=="Error":
            content+=line+"\nError\n\n"
        else:
            theSum=print_sums(data["n"],data["parts"])
            content+= theSum +"\n"
    f.close()
    
    o = open("output_ex3.txt", "w")
    o.write(content)
    o.close()

main()

'''
piece and love, best regards,
Served under the auspices of 
Noga Banana first of her name
mother of cats and breaker of chains
'''
