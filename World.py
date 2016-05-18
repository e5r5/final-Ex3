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

canvas.bind('<Button-1>',  onMiddleClick)
canvas.pack(expand=YES, fill=BOTH)


tkroot.title('Ex3')
tkroot.mainloop()
