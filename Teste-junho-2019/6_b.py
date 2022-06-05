from bs4 import BeautifulSoup
import requests 

def get_weather(texto):
    html = texto
    soup = BeautifulSoup(html, 'html5lib')
    days = soup.find_all('div',class_ = 'weekly-column')
    weather = []
    for day in days:
        day_weather = {}
        day_weather['date'] = day.find('div', class_ = 'date').text
        day_weather['prev_txt'] = day.find('img', class_ = 'weatherImg')['title']
        day_weather['temp_min'] = int(day.find('span', class_ = 'tempMin').text[:-1])
        day_weather['temp_max'] = int(day.find('span', class_ = 'tempMax').text[:-1])
        uv = day.find('img',class_='iuvImg')
        if uv:
            uv = int(uv['title'].split()[1])
            day_weather['uv'] = uv 
        weather.append(day_weather)

    return weather

texto = open('6_b.html','r',encoding='UTF-8').read()
print(get_weather(texto))