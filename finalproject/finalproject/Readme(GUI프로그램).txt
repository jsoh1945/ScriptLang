mainGUI 에서 사용 하는 모듈 : Center.py, gmail_Send.py, Hosp.py, LiveCoronaInfoJson.py

Center.py
 : 예방접종 센터 찾기 XML에서 원하는 요소별 정보를 찾는 모듈. centers.xml 파일을 읽어와서 사용자가 원하는 카테고리만을 찾아 리턴하는 함수들을 내부에 구현.
(※주의 : FindCtr(): 함수는 원하는 요소(꼭 시/도 아니여도 됨. 이름, 위도,경도 다 가능) 포함하는 아이템들 리스트로 출력하는 함수고, FindCtrOnlyOne(): 함수는 최초로 일치하는 아이템 하나만 리턴하는 함수)

gmail_Send.py
: 메일 보내기 기능 모듈

Hosp.py
: 코로나 검사 실시기관.xml에서 원하는 요소별 정보를 찾는 모듈

LiveCoronaInfoJson.py
: 실시간 코로나 발생 현황을 openAPI로 받아와서 리스트에 관련 정보들을 저장

mainGUI
: GUI 프로그램의 메인 모듈
