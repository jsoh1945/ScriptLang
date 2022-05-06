
from tkinter import *
from tkinter import font

tic_tac_toe = Tk()
tic_tac_toe.geometry("130x150")

images = {' ': PhotoImage(file='empty.gif'), 'o': PhotoImage(file='o.gif'), 'x':PhotoImage(file='x.gif')} #images dictionary 안에 이미지 3개 empty, o, x

class Cell(Label):
    token = ' '
    def __init__(self):
        self.token = ' '
        Label.__init__(self, image = images[self.token])
        

    def getToken(self):
        return self.token
    
    def getTokenimage(self):
        return self.token


    def onClick(self):
        if self.token == ' ':
            self.token = 'O'
        elif self.token == 'O':
            self.token = 'X'
        else:
            self.token = ' '

    def flip(self,event):
        pass

    
currentToken = [' ', 'O', 'X'] #다음 놓을 차례
cells = [[Cell(),Cell(),Cell()],
        [Cell(),Cell(),Cell()],
        [Cell(),Cell(),Cell()]]


def initScreen():

    for r in range(0,3):
        for c in range(0,3):
            cells[r][c].place(x=r*45,y=c*45)
    

    frameResult = Frame(tic_tac_toe,background='#00ff00')
    frameResult.pack(side='bottom',fill='x')

    resultFont= font.Font(tic_tac_toe, size=10, weight='bold', family = '바탕체')
    resultText = Label(frameResult, text="Result Text", font=resultFont )
    resultText.pack(anchor='center',fill='both')

    

initScreen()
tic_tac_toe.mainloop()

