from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Firefox()

products=[]
prices=[]
ratings=[]
driver.get("https://www.pcgarage.ro/notebook-laptop/")

content = driver.page_source
soup = BeautifulSoup(content)

for div in soup.find_all('div',class_='product_box'):
    
    name = div.find('div',class_='product_box_name')
    price = div.find('div',class_='pb-price')
    rating = div.find('span',class_='rating_container')
    products.append(name.text)
    prices.append(price.text)
    if(rating):
        ratings.append(len(list(rating.descendants)))
    else:
        ratings.append(0)

df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings}) 
df.to_csv('products.csv', index=False, encoding='utf-8')