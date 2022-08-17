# 실검코드
import requests

url = "http://www.daum.net/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.findAll("a","link_favorsch"))
# 날씨코드
city = "Seoul"
apikey = "################################"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"

result = requests.get(api)
print(result.text)

## response, apikey BeautifulSoup에 대해 조금 더 잘 알게됨