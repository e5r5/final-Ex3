from Tkinter import *
import random
import time
from math import *
import Robot

#####################################Simulation############################################

##class

robots = []
tkroot = Tk()
root = Tk()
Frame = Frame(root, width=100, height=100)
Frame.pack(expand=YES, fill=BOTH)
Frame.pack(side=TOP)
canvas = Canvas(width=1000, height=750, bg='white')
##

##one run on robots, if step() work like 20,000 time= we finsh the Simulation
def step():
   epsilon_stop_simulation = 10
   epsilonRMS = 10
   for r in robots:
        r.MoveRobot()
        OutFromGray()
        close_to_the_real_dist(r,epsilon_stop_simulation,epsilonRMS,r.oneStepRobot)




def step_until_end():
    ans=0
    Done = False
    while(not Done):
        step()
        ans=ans+1
        if(IsSimulationFinish(robots,10)):
            Done=True
    print "is Done in ",ans," steps !!"



button1 = Button(Frame, text = "Quit", command = canvas.quit)
button2 = Button(Frame, text = "step 1 time", command = step)
button3 = Button(Frame, text = "until Simulation Finish",command=step_until_end)
button1.pack(side=TOP)
button2.pack(side=TOP)
button3.pack(side=TOP)


root.title("control Ex3")
canvas.create_rectangle(100, 100, 200, 200, width=1, fill='black')
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
    if(i<15):
          robots.insert(i,Robot.Robot(i,x,y,canvas,True,robots))##add to array
          robots[i].tempX=x
          robots[i].tempY = y
    else:
          robots.insert(i,Robot.Robot(i,x,y,canvas,False,robots))##add to array



canvas.pack(expand=YES, fill=BOTH)#Show canvas

###if Simulation Finish return true else return false
def IsSimulationFinish(robots,epsilon):
    for r in robots:
        if(not((fabs(r.tempX-r.x)<=epsilon) and (fabs(r.tempY-r.y)<=epsilon) )):
            return False#for evrey robot in robots chek if Finish=only when evrey robot Finish
    return True


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
    return sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))

def TreeToGuess_RealDist(Tree,Xguess,Yguess): #must to be O(1)! return dist!
    #dis=Tree.disForTree[int(Yguess)+1][int(Xguess)+1]
    r=random.uniform(0.8, 1.2)
    return (Get_Oklidi_Dist(Tree.tempX,Tree.tempY,Xguess,Yguess)*r)


#impot: robot, Epsilon stopped the simulation, RMS Epsilon, a few pixels to move each step
# void function that upDate the guess X Y and at the end make the robot to Tree!
def close_to_the_real_dist(robot,epsilon_Stop_Simlashian,epsilonRMS,Onestep):
    Tempx=robot.tempX
    Tempy=robot.tempY
    #while we dont close to epsilon
    TempRms=RMS(Tempx,Tempy,robot.id)
    startRms=TempRms
    if(TempRms>RMS(Tempx,Tempy+Onestep,robot.id)and Robot.isOKtoMOVE(Tempx,Tempy+Onestep,robots)):# move up
       Tempy= Tempy + Onestep
       TempRms=RMS(Tempx,Tempy+Onestep,robot.id)
    elif (TempRms > RMS(Tempx, Tempy - Onestep,robot.id) and Robot.isOKtoMOVE(Tempx, Tempy- Onestep, robots)):  # move Down
       Tempy = Tempy - Onestep
       TempRms = RMS(Tempx, Tempy - Onestep,robot.id)
    elif (TempRms > RMS(Tempx + Onestep, Tempy,robot.id)and Robot.isOKtoMOVE(Tempx + Onestep,Tempy,robots)):  # move R
       Tempx = Tempx + Onestep
       TempRms = RMS(Tempx + Onestep, Tempy,robot.id)
    elif(TempRms>RMS(Tempx-Onestep,Tempy,robot.id)and Robot.isOKtoMOVE(Tempx - Onestep,Tempy,robots)):#movw L
       Tempx = Tempx - Onestep
       TempRms =RMS(Tempx - Onestep, Tempy,robot.id)
    else:#all is not ok! go with anathr step
       robots[robot.id].oneStepRobot=robots[robot.id].oneStepRobot+5
    robots[robot.id].tempY = Tempy
    robots[robot.id].tempX = Tempx

    #if is colse enough updata robot = make tree and tempX tempY
    if((fabs(Tempx-robots[robot.id].x)<=epsilon_Stop_Simlashian) and (fabs(Tempy-robots[robot.id].y)<=epsilon_Stop_Simlashian)and epsilonRMS>TempRms and not robot.isTree):
        i= (int)(robot.id)
        robots[i].tempY = Tempy
        robots[i].tempX = Tempx
        robots.insert(i,Robot.Robot(robot.id, robot.tempX, robot.tempY,canvas,True,robots))
        #print "ok is a tree now : Tempx",Tempx,"Tempy",Tempy
        robots.remove(robot)
       # print "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",robot.id
        return


# the STIA = if is close to zero, the geass close to the real dist
def RMS(xtemp,ytemp,idR):
    sum=0
    nemberOfTree = 0
    for r in robots:
        if(r.isTree):
            nemberOfTree=nemberOfTree+1
            geassToTree =Get_Oklidi_Dist(r.x,r.y,xtemp,ytemp)
            #realDist = TreeToGuess_RealDist(r,xtemp,ytemp)
            realDist = Get_Oklidi_Dist(r.x,r.y,robots[idR].x,robots[idR].y)
            newDist= (realDist-geassToTree  ) * (realDist-geassToTree)
            sum = sum + newDist
    av = sum/nemberOfTree
    return sqrt(av)

def OutFromGray():  #get out from the gray area
    for i in robots:
        if ((i.x >= 330 and i.x <= 600 and i.y >= 330 and i.y <= 500) and i.isTree==False):
            canvas.create_oval(i.x - 7, i.y - 7, i.x + 7, i.y + 7, width=0, fill='gray') #delete robot
            i.y=i.y-20 #go up
            canvas.create_oval(i.x - 5, i.y - 5, i.x + 5, i.y + 5, width=0, fill='red')
            canvas.create_text(i.x,i.y,text=i.id)


canvas.bind('<Button-1>',  onMiddleClick)
canvas.pack(expand=YES, fill=BOTH)
Frame.pack(expand=YES, fill=BOTH)
tkroot.title('Ex3')
tkroot.mainloop()
