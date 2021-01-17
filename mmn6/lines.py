# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:55:30 2021

@author: User
"""
class Point:
    """ a point in the plane """
    def __init__(self, x, y):
        try:
            self.__x = float(x)       
        except ValueError:
            raise ValueError("x coordinate must be a number")
        try:
            self.__y = float(y)       
        except ValueError:
            raise ValueError("y coordinate must be a number")

    def __str__(self):
        return "({0:.2f},{1:.2f})".format(self.x,self.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    """ all the attributes builders """
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        try:
            self.__x = float(value)
        except ValueError as e:
            print(e)
        
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        try:
            self.__y = float(value)
        except ValueError as e:
            print(e)
            
class Line:
    """ a line in the plane """
    def __init__(self, p, q):
        try:
            if(p==q):
                raise Exception('Please enter two different points')
            if(isinstance(p, Point)==False or isinstance(q, Point)==False):
                raise ValueError('The arguments type must be Points')
            else:
                self.__p = Point(p.x,p.y)
                self.__q = Point(q.x,q.y)
        except ValueError as e:
            print(e)
    
    @property
    def p(self):
        return self.__p
    
    @property
    def q(self):
        return self.__q

    @p.setter
    def p(self, value):
        if(isinstance(value, Point)==False):
           raise ValueError('The argument type must be Point')
        self.__p = value

            
    @q.setter
    def q(self, value):
        if(isinstance(value, Point)==False):
           raise ValueError('The argument type must be Point')
        self.__q = value

    
    def is_vertical(self):
        if(self.p.y==self.q.y):
            return True
        return False
        
    def slope(self):
        if(self.p.x-self.q.x==0):
            return None
        return round((self.p.y-self.q.y)/(self.p.x-self.q.x),2)
        
    def y_intersect(self):
        m=self.slope()
        if(m!=None):
            n=self.p.y-(m*self.p.x)
            return n
        return None
        
    def __str__(self):
        m=self.slope()
        n=self.y_intersect()
        if(m!=None):
            return "y = {0:.2f}x + {1:.2f}".format(m,n)
        return "x={0:.2f}".format(self.p.x)

    def parallel(self,other):
        if(self.slope()==other.slope()):
            return True
        return False
    
    def equals(self,other):
        if(str(self)==str(other)):
            return True
        return False
    
    def intersection(self,other):
        if(self.parallel(other)):
            return None
        myY=self.y_intersect()
        otherY=other.y_intersect()
        freeNum=otherY-myY
        mySlope=self.slope()
        otherSlope=other.slope()
        xFactor=mySlope-otherSlope
        xValue=round(freeNum/xFactor,2)
        yValue=xValue*mySlope+myY
        return Point(xValue,yValue)
        
        

def ui(filename):
    f=open(filename, "r")
    content=""
    rowNum=1
    #iterates throght every line in the text file to calculate the factorization options
    for row in f:
        try:
            arr=row.split(" ")
            content+=f"line {rowNum}"
            if(len(arr)==4):
                line=Line( Point(arr[0],arr[1]),Point(arr[2],arr[3]) )
                content+=f": {str(line)}\n"
            else:
                raise Exception("Every line must include 4 numbers")
            rowNum+=1
        except ValueError as e:
            content+=f" error: {e}\n"
        except Exception as e:
            content+=f" error: {e}\n"
    f.close()
    print(content)

    
def main():
    ui("input1.txt")
    ui("input4.txt")

main()

'''
piece and love, best regards,
Served under the auspices of 
Noga Banana first of her name
mother of cats and breaker of chains
'''