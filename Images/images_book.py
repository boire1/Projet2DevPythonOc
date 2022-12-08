from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import csv
from csv import writer
import os
import requests 
import shutil 


all_book=[]

pages=range(1,51)
for page in pages:
    response= requests.get('http://books.toscrape.com/catalogue/page-' + str(page) + '.html')
   

    # page = requests.get(url)
    soup= BeautifulSoup(response.text,"html.parser")

   
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
    
        link_image = book_soup.find("div", {"class": "item active"}).find("img")
        
        image_url = base_url_image + link_image['src'].replace("../", '')
        image_alt= base_url_image + link_image['alt'].replace("../", '')
        
        image_alt=image_alt[27:]

        filename = image_url.split("/")[-1]
        print(type(filename))
        filename=filename[-4:]
        
        name_mg=image_alt
        filename=image_alt+filename
      
        r = requests.get(image_url, stream = True)
        
        if r.status_code == 200:
            r.raw.decode_content = True
            
        try:    
            with open("Images/"+filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                
            print('Image telecharger avec sucess: ',filename)
        except:    
                print('Image ne peut être telecharger')    
                
        print(filename)        
                
        book ={"Title":title,            
            "Image":image_url,
            }
        all_book.append(book)
        
        info=[title,image_url]
    
 


    
    
    
    
