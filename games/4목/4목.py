from tkinter import *

window = Tk()
window.title("Connect Four") #Set title

frame1 = Frame(window)
frame1.pack()

frame2 = Frame(window)
frame2.pack()

statusLabel = ['새로 시작','Red Win', 'Yellow Win']
statusIndex = 0

class Cell(Canvas):
    def __init__(self,parent,col,row,width=20,height=20):
        Canvas.__init__(self,parent,width=width,height=height,\
            bg = "blue", borderwidth=2)
        self.color="white"
        self.row = row
        self.col = col
        self.create_oval(4,4,20,20,fill='white',tags='oval')
        self.bind('<Button-1>',self.clicked)

    def getCol(self):
        return self.col

    def getRow(self):
        return self.row

    def clicked(self,event):
        nextcolor = 'red' if self.color != 'red' else 'yellow'
        self.setColor(nextcolor)

    def setColor(self,color):
        self.delete('oval')
        self.color = color
        self.create_oval(4,4,20,20, fill = self.color,tags='oval')

def Change():
    global statusIndex
    global statusButton
    statusIndex +=1
    if(statusIndex == 3):
        statusIndex = 0
    statusButton["text"] = statusLabel[statusIndex]

cells = [[Cell(frame1,r,c) for c in range(6) ] for r in range(7)]
statusButton = Button(frame2,text=statusLabel[statusIndex], command=Change)
statusButton.pack()





for r in range(0,7):
    for c in range(0,6):
        cells[r][c].grid(row=cells[r][c].getRow(),column=cells[r][c].getCol())



window.mainloop()

