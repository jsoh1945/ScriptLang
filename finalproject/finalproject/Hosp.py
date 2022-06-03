# 코로나 검사기관 찾기

from pprint import pprint
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET

HospDoc = None

def checkDoc():
    global HospDoc
    if HospDoc == None:
        print("Doc Empty")
        return False
    return True

def freeDom():
    global HospDoc
    if checkDoc():
        HospDoc.unlink()
        print('free HospDoc complete')



HospDoc = ET.parse('코로나검사 실시기관.xml')
Hospres = HospDoc.getroot()  #response
Hitemlst = Hospres.findall('body/items/item')   # 총 102개의 검사실시기관
Hitemslst = Hospres.findall('body/items')


def FindSidoHosp(findsido):
    temp = []
    for item in Hitemlst:
        if item.find('sidoNm').text == findsido:
            temp.append(item)
    return temp

def FindNameHosp(findname):
    temp = []
    for item in Hitemlst:
        if item.find('yadmNm').text == findname:
            return item



# fitmlst = FindSidoHosp('서울')
# for fitem in fitmlst:
#     print(fitem.find('yadmNm').text)


#  모든 지역의 검사기관 출력 테스트
# for item in Hitemlst:
#     print(item.find('yadmNm').text)

# #  모든 지역 출력 테스트 (XML 지역명 표기 다름 바꿔야함)
# temptest = set()
# for item in Hitemlst:
#     temptest.add(item.find('sidoNm').text)


#print(HospDoc.toprettyxml(newl='\n'))
