from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

from Domain.Website import Website

from Repository.file_repository import FileRepository

class WebsiteService:
    def __init__(self, website_repository: FileRepository):
        self.__website_repository = website_repository

    def get_all(self):
        return self.__website_repository.get_all()

    def add(self,url,classes):
        website = Website(url,classes)
        self.__website_repository.add(website)

    def scrap(self):
        driver = webdriver.Firefox()
        products=[]
        prices=[]
        ratings=[]
        websites = self.get_all()
        for website in websites:
            driver.get(website.url)

            content = driver.page_source
            soup = BeautifulSoup(content,features="html.parser")

            for div in soup.find_all('div',class_=website.classes[0]):

                name = div.find('div',class_=website.classes[1])
                price = div.find('div',class_=website.classes[2])
                rating = div.find('span',class_=website.classes[3])
                products.append(name.text)
                prices.append(price.text)
                if(rating):
                    ratings.append(len(list(rating.descendants)))
                else:
                    ratings.append(0)

        df = pd.DataFrame({'Product Name':products,'Price':prices,'Rating':ratings})
        df.to_csv('products.csv', index=False, encoding='utf-8')
