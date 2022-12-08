import requests
from bs4 import BeautifulSoup
import csv
from csv import writer

url = "https://books.toscrape.com/catalogue/category/books_1/index.html"

response = requests.get(url)

# soup = BeautifulSoup(response.text, 'html.parser')
category = []


    
URL_base = 'https://books.toscrape.com/catalogue/category/'
soup_index = BeautifulSoup(response.text, "lxml")
liste_li = soup_index.find(
    'ul', {'class': "nav nav-list"}).find('ul').find_all('li')
for li in liste_li:
    a = li.find('a')
    cat = a.get_text().strip()
    url_cat = URL_base + a['href'].replace("../", "")
    url = url_cat
    urlofbase = "https://books.toscrape.com/catalogue"
    
    books_by_category = []
    response2 = requests.get(url)
    soup3 = BeautifulSoup(response2.text, "html.parser")
    for thing_h3 in soup3.findAll('h3'):
        liste = urlofbase + thing_h3.a.get('href').replace("../../..", "")
        base_url_image="https://books.toscrape.com/"
        
        titles = thing_h3.get_text().replace("...", "")
        
        with open('categoryliste01.csv', 'a', encoding='utf8', newline='') as ff_csv:
            thewriter = csv.writer(ff_csv, delimiter=',')
            header = ['Title ', 'Links ', 'Category']
            thewriter.writerow(header)
            infos = [titles, liste, cat]
            books_by_category.append(infos)
            
            thewriter.writerows(books_by_category)
            print(infos)
           
        