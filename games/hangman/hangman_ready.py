import math
from tkinter import * # Import tkinter
import random    

gamefinished = False

class Hangman:
    def __init__(self):
        randint = random.randrange(0,3)
        self.word = words[randint]
        self.stars = ""
        for i in range(0,len(self.word)):
            self.stars += "*"
        self.wrong = ""
        self.wrongCount = 0
        self.radius = 20
        self.draw()
        

    def getWrong(self):
        return self.wrong

    def getWord(self):
        return self.word

    def getStars(self):
        return self.stars

    def draw(self):
        # 한꺼번에 지울 요소들을 "hangman" tag로 묶어뒀다가 일괄 삭제.
        canvas.delete("hangman")

        # 인자 : (x1,y1)=topleft, (x2,y2)=bottomright, start=오른쪽이 0도(반시계방향), extent=start부터 몇도까지인지
        #    style='pieslice'|'chord'|'arc'
        canvas.create_arc(20, 200, 100, 240, start = 0, extent = 180, style='chord', tags = "hangman") # Draw the base
        canvas.create_line(60, 200, 60, 20, tags = "hangman")  # Draw the pole
        canvas.create_line(60, 20, 160, 20, tags = "hangman") # Draw the hanger
        
        
        canvas.create_line(160, 20, 160, 40, tags = "hangman") # Draw the hanger

        ## Draw the circle
        #canvas.create_oval(140, 40, 180, 80, tags = "hangman") # Draw the hanger
        

        canvas.create_text(200,190,text= "단어: "+self.stars,tags='word')
        canvas.create_text(200,210,text="틀린단어: "+self.wrong,tags='word')
        

        

    def changeStar(self,index, c):
        global gamefinished
        if not gamefinished:
            change = self.stars[:index] + c + self.stars[index+1:]
            self.stars = change
        
        if '*' not in self.stars:
            canvas.delete("word")
            canvas.create_text(200,190,text="정답: "+self.word, tags='hangman')
            canvas.create_text(200,210,text="You Win! Press Enter to restart", tags='hangman')
            gamefinished =  True


    def changeWrong(self,c):
        if not gamefinished:
            if c in self.wrong:
                pass
            else:
                self.wrong += c
                self.drawWrong()
        else:
            return

        

    def textUpdate(self):
        if gamefinished:
            return
        else:
            canvas.delete("word")
            canvas.create_text(200,190,text= "단어: "+self.stars,tags='word')
            canvas.create_text(200,210,text="틀린단어: "+self.wrong,tags='word')

    def drawWrong(self):
        global gamefinished
        if self.wrongCount == 0:
            canvas.create_oval(140, 40, 180, 80, tags = "hangman")
        elif self.wrongCount == 1:
            # Draw the left arm (중심(160,60)에서 45도 움직인 지점의 x좌표는 cos로, y좌표는 sin으로 얻기)
            x1 = 160 - self.radius * math.cos(math.radians(45))
            y1 = 60 + self.radius * math.sin(math.radians(45))
            x2 = 160 - (self.radius+60) * math.cos(math.radians(45))
            y2 = 60 + (self.radius+60) * math.sin(math.radians(45))
            canvas.create_line(x1, y1, x2, y2, tags = "hangman")  
        elif self.wrongCount == 2:
            x1 = 160 + self.radius * math.cos(math.radians(45))
            y1 = 60 + self.radius * math.sin(math.radians(45))
            x2 = 160 + (self.radius+60) * math.cos(math.radians(45))
            y2 = 60 + (self.radius+60) * math.sin(math.radians(45))
            canvas.create_line(x1, y1, x2, y2, tags = "hangman")
        elif self.wrongCount == 3:
            canvas.create_line(160, 80, 160, 140, tags = "hangman")  # 몸통
        elif self.wrongCount == 4:
            x2 = 160 - (self.radius+60) * math.cos(math.radians(45))
            y2 = 140 + (self.radius+60) * math.sin(math.radians(45))
            canvas.create_line(160, 140, x2, y2, tags = "hangman")
        elif self.wrongCount == 5:
            x2 = 160 + (self.radius+60) * math.cos(math.radians(45))
            y2 = 140 + (self.radius+60) * math.sin(math.radians(45))
            canvas.create_line(160,140, x2, y2, tags = "hangman")
            canvas.delete("word")
            canvas.create_text(200,190,text= "정답: "+self.word,tags='hangman')
            canvas.create_text(200,210,text="게임을 계속 하려면 enter를 누르세요",tags='hangman')
            gamefinished = True
            return
        self.wrongCount += 1
        print(self.wrongCount)

    def restart(self):
        global gamefinished
        gamefinished = False
        canvas.delete('word')
        randint = random.randrange(0,3)
        self.wrongCount = 0
        self.stars = ""
        self.wrong = ""
        self.word = words[randint]
        for i in range(0,len(self.word)):
            self.stars += "*"
        self.draw()
    
# Initialize words, get the words from a file
infile = open("hangman.txt", "r")
words = infile.read().split()
    
window = Tk() # Create a window
window.title("행맨") # Set a title

def processKeyEvent(event):  
    global hangman
    global gamefinished
    answer = list(hangman.getWord())
    print(answer)
    print(hangman.getStars())
    if event.char >= 'a' and event.char <= 'z':
        print(event.char)
        
        if event.char in answer:
            cnt = 0
            for c in answer:
                if c == event.char:
                    hangman.changeStar(cnt,c)
                    print("changeWord called")
                    hangman.textUpdate()
                cnt += 1
        else:
            hangman.changeWrong(event.char)
            hangman.textUpdate()
            print("changeWrong called")

            
    elif event.keycode == 13: # keycode 13 == <enter>
        if not gamefinished:
            return
        else:        
            hangman.restart()
    
    
width = 400
height = 280    
# 선, 다각형, 원등을 그리기 위한 캔버스를 생성
canvas = Canvas(window, bg = "white", width = width, height = height)
canvas.pack()

hangman = Hangman()
print(words)
# Bind with <Key> event
canvas.bind("<Key>", processKeyEvent)
# key 입력 받기 위해 canvas가 focus 가지도록 함.
canvas.focus_set()

window.mainloop() # Create an event loop
