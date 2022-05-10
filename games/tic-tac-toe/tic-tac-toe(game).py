from tkinter import *
from tkinter import font

tic_tac_toe = Tk()
tic_tac_toe.geometry("130x150")

images = {' ': PhotoImage(file='empty.gif'), 'O': PhotoImage(file='o.gif'),
          'X': PhotoImage(file='x.gif')}  # images dictionary 안에 이미지 3개 empty, o, x

class Cell(Label):
    token = ' '
    def __init__(self):
        self.token = ' '
        Label.__init__(self, image=images[self.token])

    def getToken(self):
        return self.token

    def flip(self, event):
        global game_finished
        global resultText
        global index
        global i
        if game_finished:
            return
        else:
            if self.token == ' ':
                i += 1
                index = 1 + i % 2
                self.token = Token[index]
                resultText["text"] = statusLabel[index]
                if i == 9:
                    resultText["text"] = statusLabel[3]
                    game_finished = True
                self["image"] = images[self.token]

            if isWin(currentToken[index]):
                resultText["text"] = statusLabel[4+(i%2)]
                game_finished = True
                return 0

def isWin(mark): # 돌 3개가 같게 됐는지 검사하는 조건. 같으면 True 반환
    return (cells[0][0].getToken() + cells[0][1].getToken() + cells[0][2].getToken() == mark * 3) or \
           (cells[1][0].getToken() + cells[1][1].getToken() + cells[1][2].getToken() == mark * 3) or \
           (cells[2][0].getToken() + cells[2][1].getToken() + cells[2][2].getToken() == mark * 3) or \
           (cells[0][0].getToken() + cells[1][0].getToken() + cells[2][0].getToken() == mark * 3) or \
           (cells[0][1].getToken() + cells[1][1].getToken() + cells[2][1].getToken() == mark * 3) or \
           (cells[0][2].getToken() + cells[1][2].getToken() + cells[2][2].getToken() == mark * 3) or \
           (cells[0][0].getToken() + cells[1][1].getToken() + cells[2][2].getToken() == mark * 3) or \
           (cells[2][0].getToken() + cells[1][1].getToken() + cells[0][2].getToken() == mark * 3)

game_finished = False           # 게임이 끝났는지 알려주는 bool변수
i = 0                           # 돌을 놓은 횟수. 초기값 0
Token = [' ', 'O', 'X']         # 돌 상태값
currentToken = [' ', 'O', 'X']  # 다음 놓을 차례
cells = [[Cell(),Cell(),Cell()],
        [Cell(),Cell(),Cell()],
        [Cell(),Cell(),Cell()]]

statusLabel = [' ','X차례', 'O차례', '비겼습니다. 게임종료', 'O Win!!!', 'X Win!!!']
index = 1     # statusLabel의 인덱스

for r in range(0, 3):
    for c in range(0, 3):
        cells[r][c].bind("<Button-1>", cells[r][c].flip)

#수정할 수 있도록 global 변수로 빼둠
resultFont = font.Font(tic_tac_toe, size=8, weight='bold', family='바탕체')
frameResult = Frame(tic_tac_toe, background='#00ff00')
resultText = Label(frameResult, text=statusLabel[index], font=resultFont)

def printText(index):
    global resultText
    global frameResult
    global resultFont
    frameResult = Frame(tic_tac_toe, background='#00ff00')
    frameResult.pack(side='bottom', fill='x')   
    resultText = Label(frameResult, text=statusLabel[index], font=resultFont)
    resultText.pack(anchor='center', fill='both')

def initScreen():
    for r in range(0, 3):
        for c in range(0, 3):
            cells[r][c].place(x=r * 45, y=c * 45)
    printText(index)

initScreen()   
tic_tac_toe.mainloop()
