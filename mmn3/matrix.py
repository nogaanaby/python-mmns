# -*- coding: utf-8 -*-
"""
Student: Noga Anaby
ID: 318298296
Assignment no. 3
Program: matrix.py

This progream is a matrixes calculator
"""


def valid_matrix(mat):
    """ return true if the given matrix is valid and false otherwise """
    cols=len(mat)
    for col in range(1,cols):
        if len(mat[col])!=len(mat[0]):
            return False
    return True

def matrix_scalar_mult(A,C):
    """ multiply the given matrix @A in the given scalar @C  """
    if valid_matrix(A):
        return [[A[i][j]*C for j in range(len(A[0]))] 
              for i in range(len(A))]
    else:
        return "invalid matrix"
    
def add_matrix(A,B):
    """ sum the A matrix with B matrix """
    return [ [A[i][j]+B[i][j] for j in range(len(A[0]))] 
          for i in range(len(A))]

def mult_matrix(A,B):
    """ multiply the A matrix with B matrix """
    return [
        [
         sum([A[i][k]*B[k][j] for k in range(len(A[0]))])
         for j in range(len(B[0]))
        ] 
        for i in range(len(A))
       ] 

def identy_matrix(n):
    """ return identy matrix in nxn dimentions """
    return [[0 if j != i else 1 for j in range(n)] 
            for i in range(n)]

def marix_pow(A,x):
    """ return the given matrix @A in the power of @x"""
    powerMat=A
    #iterate x times and each time multiply the product in A
    for i in range(1,x):
        powerMat=mult_matrix(A,powerMat)
    return powerMat
    
def matrix_polynom(p,A):
    """ return a new matrix based on 
    a summerized calculation of each item (number) in the given 
    list @p, multiply the matrix in the power of the item index in p"""
    dim=len(A)
    polMat=matrix_scalar_mult(identy_matrix(dim),p[0])
    #iterate throght the rest of the p list indexes,
    #summerize the next matrix multiplyed by the value of the current item(number) in p 
    #with the @A matrix in the power of the current item index
    for i in range(1,len(p)):
      polMat=add_matrix(polMat,matrix_scalar_mult(marix_pow(A,i),p[i]))
    return polMat

def print_matrix(A,fileLink):
   '''print the given matrix @A in a pretty wey into the given file address @fileLink'''
   f = open(fileLink, "w")
   content=""
   #iterate throught every row in the matrix, and print it seperatly in a pretty wey
   for row in A:
       row=[round(x,2) for x in row]
       content=str(row).replace("[","").replace("]","").replace(","," ")
       f.write(content+"\n")
   f.close()
    
def main():
    f = open("example_io/matrix_input3.txt", "r")
    line=f.readline()
    matrix=[]
    #iterate throught every non-empty line in the file, 
    #and append every item in the line into the right row in the matrix
    while line != '':
       row=line.split()
       matrix.append([float(x) for x in row])
       line=f.readline()

    p=matrix.pop(len(matrix)-1)
    print_matrix(matrix_polynom(p,matrix),"matrix_output.txt")
    
main()


'''
piece and love, best regards,
Served under the auspices of 
Noga Banana first of her name
mother of cats and breaker of chains
'''