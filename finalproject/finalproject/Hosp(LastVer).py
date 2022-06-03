from pprint import pprint
from xml.dom.minidom import parse
from xml.etree import ElementTree

HospDoc = None

def LoadXMLFromFile():
    with open("코로나검사 실시기관.xml",encoding='utf-8') as xmlFD:
        try:
            dom = parse(xmlFD)
        except Exception:
            print('loading failed')
        else:
            print('XML loading complete')
            return dom

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


HospDoc = LoadXMLFromFile()
#print(HospDoc.toprettyxml(newl='\n'))
