import csv

from bs4 import BeautifulSoup
import requests
from csv import writer

url = "https://www.pararius.com/apartments/amsterdam"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
lists = soup.find_all('section', class_="listing-search-item")

with open('housing.csv', 'w', newline='') as f:
    rewriter = csv.writer(f)
    header = ['Title', 'Location', 'Price', 'Area']
    rewriter.writerow(header)
    for lst in lists:
        title = lst.find('a', class_="listing-search-item__link--title").text.replace('\n', '')
        print(title)
        location = lst.find('div', class_="listing-search-item__sub-title").text.replace('\n', '')
        price = lst.find('div', class_="listing-search-item__price").text.replace('\n', '')
        Area = lst.find('li', class_="illustrated-features__item--surface-area").text.replace('\n', '')
        info = [title, location, price, Area]
        rewriter.writerow(info)
