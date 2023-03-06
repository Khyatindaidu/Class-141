from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import csv

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

stars_data = []

def scrape():
    headers = ['Name', 'Distance', 'Mass', 'Radius']
    soup = BeautifulSoup(browser.page_source, "html.parser")

    for ul_tag in soup.find_all('ul',attrs={"class", "expoplanet"}):
        li_tags = ul_tag.findall("li")
        temp_list=[]

        for index,li_tag in enumerate(li_tags):

            if index == 0:
                temp_list.append(li_tag.find_all("a")[0].contents[0])
            else:
                try:
                    temp_list.apend(li_tag.content[0])
                except:
                    temp_list.append('')
        stars_data.append(temp_list)
        
print(stars_data[1])

    
scrape()

# Define Header
headers = ["name", "light_years_from_earth", "planet_mass", "stellar_magnitude", "discovery_date"]

# Define pandas DataFrame   
star_df_1 = pd.DataFrame(stars_data,column = headers)

# Convert to CSV
star_df_1.to_csv('scraped.csv', index= True, index_label ='id')

