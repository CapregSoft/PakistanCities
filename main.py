from typing import List, Any

import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get(r"https://en.wikipedia.org/wiki/List_of_populated_places_in_Punjab_(Pakistan)")
# https://en.wikipedia.org/wiki/List_of_populated_places_in_Punjab_(Pakistan)
# https://en.wikipedia.org/wiki/List_of_cities_in_Gilgit_Baltistan

soup = BeautifulSoup(res.text, "html.parser")

rows = soup.find_all("tr")

dumps=[]
city={}
cities=[]
districts=[]

# print(res.text)

for row in rows:
    tds = row.find_all('td')
    i = 0
    for td in tds:
        if "edit" not in td.text:
            # print(td.text)
            if(i==2):
                districts.append(td.text)
        i=i+1
districts=list(dict.fromkeys(districts))

for district in districts:
    city_td = []
    for row in rows:
        tds = row.find_all('td')
        i = 0
        name=""
        type=""
        district_td=""
        for td in tds:
            if "edit" not in td.text:
                if(i==0):
                    name=td.text
                if(i==1):
                    type=td.text
                if i==2:
                    district_td=td.text
            if(district==district_td):
                city={"name":name,"type":type};
                city_td.append(city)
            i=i+1
    districtCities = {"name": district,"cities":city_td}
    dumps.append(districtCities)
    cities.append(city_td)
        
import json
with open('punjab.json', 'w') as fp:
    json.dump(dumps, fp)


