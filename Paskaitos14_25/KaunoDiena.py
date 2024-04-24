import selenium
import undetected_chromedriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

import time # dėl sleep komandos


opcijos = Options()
opcijos.add_argument('--incognito')

driver = uc.Chrome(options=opcijos)

url = "https://www.kaunodiena.lt"

driver.get(url)
time.sleep(3)

source = driver.page_source # pasiimam puslapio html kodą

bs = BeautifulSoup(source, 'html.parser')
ResultSet = bs.find_all('a', {'class': 'articles-list-title'})
print(ResultSet)

# for elementas in ResultSet:
#     # print("----------------------")
#     # print(elementas['href'])  # Taip galime pasiekti class'es ir puslapiu nuorodas ['href']
#     # print(elementas.text) # Taip pasiekeme elemento pav, Siuo atveju randame antrasciu pavadinimus

pavadinimai = []
for elementas in ResultSet:
    pavadinimai.append(elementas.text)


df = pd.DataFrame() # Tuscio data frame sukurimas
df['Pavadinimai'] = pavadinimai # musu tektas csv faile
df.to_csv('KaunoDiena.csv', sep=',') # 
driver.close()

