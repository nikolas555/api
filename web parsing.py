import requests
from bs4 import BeautifulSoup
import csv
from time import sleep
from random import randint
payloads = {'groups': 'emmy_winner', 'start': 1}
url = 'https://www.imdb.com/search/title/'
h = {'Accept-Language': 'en-US'}
file = open('imdb.csv', 'w', newline='\n', encoding='UTF-8_sig')
csv_obj = csv.writer(file)
csv_obj.writerow(['დასახელება', 'წელი', 'რეიტინგი'])
file.write('Title,Year,Ranking\n')

while payloads['start']<250:
    response = requests.get(url, params=payloads, headers=h)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')
    small_soup = soup.find('div', class_='lister-item mode-advanced')

    movies = small_soup.find_all('div', class_='lister-item mode-advanced')
    for movie in movies:
        title = movie.h3.a.text
        year = movie.find('span', class_='lister-item-year').text
        year = year.replace('(', '')
        year = year.replace(')', '')
        ranking = movie.strong.text
        print(title, year, ranking)
        file.write(title + ',' + year + ',' + ranking + '\n')
        csv_obj.writerow([title, year, ranking])
    payloads['start'] += 50
    sleep(randint(5, 20))