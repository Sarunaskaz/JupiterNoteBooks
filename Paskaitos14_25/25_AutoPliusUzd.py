import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

import time
import selenium
# import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


opcijos = Options()
# opcijos.add_argument('--incognito')
# opcijos.add_argument('--headless')

# driver = uc.Chrome(options=opcijos)
driver = webdriver.Chrome(options=opcijos)

# psl = range(2,11)



name = []
car_year = []
all_car_type = []
all_gas_type= []
all_gear_box = []
all_engine = []
all_engine_power = []
all_mileage = []
car_location = []

pslInfo = []
for x in range(1,2):
    pslInfo.append(f'https://autoplius.lt/skelbimai/naudoti-automobiliai?page_nr={x}')


for puslapis in pslInfo:
    driver.get(str(puslapis))
    time.sleep(15)

    source = driver.page_source
    bs = BeautifulSoup(source, "html.parser")
    ResultsSet = bs.find_all('div', {'class':'announcement-body'})



    for skelbimas in ResultsSet:
        try:            
            pavadinimas = skelbimas.find('div', {'class': 'announcement-title'}).text.strip()
            name.append(pavadinimas)
            pagaminimo_data = skelbimas.find('div', {'class': 'announcement-parameters'}).text.strip()[:4]
            car_year.append(pagaminimo_data)
            
            masinos_duomenys = skelbimas.find('div', {'class':'announcement-parameters-block'}).find('div', {'class': 'announcement-parameters'}).text.strip().replace('\n', ';').replace('   ', '').split(';')
            
            all_gas_type.append(masinos_duomenys[0])
            all_gear_box.append(masinos_duomenys[1])
            all_engine.append(masinos_duomenys[2])
            all_engine_power.append(masinos_duomenys[3])
            all_mileage.append(masinos_duomenys[4])
            car_location.append(masinos_duomenys[5])
           

            print(masinos_duomenys)
            # print(masinos_duomenys[1])
            # print(masinos_duomenys[2])
            # print(masinos_duomenys[3])
            # print(masinos_duomenys[4])
            # print(masinos_duomenys[5])

            print('-------------------kitas------------------------')
        except Exception as klaida:
            print(klaida)

df = pd.DataFrame() # Tuscio data frame sukurimas
df['Name'] = name # musu tektas csv faile
df['Year'] = car_year
# df['Car_type'] = all_car_type
df['Gear_box'] = all_gear_box
df['Gas_type'] = all_gas_type
df['Engine'] = all_engine
df['Engine_pwoer'] = all_engine_power
df['Mileage'] = all_mileage
df['Location'] = car_location
df.to_csv('AutoPliusUzd.csv', sep=';') # 

driver.close()

