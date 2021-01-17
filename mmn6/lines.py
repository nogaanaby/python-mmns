# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 18:55:30 2021

@author: User
"""
import math
import copy

class Point:
    """ a point in the plane """
    def __init__(self, x, y):
        try:
            self.__x = float(x)
            self.__y = float(y)
        except ValueError as e:
            print(e)    

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
            return "y={0:.2f}x+{1:.2f}".format(m,n)
        return "x={0:.2f}".format(self.p.x)
        
def main():
    try:
        p = Point(4.76543,7)
        print(p)
        q = Point(8,7.53333)
        l=Line(p,q)
        print(l)
        #print(l.y_intersect())
    except Exception as e:
        print(e)    
    

main()


"""
def get_inverse_element(lst, index):

    try:
        return 1/int(lst[index])
    except ValueError:
        print("value is not a number")
    except IndexError:
        print("index is not in the list")
    except ZeroDivisionError:
        print("zero has no inverse")
        
strange_list = ['seventeen', '17', '0', 'hello']
print(get_inverse_element(strange_list,0))
print(get_inverse_element(strange_list,2))
print(get_inverse_element(strange_list,4))
print(get_inverse_element(strange_list,1))
"""



    
"""    
    def __init__(self, p, q):
        if(isinstance(p, Point)==False or isinstance(q, Point)==False):
            raise ValueError('The arguments type must be Points')
        if(p==q):
           raise Exception('Please enter two different points')         
        self.__p = copy.deepcopy(p)
        self.__q = copy.deepcopy(q)
"""
