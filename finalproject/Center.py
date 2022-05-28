from pprint import pprint
from xml.dom.minidom import parse
import xml.etree.ElementTree as ET


CenterDoc = None

def LoadXMLFromFile():
    with open("centers.xml", encoding='utf-8') as xmlFD:
        try:
            dom = parse(xmlFD)
        except Exception:
            print('loading failed')
        else:
            print('XML loading complete')
            return dom

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


#CenterDoc = LoadXMLFromFile()
CenterDoc = ET.parse('centers.xml')

results = CenterDoc.getroot()
lst = results.findall('data/item/col')  # 3976개의 정보
#lst = results.findall('data/item')     # 284개의 센터정보


for item in lst:
    #item.get('name')
    if item.get('name') == "facilityName":
        print(item.text)


#  분석하기 편하게 프리티로 확인
#print(CenterDoc.toprettyxml(newl='\n'))