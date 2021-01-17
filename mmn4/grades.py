# -*- coding: utf-8 -*-
"""
Student: Noga Anaby
ID: 318298296
Assignment no. 4
Program: grades.py

This program gives information regarding students and grades
"""

def avg(arr):
    ''' return the average of the numbers in the array '''
    return sum(arr)/len(arr)

def dictionary_bubble_sort(dic):
   ''' sort the dictionary by the average grade each student got '''
   arr2D=[ [k,dic[k][0],dic[k][1] ] for k in dic.keys()]
   n = len(arr2D) 
   # iterate through all array elements and sort 
   for i in range(n): 
       for j in range(0, n-i-1):
           if arr2D[j][2] < arr2D[j+1][2] : 
               arr2D[j], arr2D[j+1] = arr2D[j+1], arr2D[j]
   return arr2D


def inner_join_students_and_grades_by_id(s,g):
    ''' return a dictionary defined by student`s id which has both student`s name and student`s average grade '''
    students=s.copy()
    grades=g.copy()
    joinStudentsNamesAndGrades={}
    #iterate throught both dectionaries and match student`s name and avg grade
    for i in students.keys():
        for j in grades.keys():
            if(i==j):
                gradesArr=grades.pop(j)
                gradeAvg=avg(gradesArr)
                joinStudentsNamesAndGrades[j]=[students[i],gradeAvg]
                break
    return joinStudentsNamesAndGrades

def get_students(filename):
    ''' return a students dictionary from the given file '''
    students={}
    s = open(filename, "r")
    #iterate throught every line, split the data into an array, and if the data is valid, saves the data on the right key
    for x in s:
      arr=x.split()
      if(len(arr)<2):
          raise Exception("Please avoid empty lines, or empty data after Id")
      students[int(arr[0])]=" ".join(arr[1::])
    return students
    
def get_grades(filename):  
    ''' return a grades dictionary from the given file '''
    grades={}
    g = open(filename, "r")
    #iterate throught every line, split the data into an array, and if the data is valid, saves the data on the right key    
    for x in g:
      arr=x.split()
      if(len(arr)<2):
          raise Exception("Please avoid empty lines, or empty data after Id")
      grades[int(arr[0])]=[int(arr[i]) for i in range(1,len(arr))]    
    return grades

def find_most_common_grades(gradesDic):
    ''' return an array of the most common grade '''
    #gradesList has only grades gathered in a list
    gradesList=[g for val in gradesDic.values() for g in val]
    gradesCountDic={}
    countMax=1
    #iterate throught each grade, put it as a key in the dictionary and the value will be the number of time it appeard
    for g in gradesList:
        if g in gradesCountDic:
            gradesCountDic[g]+=1
            if gradesCountDic[g]>countMax:
                countMax=gradesCountDic[g]
        else:
          gradesCountDic[g]=1
    
    mostCommon=[]
    #fined the grades which has the maximum apperance time, save it in an array and return it 
    for g,c in gradesCountDic.items():
        if(c==countMax):
            mostCommon.append(g)
        
    return mostCommon

def get_common_elements(list2D):
    ''' return the grades which more then one student get '''
    newL=[]
    #make each grades list into set to appear only one for each student
    for g in list2D:
        newL.append(set(g))
    
    common=set()
    #go over each student`s grades and search wether they appeard on another students grades 
    for i in range(len(newL)):
       s=newL[i]
       tempArr=newL[::]
       tempArr.pop(i)
       rest=set.union(*tempArr)
       cut=s.intersection(rest)
       common.update(cut)

    return common

def valid_ids(dictionary):
    ''' raise an exception if some id in the given dictionary does not contain nine digits or does not contain only digits '''
    for iD in dictionary.keys():
        if( str(iD).isnumeric()==False or len(str(iD))!= 9 ):
            raise Exception("Id is not valid")

def set_of_keys(dic):
    ''' return a set of keys out of the given dictionary '''
    keys=set()
    for k in dic.keys():
        keys.add(k)
    return keys


def id_appear_in_both_dics(students, grades):
    ''' raise an exception if the two given dictionaries does not contain the same students '''
    if set_of_keys(students)!=set_of_keys(grades):
        raise Exception("Ids does not match")
    
    
def main():
    ''' prints the output, stop the program and raise an error if one or more of the data is not valid '''
    try:
        students=get_students("students.txt")
        grades=get_grades("grades.txt")
        
        #checks
        valid_ids(students)
        valid_ids(grades)
        id_appear_in_both_dics(students,grades)
        
        dictionary=inner_join_students_and_grades_by_id(students,grades)
        sortedArray=dictionary_bubble_sort(dictionary)
        #prints every student and his\hers grade
        for s in sortedArray:
            print(s[1], round(s[2],2))
        
        print("Most common grades: ", find_most_common_grades(grades))
        gradesArr=[g for g in grades.values()]
        common=get_common_elements(gradesArr)
        print("Grades that more than one student got: ", str(common).replace('{','').replace('}',''))
    except OSError as err:
        print(err)
        
main()

'''
best regards,
Served under the auspices of 
Noga Banana first of her name
hope you enjoyd my code, thank you for waching
please don`t forget to subscribe if you liked my content
see you soon next week
'''























