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
        global i
        if self.token == ' ':
            i += 1
            self.token = Token[1 + i % 2]
            if i == 9:
                print("비겼습니다. 게임 종료")
            print(currentToken[2 - i % 2],"차례")

            self["image"] = images[self.token]

        if isWin(currentToken[1 + i%2]):
            print(currentToken[1 + i%2],"승리!!!!!")

def isWin(mark): # 돌 3개가 같게 됐는지 검사하는 조건. 같으면 True 반환
    return (cells[0][0].getToken() + cells[0][1].getToken() + cells[0][2].getToken() == mark * 3) or \
           (cells[1][0].getToken() + cells[1][1].getToken() + cells[1][2].getToken() == mark * 3) or \
           (cells[2][0].getToken() + cells[2][1].getToken() + cells[2][2].getToken() == mark * 3) or \
           (cells[0][0].getToken() + cells[1][0].getToken() + cells[2][0].getToken() == mark * 3) or \
           (cells[0][1].getToken() + cells[1][1].getToken() + cells[2][1].getToken() == mark * 3) or \
           (cells[0][2].getToken() + cells[1][2].getToken() + cells[2][2].getToken() == mark * 3) or \
           (cells[0][0].getToken() + cells[1][1].getToken() + cells[2][2].getToken() == mark * 3) or \
           (cells[2][0].getToken() + cells[1][1].getToken() + cells[0][2].getToken() == mark * 3)

i = 0                           # 돌을 놓은 횟수. 초기값 0
Token = [' ', 'O', 'X']         # 돌 상태값
currentToken = [' ', 'O', 'X']  # 다음 놓을 차례
cells = [[Cell(),Cell(),Cell()],
        [Cell(),Cell(),Cell()],
        [Cell(),Cell(),Cell()]]

statusLabel = ['Playing game', 'O차례', 'X차례', '비겼습니다. 게임종료', 'X Win!!!', 'O Win!!!']
index = 0     # statusLabel의 초기값 : Playing Game

for r in range(0, 3):
    for c in range(0, 3):
        cells[r][c].bind("<Button-1>", cells[r][c].flip)

def printText(index):
    frameResult = Frame(tic_tac_toe, background='#00ff00')
    frameResult.pack(side='bottom', fill='x')
    resultFont = font.Font(tic_tac_toe, size=10, weight='bold', family='바탕체')
    resultText = Label(frameResult, text=statusLabel[index], font=resultFont)
    resultText.pack(anchor='center', fill='both')

def initScreen():
    for r in range(0, 3):
        for c in range(0, 3):
            cells[r][c].place(x=r * 45, y=c * 45)
    printText(index) #아래 주석 부분을 따로 printText 함수로 구현하는 것으로 수정한 상태. (개선 필요)
    # frameResult = Frame(tic_tac_toe, background='#00ff00')
    # frameResult.pack(side='bottom', fill='x')
    # resultFont = font.Font(tic_tac_toe, size=10, weight='bold', family='바탕체')
    # resultText = Label(frameResult, text=statusLabel[index], font=resultFont)
    # resultText.pack(anchor='center', fill='both')

initScreen()
tic_tac_toe.mainloop()