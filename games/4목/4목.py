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
        return self.row

    def getRow(self):
        return self.col

    def clicked(self,event):
        nextcolor = 'red' if self.color != 'red' else 'yellow'
        self.setColor(nextcolor)

    def setColor(self,color):
        self.delete('oval')
        self.color = color
        self.create_oval(4,4,20,20, fill = self.color,tags='oval')

cells = [[Cell(frame1,0,0),Cell(frame1,0,1),Cell(frame1,0,2),Cell(frame1,0,3),Cell(frame1,0,4),Cell(frame1,0,5),Cell(frame1,0,6)],
        [Cell(frame1,1,0),Cell(frame1,1,1),Cell(frame1,1,2),Cell(frame1,1,3),Cell(frame1,1,4),Cell(frame1,1,5),Cell(frame1,1,6)],
        [Cell(frame1,2,0),Cell(frame1,2,1),Cell(frame1,2,2),Cell(frame1,2,3),Cell(frame1,2,4),Cell(frame1,2,5),Cell(frame1,2,6)],
        [Cell(frame1,3,0),Cell(frame1,3,1),Cell(frame1,3,2),Cell(frame1,3,3),Cell(frame1,3,4),Cell(frame1,3,5),Cell(frame1,3,6)],
        [Cell(frame1,4,0),Cell(frame1,4,1),Cell(frame1,4,2),Cell(frame1,4,3),Cell(frame1,4,4),Cell(frame1,4,5),Cell(frame1,4,6)],
        [Cell(frame1,5,0),Cell(frame1,5,1),Cell(frame1,5,2),Cell(frame1,5,3),Cell(frame1,5,4),Cell(frame1,5,5),Cell(frame1,5,6)],
        ]


for r in range(0,6):
    for c in range(0,7):
        cells[r][c].grid(row=cells[r][c].getRow(),column=cells[r][c].getCol())



window.mainloop()

