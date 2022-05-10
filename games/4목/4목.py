from tkinter import *

window = Tk()
window.title("Connect Four") #Set title

frame1 = Frame(window)
frame1.pack()

frame2 = Frame(window)
frame2.pack()

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


cells = [[Cell(frame1,r,c) for c in range(7) ] for r in range(6)]


for r in range(0,6):
    for c in range(0,7):
        cells[r][c].grid(row=cells[r][c].getRow(),column=cells[r][c].getCol())



window.mainloop()

