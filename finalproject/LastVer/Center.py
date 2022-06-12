# 예방접종 센터 찾기 XML 가공 모듈

from pprint import pprint
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET

CenterDoc = None

def checkDoc():
    global CenterDoc
    if CenterDoc == None:
        print("Doc Empty")
        return False
    return True

def freeDom():
    global CenterDoc
    if checkDoc():
        CenterDoc.unlink()
        print('free CenterDoc complete')


#  분석하기 편하게 프리티로 확인
#print(CenterDoc.toprettyxml(newl='\n'))

CenterDoc = ET.parse('centers.xml')
Ctrresults = CenterDoc.getroot()
Ccolslst = Ctrresults.findall('data/item/col')  # 3976개의 정보
Citemlst = Ctrresults.findall('data/item')
#lst = results.findall('data/item')     # 284개의 센터정보

# 원하는 요소(꼭 시/도 아니여도 됨. 이름, 위도,경도 다 가능) 포함하는 아이템들 리스트로 출력하는 함수
def FindCtr(findsido):
    temp = []
    for item in Citemlst:
        for col in item:
            if col.text == findsido:
                #cnt += 1
                #return item        #해당 아이템 찾자마자 꺼내는 코드(테스트용)
                temp.append(item)   #해당 아이템 찾으면 리스트에 추가
    return temp


# 찾는 요소 중 최초로 일치하는 아이템 하나만 리턴하는 함수
def FindCtrOnlyOne(findsido):
    temp = []
    for item in Citemlst:
        for col in item:
            if col.text == findsido:
                #cnt += 1
                #return item        #해당 아이템 찾자마자 꺼내는 코드(테스트용)
                #temp.append(item)
                return item

# fitmlst = FindSidoCtr('서울특별시')
# for fitem in fitmlst:
#     for cols in fitem.findall('col'):
#         if cols.get("name")=="facilityName":
#             print(cols.text)


# #해당 item 꺼내와서 출력 테스트 코드
# tempcol = tempitem.findall('col')
# for col in tempcol:
#     print(col.text)

