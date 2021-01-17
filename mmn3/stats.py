# -*- coding: utf-8 -*-
"""
Student: Noga Anaby
ID: 318298296
Assignment no. 3
Program: stats.py

This program calculates data which is lists of floats,
in order to check validness and achieve the average, 
median and the standard deviation of the lists.

list_to_string*            
            "כתבו פונקציה list_to_string שמקבלת מחרוזת המורכבת ממספרים ממשיים
            המופרדים ברווחים ומחזירה רשימה המכילה את המספרים האלה"
I am totally aware of the output as float: x.0, 
but since the question requires to output them as numbers, 
I guess the floating state is the desired one rather than checking every 
number whether the int casting more suitable or not.      
"""

import math
def isfloat(st):
    ''' return true if the given string is a valid float and false otherwise'''
    totalPoints=0
    i=0
    if st[0]=="+" or st[0]=="-":
        i+=1
    if i!=len(st)-1 and st[i]=="0":
        i+=1
        if i!=len(st)-1 and st[i]!=".":
            return False
    #iterate throght the rest of the characters and check if they are valid
    while i<=len(st)-1:
        if totalPoints>1:
            return False
        if st[i]==".":
            if i==0 or st[i-1].isdigit()==False or i==len(st)-1:
                return False
            else:
                totalPoints+=1
                i+=1
                continue
        elif st[i].isdigit()==False:
            return False
        i+=1        
    
    return True

def string_to_list(st):
    ''' return a list of floats from the given string @st'''
    strList = st.split()
    floatList=[]
    #iterate through the floatList and check whether the items are valid floats, if so it appends the floats in the returned list, if not it returns "none"
    for x in strList:
        if(isfloat(x)!=True):
            return "None"
        else:
            #left a comment above#
            floatList.append(float(x))
    return floatList   

def mean(flist):
   ''' return the average of the floats in the given list @flist'''
   average=sum(flist) / len(flist) 
   return average

def sd(flist):
    ''' return the standard deviation of the floats in the given list @flist'''
    avg=mean(flist)
    flistSum=0
    #iterate throght the list of floats and summerize the remainder of every item with the list average in the power of 2
    for x in flist:
      flistSum+=pow(x-avg,2) 
    return math.sqrt( (1/len(flist))*flistSum )
    
def newSort(flist):
    ''' return a sorted float list in an ascending order'''
    newFlist=flist.copy()
    #iterate throght the list and compare two consecutive items, 
    #if the smaller is the next item it moves the smaller 1 index down if it can, and check the previous items as well
    #if not, it continue to the next item
    for x in range(len(newFlist)-1):
        item1=newFlist[x]
        item2=newFlist[x+1]
        if item2<item1:
            newFlist[x]=item2
            newFlist[x+1]=item1
            y=x
            while y>0:
                item1=newFlist[y]
                item2=newFlist[y-1]
                if item2>item1:
                    newFlist[y]=item2
                    newFlist[y-1]=item1
                y-=1
        x+=1
    return newFlist
                
    
def median(flist):
    ''' return the median of the floats in the given list @flist'''
    flist=newSort(flist)
    n=len(flist)
    if(n%2==0):
       return (flist[int((n-1)/2)]+flist[int(n/2)])/2
    else:
       return flist[int(n/2)]
   
def main():
   f = open("numbers.txt", "r")
   content=str(f.read())
   print(content)
   f.close()
   flist = string_to_list(content)
   if(flist != 'None'):  
       avg=round(mean(flist),2)
       md=round(median(flist),2)
       sdf=round(sd(flist),2)
       cont="mean: "+str(avg)+"\n"+"standard deviation: "+str(sdf)+"\n"+"median: "+str(md)
   else:
       cont='illegal input'
   
   f = open("stats.txt", "w")
   f.write(cont)
   f.close()
main()