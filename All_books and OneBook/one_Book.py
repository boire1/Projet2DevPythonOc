from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import csv
from csv import writer


np.arange(1,10)

# all_book=[]

pages=np.arange(1,2)

for page in pages:
#     pages_to_scrape +=1
    url="http://books.toscrape.com/catalogue/page-"+str(page) +'.html'
    
    page = requests.get(url)
    soup= BeautifulSoup(page.text,"html.parser")

    links = []
    listings= soup.find_all(class_="product_pod")
    for listing in listings:
        book_link= listing.find("h3").a.get("href")
        base_url ="https://books.toscrape.com/catalogue/"
        base_url_image="https://books.toscrape.com/"
        complete_link = base_url + book_link
        links.append(complete_link)
 
    for link in links:
        response = requests.get(link).text
        book_soup = BeautifulSoup(response,"html.parser")
        
        title = book_soup.find(class_="col-sm-6 product_main").h1.text.strip()
    
        price = book_soup.find(class_="col-sm-6 product_main").p.text.strip()[1:]
        stock = book_soup.find(class_="instock availability").text.strip()
        
        book_rating=book_soup.find("p", class_="star-rating").attrs.get("class")[1]
       
        product_description = book_soup.find("div", {"id": "product_description"}).find_next("p").get_text()
      
        category=book_soup.find('ul',class_="breadcrumb").find_next('a')
        
        categorie_1=category.find_next('a')
        categorie_ok=categorie_1.find_next('a')
        catego_book=categorie_ok.get_text().strip()
       
        info=[title,catego_book]
       
        link_image = book_soup.find("div", {"class": "item active"}).find("img")

        image_url = base_url_image + link_image['src'].replace("../", '')
        
        tableau_book=book_soup.find("table",{"class":"table table-striped"})
    
        tableau_book_clean=tableau_book.text
        tab_bk_UPC=(tableau_book.text[5:21] )
   
        bk_price_excl_tva=(tableau_book.text[62:68])
        bk_price_incl_tva=(tableau_book.text[89:95])
         
        tableau_reviews=(tableau_book_clean[167:180]).strip()
        tableau_tax=(tableau_book_clean[103:107]).strip()
        
        # book ={"Title":title,
        #     "N°Upc":tab_bk_UPC,
        #     "Category":catego_book,
        #     "Price":price,
        #     "Reviews":tableau_reviews,
        #     "Available":stock,
        #     "(Price exl tva)":bk_price_excl_tva,
        #     "(Price inc tva)":bk_price_incl_tva,
        #     "Image":image_url,
        #     "Rating":book_rating,
        #     "Description":product_description}
        
        # all_book.append(book)
        
with open('one_Book_01.csv', 'w', encoding='utf8', newline='') as ff_csv:
    thewriter = csv.writer(ff_csv, delimiter=',')
    header=['Title ','Num_Upc ','Category ','Price', 'Reviews', 'Available', '(Price exl tva)',
            'Tax','(Price inc tva)','Image Link','Rating ','book link', 'Description']
    thewriter.writerow(header)
    
    info=[title,tab_bk_UPC,catego_book,price,
          tableau_reviews,stock,bk_price_excl_tva,tableau_tax,bk_price_incl_tva,image_url,book_rating,complete_link,product_description]
    thewriter.writerow(info)
   