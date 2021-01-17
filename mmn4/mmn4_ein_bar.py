"""
Student: Ein-Bar Surie
ID: 316011683
Assignment no. 4
Program: grades.py
"""

def get_students(fileName):
    '''return a students dictionary sorted by id keys '''
    students={}
    s = open(fileName, "r")
    #iterate throught every line, split the data into a list 
    for c in s:
      ls=c.split()
      if(len(ls)<2):
          raise Exception('There is an invalid id')
      students[int(ls[0])]=' '.join(ls[1::])
    return students

def get_grades(fileName):
    '''return a grades dictionary sorted by id keys'''      
    #{31829829: [39,90,80]}
    grades = {}
    g = open(fileName, 'r')
    for line in g:
        ls=line.split(' ')
        student_id=int(ls[0])
        grades[student_id] = [int(ls[i]) for i in range(1,len(ls)) if ls[i].isnumeric()]

    return grades

def valid_id(dict):
    for Id in dict.keys():
        if (len(Id)!= 9) or not str(Id).isnumeric:
            raise Exception ('There is an invalid id')

def merge_dict(dict_A, dict_B):
    merge_dict = {}
    for A in dict_A.keys():
        for B in dict_B.keys():
            if A == B:
                {dict_A[A]:dict_B[B] for k,v in merge_dict}
    return merge_dict

def avarege_grades(fileName):
    grades = open('grades.txt', 'r')
    for line in grades:
        line_ls = line.splite()
        gradesOfStudents = line_ls[1::]
    sum_grades = 0
    for grade in gradesOfStudents:
        sum_grades += int(grade)
    avg_grades = sum_grades / len(gradesOfStudents)
    return avg_grades
    
def main():
    grades = get_grades('grades.txt') 
    students = get_students('students.txt')
    merge =merge_dict(students,grades)
    """
    {
     575656757:{"name": jhon lennon, "average":90},
     698234:{"name": madona, "average":75},
    }
    
    """

main()

    


