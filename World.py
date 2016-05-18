from Tkinter import *


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
    def __init__(self,id,x,y):
        self.id=id
        self.x=x
        self.y=y
        self.history_path=[]
        self.env=[]

        canvas.create_oval(x - 5, y - 5, x + 5, y + 5, width=1, fill='red')



    def WriteMSGtoFile(s):
        with open('MSG_history'+id+'.txt','a') as file:
            file.write(s+'\n')
    def addPath(self,s):
        self.history_path[self.history_path.size]=s



class Message:
    def __init__(self,s):
        self.stam=s



canvas.bind('<Button-1>',  onMiddleClick)
canvas.pack(expand=YES, fill=BOTH)


tkroot.title('Ex3')
tkroot.mainloop()
