import requests
import time
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

counter = 0
shipsDate = []
for i in range(1,1000):
    quote_page = f"https://archiveofourown.org/tags/Harry%20Potter%20-%20J*d*%20K*d*%20Rowling/works?commit=Sort+and+Filter&page={i}&utf8=%E2%9C%93&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=F&work_search%5Bdate_from%5D=&work_search%5Bdate_to%5D=&work_search%5Bexcluded_tag_names%5D=&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=revised_at&work_search%5Bwords_from%5D=&work_search%5Bwords_to%5D="


    #quote_page = f"https://archiveofourown.org/tags/Percy%20Jackson%20and%20the%20Olympians%20*a*%20Related%20Fandoms%20-%20All%20Media%20Types/works?commit=Sort+and+Filter&page={i}&utf8=%E2%9C%93&work_search%5Bcomplete%5D=&work_search%5Bcrossover%5D=F&work_search%5Bdate_from%5D=&work_search%5Bdate_to%5D=&work_search%5Bexcluded_tag_names%5D=&work_search%5Blanguage_id%5D=&work_search%5Bother_tag_names%5D=&work_search%5Bquery%5D=&work_search%5Bsort_column%5D=revised_at&work_search%5Bwords_from%5D=&work_search%5Bwords_to%5D="
    t0 = time.time()
    time.sleep(10)
    counter += 1
    if counter == 10:
        print('moving along')
        counter = 0
    page = requests.get(quote_page)
    response_delay = time.time() - t0
    soup = BeautifulSoup(page.content, "html.parser")
    
    date = soup.find('p', attrs={'class': 'datetime'})
    date = date.text.strip()
    
    ships = soup.find_all('li', attrs={'class': 'relationships'})
    
    shipsList = []
    for i in range(0,len(ships)):
        shipsList.append(ships[i].text.strip())

    for i in shipsList:
        shipsDate.append([i,date])

df = pd.DataFrame(shipsDate, columns= ["Ship","Date"])
df.to_csv('HarryPotterFF.csv')
