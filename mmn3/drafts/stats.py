# -*- coding: utf-8 -*-
"""
Student: Noga Anaby
ID: 318298296
Assignment no. 3
Program: stats.py

comment: I know that you have beet tring to teach neasted loops, 
but I feel in most of the cases - the best practice might be to avoid it where you can
since it is not clean and afficiant solotion when you have the choise not to use neasted loops.

"""

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

def tester(st):
    print(st)
    print(isfloat(st))
    print("")
    
def main():
   print("all of those should be true: ")
   tester("0.123")
   tester("-0.123")
   tester("+0.123")
   tester("-4.01")
   tester("+3.05")
   tester("3.00")
   tester("+0")
   tester("-0")
   print("all of those should be false: ")
   tester(".123")
   tester("+.5")
   tester("54.6.7")
   tester("+123+5")
   tester("45.")
   tester("00.123")
   tester("001234")
   tester("123a4")
  #isfloat("+3.05")+isfloat("3.00")+isfloat("+0")+isfloat("-0"))
   #print("all of those should be false: ")
   #print(isfloat(".123")+isfloat("+.5")+isfloat("54.6.7")+isfloat("+123+5")+isfloat("45.")+isfloat("00.123")+isfloat("001234")+isfloat("123a4"))
''' 
  yourFloat = input("try me beach: ")
   if(isfloat(yourFloat)):
       print("ok")
   else:
       print("ha ha gut`ya")
  '''
    
main()