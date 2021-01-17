"""
Student: Noga Anaby
ID: 318298296
Assignment no. 6
Program: minesweeper.py

This is the mine-sweeper game 
"""

#make all the classes as the conztnsus
#input the board data from the user
#add comments
import random

class MSSquare:
    """ minesweeper square block class """
    def __init__(self, hasMine=False, neighborMines=0):
        self.__has_mine = hasMine
        self.__hidden = True
        self.__neighbor_mines = neighborMines

    """ all the attributes builders """
    @property
    def neighbor_mines(self):
        return self.__neighbor_mines

    @neighbor_mines.setter
    def neighbor_mines(self, value):
        self.__neighbor_mines=value
        
    @property
    def hidden(self):
        return self.__hidden
        
    @hidden.setter
    def hidden(self, value):
        self.__hidden=value
        
    @property
    def has_mine(self):
        return self.__has_mine
        
    @has_mine.setter
    def has_mine(self, value):
        self.__has_mine=value
    
    def print_square(self):
        """ prints the value=num of mines of each class object """
        if(self.__hidden):
            print("   ", end="")
        else:
            if(self.__has_mine):
                print(" X ", end="")
            else:
                print(" "+str(self.__neighbor_mines)+" ", end="")



class MSBoard:
    """ This class represents a board object """
    def __init__(self, boardWidth=6,numOfMines=4):
        self.__board_width = boardWidth
        self.__num_of_mines = numOfMines
        self.__board_data=[[MSSquare() for x in range(0,boardWidth)]  for y in range(0,boardWidth)]
        
        for i in range(0,self.__num_of_mines):
            self.spred_mine()
        
        self.initialize_board()

    @property
    def board_width(self):
        return self.__board_width

    @board_width.setter
    def board_width(self, value):
        self.__board_width=value
        
    @property
    def num_of_mines(self):
        return self.__num_of_mines
        
    @num_of_mines.setter
    def num_of_mines(self, value):
        self.__num_of_mines=value

    @property
    def board_data(self):
        return self.__board_data

    
    def spred_mine(self):
       """ Spred the mine randomly """
       mineX= random.randint(0, self.board_width-1)
       mineY= random.randint(0, self.board_width-1)
       
       if(self.board_data[mineX][mineY].has_mine==True):
           self.spred_mine()
       else:
           self.board_data[mineX][mineY].has_mine=True;
  
    
    def initialize_board(self):
        """ Go all over the board and set the right value to each square """
        #self.print_board()
        for x in range(0,len(self.board_data)):
            for y in range(0,len(self.board_data[0])):
                if(self.board_data[x][y].has_mine):
                    self.set_neighbors(x,y)

    def set_neighbors(self,x,y):
        """ If a particular square has a mine, it informes all of its neighbors to increase their value by 1 """
        self.set_square_num(x,y-1)
        self.set_square_num(x,y+1)
        self.set_square_num(x-1,y-1)
        self.set_square_num(x+1,y-1)
        self.set_square_num(x-1,y+1)
        self.set_square_num(x+1,y+1)
        self.set_square_num(x-1,y)
        self.set_square_num(x+1,y)
    
    def set_square_num(self,x,y):
        """ Set the value of num of mine neighbors """
        if(x==self.board_width or y==self.board_width or 
           x<0 or y<0 or self.board_data[x][y].has_mine):
            return
        else:
            self.board_data[x][y].neighbor_mines+=1
            #self.print_board()
    
    
    def print_board(self):
        print(" +"+"---+"*self.board_width)
        for row in self.board_data:
            print(f"{self.board_data.index(row)+1}|", end="")
            for col in row:
                col.print_square()
                print("|",end="")
            print("\n +"+"---+"*self.board_width)
        
        print(" ",end="")
        for i in range(1,self.board_width+1): print(f"  {i} ",end="")
        print("\n")
        
    def expose_all_mines(self):
        """ Exposes all the mines in case the player loses"""
        for row in self.board_data:
            for col in row:
                if(col.has_mine):
                    col.hidden=False
    
    def expose_square(self,x,y):
        """ This function decides which and how many squares to expose after the player move, 
        return the number of exposed squares to know when\if the player won 
        without going all over the board each turn """
        count_exposed_squares=0
        if(self.board_data[x][y].has_mine):
            self.expose_all_mines()
            return 0
        elif(self.board_data[x][y].hidden==False):
            return 0
        elif(self.board_data[x][y].neighbor_mines!=0):
            self.board_data[x][y].hidden=False
            count_exposed_squares+=1
            return count_exposed_squares
        else:
            count_exposed_squares+=self.expose_zeroes(x,y)
            return count_exposed_squares
    
    def expose_zeroes(self,x,y):
        """ In case the player hit a square with 0 neighbor mines, 
        I expose all the neighbor 0 squers that linked to the chosen square
        return the number of exposed squares to know when\if the player won 
        without going all over the board each turn """
        count_exposed_squares=0
        if(x==self.board_width or y==self.board_width
            or x<0 or y<0 or self.board_data[x][y].has_mine or self.board_data[x][y].hidden==False):
            return count_exposed_squares
        elif(self.board_data[x][y].neighbor_mines!=0):
            self.board_data[x][y].hidden=False
            count_exposed_squares+=1
            return count_exposed_squares
        else:
            self.board_data[x][y].hidden=False
            count_exposed_squares+=1
            count_exposed_squares+=self.expose_zeroes(x+1,y)
            count_exposed_squares+=self.expose_zeroes(x+1,y-1)
            count_exposed_squares+=self.expose_zeroes(x+1,y+1)
            count_exposed_squares+=self.expose_zeroes(x-1,y)
            count_exposed_squares+=self.expose_zeroes(x-1,y-1)
            count_exposed_squares+=self.expose_zeroes(x-1,y+1)
            count_exposed_squares+=self.expose_zeroes(x,y-1)
            count_exposed_squares+=self.expose_zeroes(x,y+1)
            return count_exposed_squares
            


def main():
    size=int(input("Enter size: "))
    numOfMines=int(input("Enter number of mines (no more than twice the size): "))
    
    if(size<4 or size>9): 
        print("Dimentions does not match the required range")
        return
    if(numOfMines>2*size or numOfMines<1):
        print("Number of mines does not match the required range")
        return
    
    board=MSBoard(size,numOfMines)
    board.print_board()
    count_exposed_squares=0
    
    while(True):
       if(count_exposed_squares == board.board_width*board.board_width-board.num_of_mines):
           print("you won!")
           return
       
       choice=input("Enter your choice with space(row column): ")
       choice=choice.split()
       row=int(choice[0])-1
       col=int(choice[-1])-1
       if(row>=board.board_width or col>=board.board_width):
           print("invalid choise, you shold choose row and col between 1 to "+str(board.board_width)+". please choose again")
           continue
       
       count_exposed_squares+=board.expose_square(row,col)
       board.print_board()
       
       if(board.board_data[row][col].has_mine):
           print("you lost")
           return
          
        
    
main()
