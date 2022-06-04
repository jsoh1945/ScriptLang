import requests

url = 'http://apis.data.go.kr/1790387/covid19CurrentStatusKorea/covid19CurrentStatusKoreaJason'
params ={'serviceKey' : 'W4aKgIXbfeyVPnSEdsvSTzY4hlbQsmC7xwQXeL8J3ApXRYCaPXCICZU/vwVK4GrTe6H5r/tMdTqmwbtpKQSj9A==' }



response = requests.get(url, params=params)
result = response.json()

LiveCoronaInfo = result['response']['result'][0]

print(LiveCoronaInfo)
#형식: LiveCoronaInfo['원하는내용']
#--------여기를 이용해서 그래프 만들 예정---------
#rate_hospitalizations - 인구 10만명당 신규입원 
#rate_confirmations - 인구 10만명당 확진
#rate_deaths - 인구10만명당 사망

#--------리스트박스에 표시----------
#cnt_deaths - 일일사망 발생현황
#cnt_severe_symptoms - 일일 재원 위중증 발생현황
#cnt_hospitalizations - 일일 신규 입원 발생현황
#cnt_confirmations - 일일 확진 발생현황
#mmddhh - 데이터 조회 기준일시

