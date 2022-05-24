from tkinter import *
from tkinter import font
from tkinter import ttk
from urllib.request import urlopen
import webbrowser #URL 리다이렉션을 위한 import


window = Tk() #Create a window
window.title("코비디피아")  # Set title
window.geometry('600x900+450+100')


#사용할 폰트
##########################################################################
fontTitle = font.Font(window,size=18,weight='bold')
fontNormal = font.Font(window,size=15,weight='bold')
##########################################################################

def urlOpen():
    webbrowser.open("http://ncov.mohw.go.kr/")


#1번째 - 로고, 이메일, 리다이렉션 버튼
##########################################################################
TopFrame = Frame(window,width=600,height=50,background='#00FF00')
TopFrame.pack(side='top', fill='x')


titleText = Label(TopFrame,text='코비디피아', font=fontTitle,width=20,height=3,borderwidth=12,relief='ridge')
titleText.grid(row=0,column=0)

emailImage = PhotoImage(file="email.png") # 이메일 이미지 추가
emailButton = Button(TopFrame, image=emailImage,padx=5,pady=5) # 이메일 버튼에 이미지 심어놓음
emailButton.grid(row=0,column=1)

redirectButton = Button(TopFrame,text='리다이렉션',width=17,height=6,anchor='center',padx=5,pady=5,command=urlOpen)
redirectButton.grid(row=0,column=2)
##########################################################################

#2번째 시,도 선택 
##########################################################################
ProvinceCitySelectFrame = Frame(window,width=600,height=50,background='#0000FF')
ProvinceCitySelectFrame.pack(side='top', fill='x')

ProvinceText = Label(ProvinceCitySelectFrame,text='        도 선택: ',font=fontNormal)
ProvinceText.grid(row=0,column=0)

values=[str(i)+"번" for i in range(1, 101)] 
ProvinceSelect = ttk.Combobox(ProvinceCitySelectFrame,height=10,values=values)
ProvinceSelect.grid(row=0,column=1)

CityText = Label(ProvinceCitySelectFrame,text='     시 선택: ',font=fontNormal)
CityText.grid(row=0,column=2)

CitySelect = ttk.Combobox(ProvinceCitySelectFrame,height=10,values=values)
CitySelect.grid(row=0,column=3)
##########################################################################


#3번째 발생현황, 병원정보, 예방접종센터 선택 버튼
##########################################################################
SelectButtonFrame = Frame(window,width=600,height=100,background='#FF0000')
SelectButtonFrame.pack(side='top', fill='x')

CovidNowButton = Button(SelectButtonFrame,text='발생 현황',height=5,width=20)
CovidNowButton.grid(row=0,column=0,padx=24)

HosInfoButton = Button(SelectButtonFrame,text='병원 정보',height=5,width=20)
HosInfoButton.grid(row=0,column=1,padx=25)

CenterInfoButton = Button(SelectButtonFrame,text='예방접종 센터',height=5,width=20)
CenterInfoButton.grid(row=0,column=2,padx=24)
##########################################################################

#4번째 지도 표시 & 리스트
##########################################################################
MapAndListFrame = Frame(window,width=600,height=570,background='#FFFF00')
MapAndListFrame.pack(side='top', fill='x')

#맵구현하면 넣을예정
MapScrollbar = Scrollbar(MapAndListFrame)
MapBox = Listbox(MapAndListFrame, selectmode='extended',\
                 font=fontNormal, width=25, height=19, \
                 borderwidth=12, relief='ridge', yscrollcommand=MapScrollbar.set)
MapBox.grid(row=0,column=0)

Infocrollbar = Scrollbar(MapAndListFrame)
InfoListBox = Listbox(MapAndListFrame, selectmode='extended',\
                 font=fontNormal, width=25, height=19, \
                 borderwidth=12, relief='ridge', yscrollcommand=Infocrollbar.set)
InfoListBox.grid(row=0,column=1)
##########################################################################

#5월24일 증상/대처 버튼 클릭 시 텍스트 바뀌게하는 함수
def SymptomHandleTextChange():
    global SymptomText
    global SymptomFlag
    if SymptomFlag == 0:
        SymptomText["text"] = "이건 대처입니다"
        SymptomFlag = 1
    else:
        SymptomText["text"] = "증상은 이러이러 합니다"
        SymptomFlag = 0


#5번째 증상 및 대처
##########################################################################
symptomAndhandleFrame = Frame(window,width=600,height=157,background='#FF00FF')
symptomAndhandleFrame.pack(side='top', fill='x')

SymptomHandleButton = Button(symptomAndhandleFrame,text='증상/대처법',height=5,width=20, command=SymptomHandleTextChange)
SymptomHandleButton.grid(row=0,column=0)

SymptomText = Label(symptomAndhandleFrame,text='증상은 이러이러 합니다', font=fontTitle,width=28,height=5,borderwidth=12,relief='ridge')
SymptomText.grid(row=0,column=1)
SymptomFlag = 0 # 0 = 증상, 1 = 대처
##########################################################################



window.mainloop()