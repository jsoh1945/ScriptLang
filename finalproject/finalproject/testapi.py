# Python3 샘플 코드 #

# #건강보험심사평가원_코로나19병원정보(국민안심병원 외)서비스
# import requests

# url = 'http://apis.data.go.kr/B551182/pubReliefHospService/getpubReliefHospList'
# params ={'serviceKey' : '	Z1rQy2Cp5%2BrARrARu8dfhpaHGuow6M2z4zIJDFtAdSXwUKNt9X7MU9QiAeo2b2pvi4DxToIuWG1UkxKYamAq8A%3D%3D', 'pageNo' : '1', 'numOfRows' : '10', 'spclAdmTyCd' : 'A0' }

# response = requests.get(url, params=params)
# print(response.content)


#==========================================================================
#질병관리청_코로나19 국내발생현황 조회
import requests

url = 'http://apis.data.go.kr/1790387/covid19CurrentStatusKorea/covid19CurrentStatusKoreaJason'
params ={'serviceKey' : '서비스키' }

response = requests.get(url, params=params)
print(response.content)