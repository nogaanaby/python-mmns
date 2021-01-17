# -*- coding: utf-8 -*-
"""
Student: Noga Anaby
ID: 318298296
Assignment no. 3
Program: stats.py

comment: I know that you have beet tring to teach neasted loops, 
but I feel in most of the cases - the best practice might be to avoid it where you can
since it is not clean and afficiant solotion when you have the choise not to use neasted loops.


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
    totalPoints=0
    i=0
    if st[0]=="+" or st[0]=="-":
        i+=1
    if i!=len(st)-1 and st[i]=="0":
        i+=1
        if i!=len(st)-1 and st[i]!=".":
            return False
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

def list_to_string(st):
    strList = st.split()
    floatList=[]
    for x in strList:
        if(isfloat(x)!=True):
            return "None"
        else:
            #left a comment above#
            floatList.append(float(x))
    return floatList   

def mean(flist):
   average=sum(flist) / len(flist) 
   return average

def sd(flist):
    avg=mean(flist)
    flistSum=0
    for x in flist:
      flistSum+=pow(x-avg,2) 
    return math.sqrt( (1/len(flist))*flistSum )
    
def newSort(flist):
    newFlist=flist.copy()
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
    flist=newSort(flist)
    n=len(flist)
    if(n%2==0):
       return (flist[int((n-1)/2)]+flist[int(n/2)])/2
    else:
       return flist[int(n/2)]
   
def main():
   yourStr = input("type a float str ")
   flist = list_to_string(yourStr)
   #avg=mean(flist)
   std=median(flist)
   
   print(newSort(flist))
   print(std)

    
main()