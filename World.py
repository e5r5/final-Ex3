from Tkinter import *
import random
import time
def showPosEvent(event):
    print ' X=%s Y=%s' % ( event.x, event.y)


def onMiddleClick(event):
    showPosEvent(event)

###main

tkroot = Tk()
#labelfont = ('courier', 10, 'bold')

canvas = Canvas(width=1000, height=750, bg='white')


canvas.create_rectangle(100, 100, 200, 200, width=1, fill='black')
#canvas.create_rectangle(100, 400,550 , 500, width=5, fill='gray')
canvas.create_rectangle(300, 600,700 , 700, width=3, fill='black')
canvas.create_rectangle(330, 330,600 , 500, width=2, fill='gray')
button1 = Button(canvas, text = "Quit", command = canvas.quit)
button1.configure(width = 10)
button1_window = canvas.create_window(10, 10, window=button1)
#button2 = Button(canvas, text = "next", command = simolator.next)
#button2.configure(width = 10)
#button2_window = canvas.create_window(10, 10, window=button2)


class Robot:
    x=0
    y=0
    id=0
    def __init__(self,id,x,y):
        start_time=time.time()
        self.id=id
        self.x=x
        self.y=y
        start_time=time.time()
        self.history_path=[]
        self.env=[]

        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, width=1, fill='red')


    def WriteMSGtoFile(s):
        with open('MSG_history'+id+'.txt','a') as file:
            file.write(s+'\n')
    def addPath(self,s):
        self.history_path[self.history_path.size]=s

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


class Simulator:
    robots = []
    def __init__(self):
        start_time=time.time()
        for i in range(0,100):
            x=random.random()*1000
            y=random.random()*750
            while ((x>=95 and x<=205 and y>=95 and y<=205)or (x>=295 and x<=705 and y>=595 and y<=705)):
                x = random.random() * 1000
                y = random.random() * 750
            self.robots.insert(i,Robot(i,x,y))
        self.robots.insert(0,Robot(0,230,110))

    def MoveRobot( self,i, x, y):
        r = Simulator.robots.pop(i)
        if (r.x >= 330 and r.x <= 600 and r.y >= 330 and r.y <= 500):
            canvas.create_oval(r.x - 5, r.y - 5, r.x + 5, r.y + 5, width=0, fill='gray')
        else:
            canvas.create_oval(r.x - 5, r.y - 5, r.x + 5, r.y + 5, width=0, fill='white')

        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, width=1, fill='red')
        Simulator.robots.insert(i, Robot(i, x, y))




def swap(a, b, arr):
         t = arr[a]
         arr[a] = arr[b]
         arr[b] = t

def RandomArr(arr):
         for i in range(0, 100):
             swap(i, random.randint(0, 100), arr)

s = Simulator()


canvas.bind('<Button-1>',  onMiddleClick)
canvas.pack(expand=YES, fill=BOTH)


tkroot.title('Ex3')
tkroot.mainloop()
