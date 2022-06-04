from tkinter import *
from tkinter import font
from tkinter import ttk
from urllib.request import urlopen
from tkinter import messagebox
from tkinter import *
import tkintermapview

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

#

def urlOpen():
    webbrowser.open("http://ncov.mohw.go.kr/")

def VaccinationCenter():
    global Ccolslst
    global Citemlst
    global curentsido
    global fitmlst

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
    InfoListBox.delete(0,InfoListBox.size())

    lstidx = SidoSelect.current()  # 시/도 콤보박스에서 현재 선택한 인덱스
    curentsido = sidovalues[lstidx]  # 인덱스 값으로 접근하여 텍스트 현재 시/도 얻어옴

    print("현재 선택한 시/도:", curentsido)    # 아무 시/도 도 선택하지 않았을때엔 랜덤으로 가리킴
    fitmlst = FindSidoHosp(curentsido)       # 현재 선택한 시/도에 해당하는 item을 저장한 list

    name = 0
    telno = 1
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
    global SigunguSelect

    # 사용할 폰트
    ##########################################################################
    fontTitle = font.Font(window, size=18, weight='bold')
    fontNormal = font.Font(window, size=15, weight='bold')
    fontInfo = font.Font(window, size=12, weight='bold')
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

    CovidNowButton = Button(SelectButtonFrame, text='발생 현황', height=5, width=20)
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