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

psl = range(2,11)


pslInfo = []
for x in psl:
    pslInfo.append(f'https://www.aruodas.lt/butai/puslapis/{x}/')

# url = [x for x in pslInfo]
Busto_adresas = []
Busto_kaina = []
Busto_kaina_uzKV = []
Busto_plotas = []
Busto_kamb_sk = []

for puslapis in pslInfo:
    driver.get(str(puslapis))
    time.sleep(15)

    source = driver.page_source
    bs = BeautifulSoup(source, "html.parser")
    ResultsSet = bs.find_all('div', {'class':'advert-flex'})
    # print(len(ResultsSet))


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

            plotas1 = skelbimas.find('div', {"class": "list-AreaOverall-v2 list-detail-v2"})
            plotas2 = plotas1.contents

            kamb = skelbimas.find('div', {"class": "list-RoomNum-v2 list-detail-v2"})
            kambarys1 = kamb.contents
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

            g = ''
            for i in plotas2:
                g = g + str(i).strip() # str - kad garantuotai būtų tekstas
            plotas = g.replace('<br/>', ', ') #.replace(' ', '')

            z = ''
            for i in kambarys1:
                z = z + str(i).strip() # str - kad garantuotai būtų tekstas
            kambarys = z.replace('<br/>', ', ') #.replace(' ', '')

            # tuo tarpu .text gražina contents tekstą kaip vientisą
            # tekstas = tag.text.strip() # string metodas, skirtas pašalinti tarpus iš pradžios bei pabaigos
            # print("====SKELBIMAS====")
            # print(f'Adresas: {adresas}"\n"Buto kaina: {kaina1}"\n"Kaina uz kvadaratini metra: {kainaUzKV[:5]} €/m² "\n"Busto plotas: {plotas}"\n"Kambariu skaicius: {kambarys}')

            Busto_adresas.append(adresas)
            Busto_kaina.append(kaina1)
            Busto_kaina_uzKV.append(kainaUzKV[:5])
            Busto_plotas.append(plotas)
            Busto_kamb_sk.append(kambarys)

        except:
            pass

df = pd.DataFrame() # Tuscio data frame sukurimas
df['Adresas'] = Busto_adresas # musu tektas csv faile
df['Kaina'] = Busto_kaina
df['KainaKV'] = Busto_kaina_uzKV
df['plotas'] = Busto_plotas
df['KambariuSk'] = Busto_kamb_sk
df.to_csv('AruodasUzd.csv', sep=';') # 
driver.close()


#surinkite iš puslapių nuo 2 iki 11-to butų skelbimus ir tokią informaciją - kaina, kaina už 1 kv metrą, adresas, plotas, kambarių kiekis. 
# šiuos duomenis eksportuokite į csv failą, skirtukas turi būti ;.
#suraskite, kiek iš atrinktų butų buvo pagal kainą pigūs, brangūs, neįperkami. Kriterijus - 1 kv metro kaina iki 1 VDu - pigūs, iki 3 VDU - brangūs, daugiau nei 3 VDU - neįperkami.
#pavaizduokite su boxplotais kainų už 1 kv pasiskirstymą nuo kambarių skaičiaus.
#Pavaizduokiet tokią informaciją: atrinktų butų kainų pasiskirstymą tarp miestų.
#pavaizduokite tokią informaciją - kiek buvo sklebimų per skirtingus miestus jūsų atrankoje?