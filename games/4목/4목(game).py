from tkinter import *

window = Tk() #Create a window
window.title("Connect Four")  # Set title

frame1 = Frame(window)
frame1.pack()

frame2 = Frame(window)
frame2.pack()

class Cell(Canvas):
    def __init__(self, parent, col, row, width=20, height=20):
        Canvas.__init__(self, parent, width=width, height=height,\
                        bg="blue", borderwidth=2)
        self.color = 'white'
        self.row = row
        self.col = col
        self.create_oval(4, 4, 20, 20, fill='white', tags='oval')
        self.bind('<Button-1>', self.clicked)

    def getCol(self):
        return self.col

    def getRow(self):
        return self.row

    def getColor(self):
        return self.color

    def clicked(self, event):
        # nextcolor = 'red' if self.color != 'red' else 'yellow'
        # self.setColor(nextcolor)
        global TurnIndex
        global Turn
        global statusLabel
        global cells

        if TurnIndex == 42: #돌이 다 차서 종료
            Change(2)
            return
        else:
            TurnIndex += 1
            cells[getPossibleRow(self.col)][self.col].setColor(Turn[TurnIndex % 2])
            if isWin(Turn[TurnIndex % 2]):
                Change(1 + TurnIndex % 2)

    def setColor(self, color):
        self.delete('oval')
        self.color = color
        self.create_oval(4, 4, 20, 20, fill=self.color, tags='oval')


#돌이 들어갈 수 있는 열 반환
def getPossibleRow(column_index):
    for row_index in range(5,-1,-1):
        if cells[row_index][column_index].getColor() == 'white':
            return row_index

def isWin(color):
    #수평
    for row_index in range(6):
        for column_index in range(7 - 3):
            if cells[row_index][column_index].getColor() == color and cells[row_index][column_index + 1].getColor() == color and \
                    cells[row_index][column_index + 2].getColor() == color and cells[row_index][column_index + 3].getColor() == color:
                return True
    #수직
    for row_index in range(6 - 3):
        for column_index in range(7):
            if cells[row_index][column_index].getColor() == color and cells[row_index + 1][column_index].getColor() == color and \
                    cells[row_index + 2][column_index].getColor() == color and cells[row_index + 3][column_index].getColor() == color:
                return True
    #대각선 /
    for row_index in range(6 - 3):
        for column_index in range(7 - 3):
            if cells[row_index][column_index].getColor() == color and cells[row_index + 1][column_index + 1].getColor() == color and \
                    cells[row_index + 2][column_index + 2].getColor() == color and cells[row_index + 3][column_index + 3].getColor() == color:
                return True
    #대각선 \
    for row_index in range(3, 6):
        for column_index in range(7 - 3):
            if cells[row_index][column_index].getColor() == color and cells[row_index - 1][column_index + 1].getColor() == color and \
                    cells[row_index - 2][column_index + 2].getColor() == color and cells[row_index - 3][column_index + 3].getColor() == color:
                return True


def Change(Index):   # 하단 상태창 수정
    #global statusIndex
    global statusButton
    statusButton["text"] = statusLabel[Index]


def Initialize():   # 새로시작시 모든 값초기화
    global  cells
    global  TurnIndex
    for r in range(6):
        for c in range(7):
            cells[r][c].setColor('white')
    TurnIndex = 1

Turn = ['red', 'yellow', 'None'] #None : 게임 끝일때.
TurnIndex = 1
currentToken = ['white', 'red', 'yellow']         # 돌 상태값
statusLabel = ['새로 시작', 'Red Win', 'Yellow Win']
statusIndex = 0 #아래 버튼의 문구 변경하는 index

cells = [[Cell(frame1, row=r, col=c) for c in range(7)] for r in range(6)]

statusButton = Button(frame2, text=statusLabel[0], command=Change)
statusButton.pack()

for r in range(6):
    for c in range(7):
        cells[r][c].grid(row=cells[r][c].getRow(), column=cells[r][c].getCol())

window.mainloop()

