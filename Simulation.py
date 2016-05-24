from Tkinter import *
import random
import time
from math import *
import Robot

#####################################Simulation############################################

##class

robots = []
tkroot = Tk()
canvas = Canvas(width=1000, height=750, bg='white')
root = Tk()
Frame = Frame(root, width=70, height=70)
Frame.pack(side=TOP)
##

canvas.create_rectangle(100, 100, 200, 200, width=1, fill='black')
#canvas.create_rectangle(100, 400,550 , 500, width=5, fill='gray')
canvas.create_rectangle(300, 600,700 , 700, width=3, fill='black')
canvas.create_rectangle(330, 330,600 , 500, width=2, fill='gray')

##make random robots:
for i in range(0,100):
    random.seed(100-i)
    x=random.random()*1000
    y=random.random()*750
    while ((x>=95 and x<=205 and y>=95 and y<=205)or (x>=295 and x<=705 and y>=595 and y<=705)):
            x = random.random() * 1000
            y = random.random() * 750
    if(i<30):
          robots.insert(i,Robot.Robot(i,x,y,canvas,True))##add to array
    else:
          robots.insert(i,Robot.Robot(i,x,y,canvas,False))##add to array

canvas.pack(expand=YES, fill=BOTH)#Show canvas

###if Simulation Finish return true else return false
def IsSimulationFinish(robots,epsilon):
    for r in robots:
        if(not((fabs(r.tempX-r.x)<=epsilon) and (fabs(r.tempY-r.y)<=epsilon))):
            return False#for evrey robot in robots chek if Finish=only when evrey robot Finish
    return True

##one run on robots, if step() work like 20,000 time= we finsh the Simulation
def step(robots):
         print "hi"

##@@@@@@@like this the progrms look like
 #   while(not IsSimulationFinish(robots,50)):
 #       print "hi"
#        canvas.pack(expand=YES, fill=BOTH)
 ##
 #progeme run here!!!!!!!
 ##
# if we here we Finish!! = print cunt and bay bay to ex3

##two buttons in the Simulation
# button1 = Button(canvas, text = "Quit", command = canvas.quit)
# button1.configure(width = 10)
# button1_window = canvas.create_window(10, 10, window=button1)
# button2 = Button(canvas, text = "next",command = step(robots))
# button2.configure(width = 10)
# button2_window = canvas.create_window(10, 10, window=button2 )


button1 = Button(Frame, text = "Quit", command = canvas.quit)
button2 = Button(Frame, text = "step 1 time" )#command = step(robots,firstTimeStep))
button3 = Button(Frame, text = "step 5000 times")
button1.pack(side=TOP)
button2.pack(side=TOP)
button3.pack(side=TOP)

firstTimeStep=True
########################################GUI######################################
def showPosEvent(event):
    print ' X=%s Y=%s' % ( event.x, event.y)


def onMiddleClick(event):
    showPosEvent(event)



############################################################################################
class MSG:
    def __init__(self, IDmsg, timeMsg, senderID, dataMSG, power, sourceMsg):
        start_time=time.time()
        self.IDmsg=IDmsg
        self.timeMSG=timeMsg
        self.senderID=senderID
        self.dataMSG=dataMSG
        self.power=power
        self.sourceMSG=sourceMsg
        self.counterMSG=1

    def updateMSG(self, timeMSG1, senderID1, dataMSG1, power1):
        self.timeMSG=timeMSG1
        self.senderID=senderID1
        self.dataMSG=dataMSG1
        self.power=power1
        self.counterMSG=self.counterMSG+1


############################## class Simulator:################################################


def swap(a, b, arr):
         t = arr[a]
         arr[a] = arr[b]
         arr[b] = t

def RandomArr(arr):
         for i in range(0, 100):
             swap(i, random.randint(0, 100), arr)

#return the oklidi dist from to point
def Get_Oklidi_Dist(x1,y1,x2,y2):
    return math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def TreeToGuess_RealDist(xTree,yTree,Xguess,Yguess): #must to be O(1)! return dist!
    return 555;

#impot: robot, Epsilon stopped the simulation, RMS Epsilon, a few pixels to move each step
# void function that upDate the guess X Y and at the end make the robot to Tree!
def close_to_the_real_dist(robot,epsilon_Stop_Simlashian,epsilonRMS,Onestep):
    Tempx=robot.tempX
    Tempy=robot.tempY
    #while we dont close to epsilon
    while(RMS(Tempx,Tempy)>epsilonRMS):
        TempRms=RMS(Tempx,Tempy)
        if(TempRms>RMS(Tempx,Tempy+Onestep) and Robot.isOKtoMOVE(Tempx,Tempy)):# move up
            Tempy= Tempy + Onestep
        elif(TempRms>RMS(Tempx,Tempy-Onestep)and Robot.isOKtoMOVE(Tempx,Tempy)):#move Down
            Tempy = Tempy - Onestep
        elif(TempRms>RMS(Tempx+Onestep,Tempy)and Robot.isOKtoMOVE(Tempx,Tempy)):   #move R
            Tempx = Tempx + Onestep
        elif(TempRms>RMS(Tempx-Onestep,Tempy)and Robot.isOKtoMOVE(Tempx,Tempy)):#movw L
            Tempx = Tempx - Onestep
        else:#all is not ok! go with anathr step
            Onestep = Onestep*2
    #if is colse enough updata robot = make tree and tempX tempY
    if(((math.fabs(Tempx-robots[robot.id].tempX)<=epsilon_Stop_Simlashian) and (math.fabs(Tempy-robots[robot.id].tempY)<=epsilon_Stop_Simlashian))):
        robot.isTree=True
        robot.tempY=Tempy
        robot.tempX=Tempx
    else:
        print "Error in function (close_to_the_real_dist) ,the main function, need to fix!   "

# the STIA = if is close to zero, the geass close to the real dist
def RMS(xtemp,ytemp):
    sum=0
    nemberOfTree = 30
    for r in robots:
        if(r.isTree):
            geassToTree =Get_Oklidi_Dist(r.tempY,r.tempY,xtemp,ytemp)
            realDist = TreeToGuess_RealDist(r.tempX,r.tempY,xtemp,ytemp)
            newDist= (geassToTree - realDist) * (geassToTree - realDist)
            sum = sum + newDist
    av = sum/nemberOfTree
    return math.sqrt(av)


canvas.bind('<Button-1>',  onMiddleClick)
canvas.pack(expand=YES, fill=BOTH)


tkroot.title('Ex3')
tkroot.mainloop()
