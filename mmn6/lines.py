# -*- coding: utf-8 -*-
"""
Student: Noga Anaby
ID: 318298296
Assignment no. 6
Program: line.py

This program is a linear functions calculator
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
        """ returns true if the line is verical and false otherwize """
        if(self.p.x==self.q.x):
            return True
        return False
        
    def slope(self):
        """ returns the line slope """
        if(self.p.x-self.q.x==0):
            return None
        return (self.p.y-self.q.y)/(self.p.x-self.q.x)
        
    def y_intersect(self):
        """ returns the line y intersection """
        m=self.slope()
        if(m!=None):
            n=self.p.y-(m*self.p.x)
            return n
        return None
        
    def __str__(self):
        """ returns the line equivelent as string """
        m=self.slope()
        n=self.y_intersect()
        if(m!=None):
            return "y = {0:.2f}x + {1:.2f}".format(m,n)
        return "x = {0:.2f}".format(self.p.x)

    def parallel(self,other):
        """ returns true if this line is parallel to the line given in the parameter and false otherwize """
        if(self.slope()==other.slope()):
            return True
        return False
    
    def equals(self,other):
        """ returns true if this line is equal to the line given in the parameter and false otherwize """
        if(other.slope()==self.slope() and self.y_intersect()==other.y_intersect()):
            return True
        return False
    
    def intersection(self,other):
        """ returns the intersection point between this line and the line given in the parameter"""        
        if(self.parallel(other)):
            return None
        
        myY=self.y_intersect()
        otherY=other.y_intersect()
        mySlope=self.slope()
        otherSlope=other.slope()
        if(myY and otherY):
            freeNum=otherY-myY
            xFactor=mySlope-otherSlope
            xValue=freeNum/xFactor
            yValue=xValue*mySlope+myY
        elif(self.is_vertical()):
            xValue=self.p.x
            yValue=xValue*otherSlope+otherY
        else:
            xValue=other.p.x
            yValue=xValue*mySlope+myY
        return Point(xValue,yValue)
            
        
def main():
    f=open("input.txt", "r")
    content=""
    rowNum=1
    linesArr=[]
    #iterates throght every row in the text file
    for row in f:
        try:
            row=row.strip()
            arr=row.split(" ")
            if(len(arr)==4):
                line=Line( Point(arr[0],arr[1]),Point(arr[2],arr[3]) )
                content+=f"line {rowNum}: {str(line)}\n"
                #iterates throght every line that where calculated before this row
                for l in linesArr:
                   intersection=line.intersection(l["line"])
                   otherLineNum=l["lineNum"]
                   content+=f"line {rowNum} "
                   if(intersection):
                       content+=f"with line {otherLineNum}: {intersection}\n"
                   elif( line.equals(l["line"]) ):
                       content+=f"is equal to line {otherLineNum}\n"
                   else:
                      content+=f"is parallel to line {otherLineNum}\n"
                      
                lineDic={"lineNum":rowNum,"line":line}
                linesArr.append(lineDic)
                
            else:
                raise Exception(f"Not enough data for line {rowNum}.")
        except ValueError as e:
            content+=f"Line {rowNum} error: {e}\n"
        except Exception as e:
            content+=f"{e}\n"
        content+="\n"
        rowNum+=1
    f.close()
    
    o = open("output.txt", "w")
    o.write(content)
    o.close()
    

main()

'''
piece and love, best regards,
Served under the auspices of 
Noga Banana first of her name
mother of cats and breaker of chains
'''