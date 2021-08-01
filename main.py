from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import csv

bright_stars_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'

page = requests.get(bright_stars_url, verify=False)
print(page)

soup = bs(page.text,'html.parser')
star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')

def scrape():
    headers = ["Name","Distance","Mass","Radius"]
    stars_data= []
    for tr_tag in table_rows:
        td_tags = tr_tag.find_all("td")
        for index, td_tags in enumerate(td_tags):
            if index == 1:
                temp_list.append(td_tags.find_all("a")[1].contents[0])
            else:
                temp_list.append(td_tags.contents[0])
        stars_data.append(temp_list)
    with open("scrapper_2.csv", "w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(stars_data)