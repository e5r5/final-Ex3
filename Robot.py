from Tkinter import *
import random
import time
from math import *

class Robot:
    x = 0
    y = 0
    id = 0
    battery = 70
    IsWhite = None
    tempX=0
    tempY=0
    disForTree= None
    canvas = None
    robot=[]
    def __init__(self, id, x, y,canvas,isTree,robots):
        start_time = time.time()
        self.id = id
        self.x = x
        self.y = y
        self.isTree=isTree
        start_time = time.time()
        self.history_path = []
        self.env = []
        self.canvas=canvas
        self.robots=robots
        if(isTree):
             canvas.create_oval(x - 5, y - 5, x + 5, y + 5, width=0,fill='green')
             canvas.create_text(x, y, text=id)
        else:
             canvas.create_oval(x - 5, y - 5, x + 5, y + 5, width=0,fill='red')
             canvas.create_text(x, y, text=id)


        if ((x >= 330 and x <= 600 and y >= 330 and y <= 500)):
            self.IsWhite = False
        else:
            self.IsWhite = True

        #built for tree matrix for distance to another robots
        if(isTree):
            x1= int(x) +1
            y1= int(y) +1
            w, h = 750,1000
            # built the matrix with limit
            self.disForTree= [[-1 for i in range(w + 2)] for j in range(h + 2)]
            for j in range(0, w + 2, 1):
                for i in range(0, h + 2, 1):
                    self.disForTree[0][j] = -5
                    self.disForTree[h + 1][j] = -5
                    self.disForTree[i][0] = -5
                    self.disForTree[i][w + 1] = -5
                    if ((j >= 100 + 1 and j <= 200 + 1 and i >= 100 + 1 and i <= 200 + 1) or (
                                            j >= 300 + 1 and j <= 700 + 1 and i >= 600 + 1 and i <= 700 + 1)):
                        self.disForTree[i][j] = -5
            self.disForTree[x1][y1] = 0
            arr = [x1, y1]
            start = 0
            end = 1
            # calculation the distance
            while (start < end):

                x1 = arr[start]
                y1 = arr[start + 1]
                start = start + 2
                if (self.disForTree[x1 + 1][y1] == -1):
                    self.disForTree[x1 + 1][y1] = self.disForTree[x1][y1] + 1
                    arr.append(x1 + 1)
                    arr.append(y1)
                    end = end + 2
                if (self.disForTree[x1 - 1][y1] == -1):
                    self.disForTree[x1 - 1][y1] = self.disForTree[x1][y1] + 1
                    arr.append(x1 - 1)
                    arr.append(y1)
                    end = end + 2
                if (self.disForTree[x1][y1 + 1] == -1):
                    self.disForTree[x1][y1 + 1] = self.disForTree[x1][y1] + 1
                    arr.append(x1)
                    arr.append(y1 + 1)
                    end = end + 2
                if (self.disForTree[x1][y1 - 1] == -1):
                    self.disForTree[x1][y1 - 1] = self.disForTree[x1][y1] + 1
                    arr.append(x1)
                    arr.append(y1 - 1)
                    end = end + 2




    def isOKtoMOVE(self,tempX, tempY):
        if (tempX > 1000 or tempX < 0):  # if its not in the limit of the canvas
            return False

        if (tempY > 750 or tempY < 0):
            return False
        elif ((tempX >= 95 and tempX <= 205 and tempY >= 95 and tempY <= 205) or (
                                tempX >= 295 and tempX <= 705 and tempY >= 595 and tempY <= 705)):  # if its in a black area
            return False
        for i in self.robots:
            if (i.x-5<tempX and i.x+5>tempX and i.y-5<tempY and i.y+5>tempY):
                return False
        else:
            return True

    def control_battery(self):
        if (self.IsWhite and self.battery < 100):
            self.battery = self.battery + 1
        elif ((not self.IsWhite) and self.battery > 0):
            self.battery = self.battery - 1

    def MoveRobot(self):
        if (self.isTree):
            self.canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, width=0, fill='green')
            self.canvas.create_text(self.x, self.y, text=self.id)
            return

        if (self.x >= 330 and self.x <= 600 and self.y >= 330 and self.y <= 500):  # delete the old robot
            self.canvas.create_oval(self.x - 7, self.y - 7, self.x + 7, self.y + 7, width=0, fill='gray')
        else:
            self.canvas.create_oval(self.x - 7, self.y - 7, self.x + 7, self.y + 7, width=0, fill='white')

        # find a new x, y for the robot
        while (True):
            #print 'hi'
            MoveTo = random.random()
            if (MoveTo < 0.25):  # move right
                tempX = self.x + 10
                tempY = self.y
            elif (MoveTo < 0.50):  # move left
                tempX = self.x - 10
                tempY = self.y
            elif (MoveTo < 0.75):  # move up
                tempY = self.y + 10
                tempX = self.x
            else:  # move down
                tempY = self.y - 10
                tempX = self.x

            if (self.isOKtoMOVE(tempX,tempY)==True):  # if the point is in good area- break while
                self.x = tempX
                self.y = tempY
                break

        self.canvas.create_oval(self.x - 5, self.y - 5, self.x + 5, self.y + 5, width=0,fill='red')  # create a robot in the new x,y
        self.canvas.create_text(self.x,self.y,text=self.id)

        self.control_battery


    def WriteMSGtoFile(s):
        with open('MSG_history'+id+'.txt','a') as file:
            file.write(s+'\n')
    def addPath(self,s):
        self.history_path[self.history_path.size]=s

