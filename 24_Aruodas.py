#!/bin/python3

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

url = "https://www.aruodas.lt/butai/puslapis/2/"

driver.get(url)
time.sleep(15)

source = driver.page_source
bs = BeautifulSoup(source, "html.parser")
ResultsSet = bs.find_all('div', {'class':'advert-flex'})


# for ciklas,  eiliskumas:
# 1) susirandam per web inspect klase kuria norim issiWebscrapint(pasiimti norima info)
# 2) Tag vietoje einam giliau ir pasitikslinam norima info
# 3) Prisiskiriam linko taga, kad spausdintu hyperlink norimos info
# 4) su 'contents' metodu gaunam objekta teksto gabalais, jeigu butu su 'text' grazintu teksta kaip vientisa
# 5) pasidarom dar vien 'for' cikla, kad pereitu dar karta per teksta ir panaudojus metoda 'strip', kad panaikintu tarpus is pradzios ir pabaigos.
# 6) Kintamasis 'adresas' reikalingas, kad pakeistu <br/> i tarpa su kableliu. 

for skelbimas in ResultsSet:
    try:
        addres_element  = skelbimas.find('div', {'class':'list-adress-v2'})
        tag = addres_element.find('h3').find('a', href=True)
        linkas = tag['href']

        kaina = addres_element.find('div', {"class": "price"})
        tag1 = kaina.find('span')
        PilnaKaina = tag1.contents
        
        kainaKV = addres_element.find('div', {"class": "price"})
        Kv = kainaKV.find('span', {'class' : 'price-pm-v2'})
        PilnaKainaUzKV = Kv.contents
        # tekstą galima pasiekti ir per 
        # .contents atributą
        tekstas = tag.contents #jums gražina list objektą su teksto gabalais
        f = ''
        for i in tekstas:
            f = f + str(i).strip() # str - kad garantuotai būtų tekstas
        adresas = f.replace('<br/>', ', ')
        
        d = ''
        for i in PilnaKaina:
            d = d + str(i).strip() # str - kad garantuotai būtų tekstas
        kaina1 = d.replace('<br/>', ', ')

        c = ''
        for i in PilnaKainaUzKV:
            c = c + str(i).strip() # str - kad garantuotai būtų tekstas
        kainaUzKV = c.replace('<br/>', ', ') #.replace(' ', '')

        # tuo tarpu .text gražina contents tekstą kaip vientisą
        # tekstas = tag.text.strip() # string metodas, skirtas pašalinti tarpus iš pradžios bei pabaigos
        print("====SKELBIMAS====")
        print(f'{linkas} "\n"{adresas}"\n" {kaina1}"\n" {kainaUzKV[:5]} €/m²')
    except:
        pass

# Jūsų užduotis:
# Iš printinti linką, adresą, buto kainą, buto kainą už 1 kv metrą, vaizdas turi būti toks:
# ===SKELBIMAS===
# linkoas,
# adreas
# kaina
# kaina už 1 kv metrą



driver.close()