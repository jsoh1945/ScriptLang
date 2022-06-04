from email import message
from tkinter import *
from tkinter import font
from tkinter import ttk
from urllib.request import urlopen
from tkinter import messagebox
from tkinter import *
import tkintermapview
from LiveCoronaInfoJson import *

import webbrowser #URL 리다이렉션을 위한 import
from Hosp import *
from Center import *

window = Tk() #Create a window
window.title("코비디피아")  # Set title
window.geometry('600x900+450+100')

InfoListBox = Listbox()
MapBox = tkintermapview.TkinterMapView()
emailImage = None
titleImage = None
redirecImage = None

SymptomFlag = 0
SymptomText = Label()

sidovalues = set()
SidoSelect = ttk.Combobox()
curentsido = ''
fitmlst = []

graphWindow = " " #그래프를 그리는 윈도우

#예방접종 기관 버튼 클릭flag, 코로나검사 실시기관 버튼 클릭flag
#예방접종 센터 정보 버튼을 클릭하면 VaccinationClicked = True
#코로나검사 실시 센터 버튼을 클릭하면 HospClicked = True\
#실시간 정보 버튼을 클릭하면 LiveClicked = True
#실시간 정보 버튼을 여러번 클릭하지못하게하는 변수 graphShowed
VaccinationClicked = False
HospClicked = False
LiveClicked = False
graphShowed = False


def urlOpen():
    webbrowser.open("http://ncov.mohw.go.kr/")

def VaccinationCenter():
    global Ccolslst
    global Citemlst
    global curentsido
    global fitmlst
    global HospClicked
    global VaccinationClicked
    global LiveClicked

    VaccinationClicked = True
    if HospClicked or LiveClicked:
        HospClicked = False
        LiveClicked = False
    InfoListBox.delete(0, InfoListBox.size())

    sidolstidx = SidoSelect.current()  # 시/도 콤보박스에서 현재 선택한 인덱스
    curentsido = sidovalues[sidolstidx]  # 인덱스 값으로 접근하여 텍스트 현재 시/도 얻어옴
    fitmlst = FindCtr(curentsido)       # 현재 선택한 시/도에 해당하는 item을 저장한 list

    name = 0
    num = 1
    for fitem in fitmlst:
        for cols in fitem.findall('col'):
            if cols.get("name") == "facilityName":
                #print(cols.text)
                temp = cols.text
                InfoListBox.insert(name, temp)
                name += 1
                num += 1
    print("선택한 시/도: ", curentsido)
    print("======================================")

def SelectSido():
    global sidovalues
    global Ccolslst
    global fitmlst

    for item in Ccolslst:
        if item.get('name') == "sido":
            sidovalues.add(item.text)
    sidovalues = list(sidovalues)

    # #테스트용
    # for i in sidovalues:
    #     print(i)
    return sidovalues


#CenterInfoButton에 들어갈 command함수, GUI의 "코로나검사 실시 기관" 버튼을 누르면 실행되는 함수
def showHospInfo():
    global Hitemlst
    global curentsido
    global HospClicked
    global VaccinationClicked
    global LiveClicked

    HospClicked = True
    if VaccinationClicked or LiveClicked:
        VaccinationClicked = False
        LiveClicked = False
    InfoListBox.delete(0,InfoListBox.size())

    lstidx = SidoSelect.current()  # 시/도 콤보박스에서 현재 선택한 인덱스
    curentsido = sidovalues[lstidx]  # 인덱스 값으로 접근하여 텍스트 현재 시/도 얻어옴

    print("현재 선택한 시/도:", curentsido)    # 아무 시/도 도 선택하지 않았을때엔 랜덤으로 가리킴
    fitmlst = FindSidoHosp(curentsido)       # 현재 선택한 시/도에 해당하는 item을 저장한 list

    name = 0
    num = 1

    for fitem in fitmlst:
        temp = fitem.find('yadmNm').text
        InfoListBox.insert(name, temp)
        name += 1
        num += 1
    print("======================================")

#5월24일 증상/대처 버튼 클릭 시 텍스트 바뀌게하는 함수
def SymptomHandleTextChange():
    global SymptomText
    global SymptomFlag
    if SymptomFlag == 0:
        SymptomText["text"] = "대처법(오미크론): "+"\n"+"1. 물 하루에 2L 이상 마시기"+"\n"+"2. 주변 생활 환경이 건조하지 않도록 습도조절"+"\n"+"3. 식사 거르지 않고 영양분 충분히 챙기기"+"\n"+"4. 잠을 충분히 자기"
        SymptomFlag = 1
    else:
        SymptomText["text"] = "증상(오미크론): "+"\n"+"1. 심한 인후통"+"\n"+"2. 열이 있다면 미열"+"\n"+"3. 몸에 기운이 없고 힘이 빠짐"+"\n"+"4. 콧물"
        SymptomFlag = 0


def ViewMap():
    global InfoListBox
    global MapBox
    global HospClicked
    global LiveClicked

    if HospClicked or LiveClicked:
        messagebox.showerror("경고","해당 정보는 지도를 지원하지 않습니다")
        return
    lstidx = InfoListBox.curselection() # 현재 선택한 인덱스(튜플형태로 반환됨. 첫번째 원소가 인덱스값)
    if lstidx == ():
        messagebox.showerror("경고", "먼저 기관을 선택해주세요")
    else:
        #초기값 임의지정
        addr = "경기도 시흥시 산기대학로 237"
        lng = 0  # 경도
        lat = 0  # 위도

        findplace = InfoListBox.get(lstidx[0])
        print(findplace)

        fitem = FindCtrOnlyOne(findplace)
        for cols in fitem.findall('col'):
            if cols.get("name") == "lat":
                lat = float(cols.text)
            if cols.get("name") == "lng":
                lng = float(cols.text)
            if cols.get("name") == "address":
                addr = cols.text

        MapBox.set_position(lat, lng)  # 위도,경도 위치지정
        marker_1 = MapBox.set_address(addr, marker=True)
        MapBox.set_zoom(15)  # 0~19 (19 is the highest zoom level)

        # 주소 위치지정 (마크 표시되는 기관만 표시함(한글주소여서 오류발생하는 기관존재))
        if marker_1:
            #print(marker_1.position, marker_1.text)  # get position and text
            marker_1.set_text(findplace)  # set new text

def ViewDetail():
    global InfoListBox
    global MapBox
    global VaccinationClicked
    global HospClicked
    global LiveClicked

    if HospClicked or LiveClicked:
        messagebox.showerror("경고","예방접종 센터 정보 버튼을 클릭한 상태가 아닙니다")
        return

    lstidx = InfoListBox.curselection() # 현재 선택한 인덱스(튜플형태로 반환됨. 첫번째 원소가 인덱스값)

    if lstidx == ():
        messagebox.showerror("경고", "먼저 기관을 선택해주세요")
    else:
        findplace = InfoListBox.get(lstidx[0])
        fitem = FindCtrOnlyOne(findplace)
        for cols in fitem.findall('col'):
            if cols.get("name") == "address":
                addr = cols.text
            if cols.get("name") =="phoneNumber":
                tel = cols.text
            if cols.get("name") =="centerName":
                ctrname = cols.text
        msgboxstr = "예방접종센터명: "+findplace+"\n"\
                   +"공식센터명: "+ctrname+"\n"\
                   +"전화번호: "+tel+"\n"\
                   +"주소: "+addr
        messagebox.showinfo("예방접종센터 정보",msgboxstr)
        print("예방접종센터명: ", findplace)
        print("공식센터명: ", ctrname)
        print("전화번호: ", tel)
        print("주소: ", addr)

def HViewDetail():
    global InfoListBox
    global MapBox
    global VaccinationClicked
    global HospClicked
    global LiveClicked
    
    if VaccinationClicked or LiveClicked:
        messagebox.showerror("경고","코로나검사 실시 센터 버튼을 클릭하지 않았습니다")
        return
    lstidx = InfoListBox.curselection() # 현재 선택한 인덱스(튜플형태로 반환됨. 첫번째 원소가 인덱스값)
    if lstidx == ():
        messagebox.showerror("경고", "먼저 기관을 선택해주세요")
    else:
        findplace = InfoListBox.get(lstidx[0])
        print(findplace)
        fitem = FindNameHosp(findplace) 
        #name = fitem.find('yadmNm').text
        tel = fitem.find('telno').text
        sido = fitem.find('sidoNm').text
        sgg = fitem.find('sgguNm').text

        msgboxstr = "코로나 검사기관명: "+findplace+"\n"\
                    +"전화번호: "+tel+"\n"\
                    +"주소: "+sido+sgg
        messagebox.showinfo("기관정보",msgboxstr)
        print("코로나 검사기관명: ", findplace)
        print("전화번호: ", tel)
        print("주소: ", sido, sgg)        
    
def LiveInfo():
    global HospClicked
    global VaccinationClicked
    global LiveClicked
    global InfoListBox
    global LiveCoronaInfo
    global graphShowed
    global graphWindow

    if graphShowed:
        messagebox.showerror("경고","두번 이상 클릭 할 수 없습니다")
        return
    InfoListBox.delete(0,InfoListBox.size())
    LiveClicked = True
    graphShowed = True
    if HospClicked or VaccinationClicked:
        HospClicked = False
        VaccinationClicked = False
    data = []
    dataName = []
    for k in LiveCoronaInfo:
        if k == 'mmddhh':
            InfoListBox.insert(0,"기준 일시: "+"2022.0"+LiveCoronaInfo[k])
        elif k == 'cnt_confirmations':
            InfoListBox.insert(0,"일일 확진자: "+LiveCoronaInfo[k]+"명")
        elif k == 'cnt_hospitalizations':
            InfoListBox.insert(0,"일일 신규입원자: "+LiveCoronaInfo[k]+"명")
        elif k == 'cnt_severe_symptoms':
            InfoListBox.insert(0,"일일 재원 위중증 발생자: "+LiveCoronaInfo[k]+"명")
        elif k == 'cnt_deaths':
            InfoListBox.insert(0,"일일 사망자: "+LiveCoronaInfo[k]+"명")
        elif k == 'rate_deaths':
            data.append(float(LiveCoronaInfo[k]))
            dataName.append('사망자')
        elif k == 'rate_hospitalizations':
            data.append(float(LiveCoronaInfo[k]))
            dataName.append('신규 입원자')                  
        elif k == 'rate_severe_symptoms':
            data.append(float(LiveCoronaInfo[k]))
            dataName.append('재원 위중증 발생자')     
    graphWindow = Tk()
    graphWindow.title('10만명당 점유율')
    graphWindow.geometry('400x400+200+100')
    graphWindow.protocol("WM_DELETE_WINDOW",on_closing_graphWindow)
    canvas = Canvas(graphWindow,width=300,height=300)
    canvas.place(relx=.5,rely=.5,anchor=CENTER)
    drawGraph(canvas,data,dataName,300,300)
    
def on_closing_graphWindow():
    global graphShowed
    global graphWindow
    graphShowed = False
    graphWindow.destroy()
    

def drawGraph(canvas, data, dataName, cWidth,cHeight):
    if not len(data):
        canvas.create_text(cWidth/2,cHeight/2,text="no data")
        return
    
    nData = len(data)
    nMax = max(data)
    nMin = min(data)

    canvas.create_rectangle(0,0,cWidth,cHeight,fill='white')
    if nMax == 0:
        nMax = 1
    rectWidth = (cWidth // nData)
    bottom = cHeight - 20
    maxheight = cHeight -40
    
    for i in range(nData):
        if nMax == data[i]:color='red'
        elif nMin == data[i]:color='blue'
        else:color = 'grey'

        curHeight = maxheight * data[i]/nMax
        top = bottom - curHeight
        left = i*rectWidth
        right = (i+1)*rectWidth
        canvas.create_rectangle(left,top,right,bottom,fill=color,activefill='yellow')
        canvas.create_text((left+right)//2,top-10,text=str(data[i])+'명')
        canvas.create_text((left+right)//2,bottom+10,text=dataName[i])
    
def InitScreen():
    global InfoListBox
    global MapBox

    global emailImage
    global titleImage
    global redirecImage

    global SymptomFlag
    global SymptomText
    global sidovalues

    global SidoSelect

    # 사용할 폰트
    ##########################################################################
    fontTitle = font.Font(window, size=18, weight='bold')
    fontNormal = font.Font(window, size=15, weight='bold')
    ##########################################################################

    # 1번째 - 로고, 이메일, 리다이렉션 버튼
    ##########################################################################
    TopFrame = Frame(window, width=600, height=50, background='#005BAF')
    TopFrame.pack(side='top', fill='x')

    titleImage = PhotoImage(file='logo.png')
    titleText = Label(TopFrame, image=titleImage, font=fontTitle, relief='ridge')
    titleText.grid(row=0, column=0)

    emailImage = PhotoImage(file="email.png")  # 이메일 이미지 추가
    emailButton = Button(TopFrame, image=emailImage, padx=5, pady=5)  # 이메일 버튼에 이미지 심어놓음
    emailButton.grid(row=0, column=1)

    redirecImage = PhotoImage(file='redirec.png')
    redirectButton = Button(TopFrame, image= redirecImage,anchor='center', padx=5, pady=5,
                            command=urlOpen)
    redirectButton.grid(row=0, column=2)
    ##########################################################################

    # 2번째 시,도 선택
    ##########################################################################
    ProvinceCitySelectFrame = Frame(window, width=600, height=50, background='#005BAF')
    ProvinceCitySelectFrame.pack(side='top', fill='x')

    ProvinceText = Label(ProvinceCitySelectFrame, text='      시/도 선택: ', font=fontNormal)
    ProvinceText.grid(row=0, column=0)

    SidoSelect = ttk.Combobox(ProvinceCitySelectFrame, width=27, height=10, values=SelectSido())
    SidoSelect.grid(row=0, column=1)

    ViewMapSelect = Button(ProvinceCitySelectFrame, text='맵보기', padx=5, command=ViewMap)
    ViewMapSelect.grid(row=0, column=2)

    ViewDetailSelect = Button(ProvinceCitySelectFrame, text='접종센터정보', padx=4, command=ViewDetail)
    ViewDetailSelect.grid(row=0, column=3)

    HViewDetailSelect = Button(ProvinceCitySelectFrame, text='검사기관정보', padx=4, command=HViewDetail)
    HViewDetailSelect.grid(row=0, column=4)

    ##########################################################################

    # 3번째 발생현황, 병원정보, 예방접종센터 선택 버튼
    ##########################################################################
    SelectButtonFrame = Frame(window, width=600, height=100, background='#005BAF')
    SelectButtonFrame.pack(side='top', fill='x')

    CovidNowButton = Button(SelectButtonFrame, text='발생 현황', height=5, width=20, command=LiveInfo)
    CovidNowButton.grid(row=0, column=0, padx=24)

    CenterInfoButton = Button(SelectButtonFrame, text='예방접종 센터 정보', height=5, width=20, command=VaccinationCenter)
    CenterInfoButton.grid(row=0, column=1, padx=25)

    HosInfoButton = Button(SelectButtonFrame, text='코로나 검사 실시 센터', height=5, width=20, command=showHospInfo)
    HosInfoButton.grid(row=0, column=2, padx=24)
    ##########################################################################

    # 4번째 지도 표시 & 리스트
    ##########################################################################
    MapAndListFrame = Frame(window, width=300, height=570, background='#005BAF')
    MapAndListFrame.pack()

    # 맵
    MapBox = tkintermapview.TkinterMapView(MapAndListFrame, width=300, height=500, corner_radius=0)
    MapBox.grid(row=0, column=0)

    # 정보 출력 리스트 박스
    Infocrollbar = Scrollbar(MapAndListFrame)
    InfoListBox = Listbox(MapAndListFrame, selectmode='extended', \
                          font=fontNormal, width=25, height=19, \
                          borderwidth=12, relief='ridge', yscrollcommand=Infocrollbar.set)
    InfoListBox.grid(row=0, column=1)

    ##########################################################################

    # 5번째 증상 및 대처
    ##########################################################################
    symptomAndhandleFrame = Frame(window, width=600, height=157, background='#005BAF')
    symptomAndhandleFrame.pack(side='top', fill='x')

    SymptomHandleButton = Button(symptomAndhandleFrame, text='증상/대처법', height=5, width=20,
                                 command=SymptomHandleTextChange)
    SymptomHandleButton.grid(row=0, column=0)

    SymptomText = Label(symptomAndhandleFrame,
                        text="증상: " + "\n" + "1. 심한 인후통" + "\n" + "2. 열이 있다면 미열" + "\n" + "3. 몸에 기운이 없고 힘이 빠짐" + "\n" + "4. 콧물",
                        font=fontTitle, width=28, height=5, borderwidth=12, relief='ridge')
    SymptomText.grid(row=0, column=1)
    SymptomFlag = 0  # 0 = 증상, 1 = 대처
    ##########################################################################


InitScreen()

window.mainloop()