from msilib.schema import ListBox
from tkinter import *
from tkinter import font
from tkinter import ttk
from urllib.request import urlopen
import webbrowser #URL 리다이렉션을 위한 import
from Hosp import *
from Center import *

window = Tk() #Create a window
window.title("코비디피아")  # Set title
window.geometry('600x900+450+100')

InfoListBox = Listbox()
emailImage = None

SymptomFlag = 0
SymptomText = Label()

sidovalues = set()
sigunguvalues = set()

ProvinceSelect = ttk.Combobox()
CitySelect = ttk.Combobox()


def urlOpen():
    webbrowser.open("http://ncov.mohw.go.kr/")

def VaccinationCenter():
    global Ccolslst
    global Citemlst

    InfoListBox.delete(0, InfoListBox.size())

    lstidx = ProvinceSelect.current()  # 시/도 콤보박스에서 현재 선택한 인덱스
    curentsido = sidovalues[lstidx]  # 인덱스 값으로 접근하여 텍스트 현재 시/도 얻어옴

    print("현재 선택한 시/도:", curentsido)    # 아무 시/도 도 선택하지 않았을때엔 랜덤으로 가리킴
    fitmlst = FindSidoCtr(curentsido)       # 현재 선택한 시/도에 해당하는 item을 저장한 list

    name = 0
    telno = 1
    num = 1

    for fitem in fitmlst:
        for cols in fitem.findall('col'):
            if cols.get("name") == "facilityName":
                #print(cols.text)
                temp = "[" + str(num) + "]" + cols.text
                InfoListBox.insert(name, temp)
                name += 1
                num += 1
    print("======================================")

    #################################################################
    # name = 0
    # telno = 1
    # num = 1
    # for col in Ccolslst:
    #     if col.get('name') == "facilityName":
    #         temp = "["+ str(num) + "]" + col.text
    #         InfoListBox.insert(name, temp)
    #         name += 2
    #         num += 1
    #
    # for col in Ccolslst:
    #     if col.get('name') == "phoneNumber":
    #         temp = 'Tel: ' + str(col.text)
    #         InfoListBox.insert(telno, temp)
    #         telno += 2


def SelectSido():
    global sidovalues
    global Ccolslst

    for item in Ccolslst:
        if item.get('name') == "sido":
            sidovalues.add(item.text)
    sidovalues = list(sidovalues)

    # #테스트용
    # for i in sidovalues:
    #     print(i)

    return sidovalues


def SelectSigungu():
    global sigunguvalues
    global Ccolslst

    for item in Ccolslst:
        if item.get('name') == "sigungu":
            if item.text != None:
                sigunguvalues.add(item.text)

    sigunguvalues = list(sigunguvalues)
    return sigunguvalues


#CenterInfoButton에 들어갈 command함수, GUI의 "코로나검사 실시 기관" 버튼을 누르면 실행되는 함수
def showHospInfo():
    global Hitemlst

    InfoListBox.delete(0,InfoListBox.size())

    lstidx = ProvinceSelect.current()  # 시/도 콤보박스에서 현재 선택한 인덱스
    curentsido = sidovalues[lstidx]  # 인덱스 값으로 접근하여 텍스트 현재 시/도 얻어옴

    print("현재 선택한 시/도:", curentsido)    # 아무 시/도 도 선택하지 않았을때엔 랜덤으로 가리킴
    fitmlst = FindSidoHosp(curentsido)       # 현재 선택한 시/도에 해당하는 item을 저장한 list

    name = 0
    telno = 1
    num = 1

    for fitem in fitmlst:
        #print(fitem.find('yadmNm').text)
        temp = "[" + str(num) + "]" + fitem.find('yadmNm').text
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


def InitScreen():
    global InfoListBox
    global emailImage
    global SymptomFlag
    global SymptomText
    global sidovalues

    global ProvinceSelect
    global CitySelect

    # 사용할 폰트
    ##########################################################################
    fontTitle = font.Font(window, size=18, weight='bold')
    fontNormal = font.Font(window, size=15, weight='bold')
    ##########################################################################

    # 1번째 - 로고, 이메일, 리다이렉션 버튼
    ##########################################################################
    TopFrame = Frame(window, width=600, height=50, background='#00FF00')
    TopFrame.pack(side='top', fill='x')

    titleText = Label(TopFrame, text='코비디피아', font=fontTitle, width=20, height=3, borderwidth=12, relief='ridge')
    titleText.grid(row=0, column=0)

    emailImage = PhotoImage(file="email.png")  # 이메일 이미지 추가
    emailButton = Button(TopFrame, image=emailImage, padx=5, pady=5)  # 이메일 버튼에 이미지 심어놓음
    emailButton.grid(row=0, column=1)

    redirectButton = Button(TopFrame, text='리다이렉션', width=17, height=6, anchor='center', padx=5, pady=5,
                            command=urlOpen)
    redirectButton.grid(row=0, column=2)
    ##########################################################################

    # 2번째 시,도 선택
    ##########################################################################
    ProvinceCitySelectFrame = Frame(window, width=600, height=50, background='#0000FF')
    ProvinceCitySelectFrame.pack(side='top', fill='x')

    ProvinceText = Label(ProvinceCitySelectFrame, text='      시/도 선택: ', font=fontNormal)
    ProvinceText.grid(row=0, column=0)

    #values = [str(i) + "번" for i in range(1, 284 + 1)]
    ProvinceSelect = ttk.Combobox(ProvinceCitySelectFrame, height=10, values=SelectSido())
    ProvinceSelect.grid(row=0, column=1)

    CityText = Label(ProvinceCitySelectFrame, text='시/군/구선택: ', font=fontNormal)
    CityText.grid(row=0, column=2)

    CitySelect = ttk.Combobox(ProvinceCitySelectFrame, height=10, values=SelectSigungu())
    CitySelect.grid(row=0, column=3)
    ##########################################################################

    # 3번째 발생현황, 병원정보, 예방접종센터 선택 버튼
    ##########################################################################
    SelectButtonFrame = Frame(window, width=600, height=100, background='#FF0000')
    SelectButtonFrame.pack(side='top', fill='x')

    CovidNowButton = Button(SelectButtonFrame, text='발생 현황', height=5, width=20)
    CovidNowButton.grid(row=0, column=0, padx=24)

    HosInfoButton = Button(SelectButtonFrame, text='예방접종 센터 정보', height=5, width=20, command=VaccinationCenter)
    HosInfoButton.grid(row=0, column=1, padx=25)

    CenterInfoButton = Button(SelectButtonFrame, text='코로나 검사 실시 센터', height=5, width=20, command=showHospInfo)
    CenterInfoButton.grid(row=0, column=2, padx=24)
    ##########################################################################

    # 4번째 지도 표시 & 리스트
    ##########################################################################
    MapAndListFrame = Frame(window, width=600, height=570, background='#FFFF00')
    MapAndListFrame.pack(side='top', fill='x')

    # 맵구현하면 넣을예정
    MapScrollbar = Scrollbar(MapAndListFrame)
    MapBox = Listbox(MapAndListFrame, selectmode='extended', \
                     font=fontNormal, width=25, height=19, \
                     borderwidth=12, relief='ridge', yscrollcommand=MapScrollbar.set)
    MapBox.grid(row=0, column=0)

    Infocrollbar = Scrollbar(MapAndListFrame)
    InfoListBox = Listbox(MapAndListFrame, selectmode='extended', \
                          font=fontNormal, width=25, height=19, \
                          borderwidth=12, relief='ridge', yscrollcommand=Infocrollbar.set)
    InfoListBox.grid(row=0, column=1)
    ##########################################################################

    # 5번째 증상 및 대처
    ##########################################################################
    symptomAndhandleFrame = Frame(window, width=600, height=157, background='#FF00FF')
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