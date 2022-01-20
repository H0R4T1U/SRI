from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

from Domain.website import Website
from selenium.webdriver.firefox.options import Options

from Repository.file_repository import FileRepository


class WebsiteService:
    def __init__(self, website_repository: FileRepository):
        self.__website_repository = website_repository

    def get_all(self):
        return self.__website_repository.get_all()

    def add(self,name, url, container_class, classes):
        website = Website(name,url, container_class, classes)
        self.__website_repository.add(website)

    def get_files_from_file(self):
        self.__website_repository.read_file()

    def scrap(self):
        options = Options()
        options.headless = True

        driver = webdriver.Firefox(options=options)

        websites = self.get_all()
        for website in websites:
            data = {}
            df = pd.DataFrame()
            driver.get(website.url)

            content = driver.page_source
            soup = BeautifulSoup(content, features="html.parser")

            for div in soup.find_all('div', class_=website.container_class):
                for ScrapedClass in website.classes:
                    try:
                        data[f"{ScrapedClass}"] = div.find('div', class_=ScrapedClass).text
                    except:
                        data[f"{ScrapedClass}"] = "null"
                    df = df.append(data, ignore_index=True)

            df.to_csv(f'{website.name}.csv', index=False, encoding='utf-8')

        driver.quit()