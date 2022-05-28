# 예방접종 센터 찾기 XML

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


CenterDoc = ET.parse('centers.xml')
Ctrresults = CenterDoc.getroot()
Ctrlst = Ctrresults.findall('data/item/col')  # 3976개의 정보
#lst = results.findall('data/item')     # 284개의 센터정보


#  분석하기 편하게 프리티로 확인
#print(CenterDoc.toprettyxml(newl='\n'))