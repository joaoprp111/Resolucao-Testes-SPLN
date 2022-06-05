from bs4 import BeautifulSoup
import requests 
import pprint

def get_race_results(num_GP,localizacao):
    url = 'https://www.formula1.com/en/results.html/2019/races/' + str(num_GP) + '/' + localizacao + '/race-result.html'
    html = requests.get(url).text 
    soup = BeautifulSoup(html,'html5lib')
    race = soup.find('h1',class_ = 'ResultsArchiveTitle').text 
    race = race.split(' - ')[0].strip('\n ')
    date = soup.find('span', class_ = 'full-date').text 
    location = soup.find('span', class_ = 'circuit-info').text 
    standings_table = soup.find('table',class_='resultsarchive-table')
    table_tbody = standings_table.find('tbody')
    drivers = table_tbody.find_all('tr')
    standings = list()
    for driver in drivers:
        driver_info = {}
        driver_info['pos'] = driver.select('td:nth-of-type(2)')[0].text
        driver_info['laps'] = int(driver.select('td:nth-of-type(3)')[0].text)
        driver_info['pts'] = int(driver.select('td:nth-of-type(8)')[0].text)
        driver_info['time'] = driver.select('td:nth-of-type(7)')[0].text
        driver_name_info = driver.select('td:nth-of-type(4)')[0]
        name_spans = driver_name_info.find_all('span')
        count = 1
        driver_info['driver'] = ''
        for span_tag in name_spans:
            if count <= 2:
                driver_info['driver'] += span_tag.text
                if count == 1:
                    driver_info['driver'] += ' '
                count += 1
        driver_info['team'] = driver.select('td:nth-of-type(5)')[0].text
        standings.append(driver_info)
    race_results = {}
    race_results['date'] = date
    race_results['location'] = location 
    race_results['race'] = race
    race_results['standings'] = standings

    return race_results

with open('output_6b.txt','w',encoding='UTF-8') as f:
    f.write(str(get_race_results(1006,'canada')))