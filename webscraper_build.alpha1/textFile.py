from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import csv

teststr = "/players/a/allenja01.html"

splitstr = teststr.split("/")

print(splitstr)

target = teststr.split("/")[3]

print(target)

extract = target.split(".")[0]

print(target.split("."))
print(extract)

sample = {'cartevi01': ['Vince Carter', '/players/c/cartevi01.html']}

id = 'cartevi01'
info = sample.get(id)

print(info)

url = 'https://www.basketball-reference.com'

driver = webdriver.Chrome(
    #executable_path='C:/Users/New/Google Drive/CS4411 - Project/webscraper_build.alpha1/chromedriver.exe'
    executable_path='/usr/local/Cellar/chromedriver/2.37/bin'
)

target_url = url + info[1]

print(target_url)

driver.get(target_url)

# time.sleep(1)

html = BeautifulSoup(driver.page_source, "html.parser")

driver.close()

table = html.find('table', attrs={'id': 'per_poss'})

headers = table.find('thead')
fields = headers.find_all('th')
field_names = ['player_id']

for field in fields:
    field_names.append(field.text)

print(field_names)

player_stats = []
stats = table.find('tbody')
stat_lines = stats.find_all('tr')
for stat_line in stat_lines:
    season = stat_line.th.a.text
    per_season = stat_line.find_all('td')

    # identifier = season.split('-')[0] + season.split('-')[1]

    year = int(season.split('-')[0])

    # print('2000, ', year)

    games = int(stat_line.find('td', attrs={'data-stat': 'g'}).text)
    # print('games played', games)

    row = [id, season]

    for value in per_season:
        row.append(value.text)

    player_stats.append(row)

with open('test.csv', 'w') as testF:
    exporter = csv.writer(testF)
    exporter.writerow(field_names)
    exporter.writerows(player_stats)


for row in player_stats:
    print(row)

