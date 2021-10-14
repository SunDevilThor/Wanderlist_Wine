# Wanderlust Wine - UK
# Tutorial from John Watson Rooney YouTube channel

import requests
from bs4 import BeautifulSoup
from requests.api import head
import pandas as pd
import re

wine_list = []

# Step 1 - Request
def request(x):
    url = f'http://www.wanderlustwine.co.uk/buy-wine-online/page/{x}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


# Step 2 - Parse
def parse(soup):
    products = soup.find_all('li', class_= 'product')

    for item in products:
        name = item.find('h2', class_= 'woocommerce-loop-product__title').text
        price = item.find('span', 'woocommerce-Price-amount amount').text
    
        wine = {
            'name': name, 
            'price': price,
        }

        wine_list.append(wine)

# Step 3 - Output
def output():
    df = pd.DataFrame(wine_list)
    print(df.head())
    df.to_csv('Wanderlust-Wine.csv')

for x in range(1, 4):
    print('Getting page:', x)
    html = request(x)
    print('Parsing...')
    parse(html)

output()
print('Saved items to CSV file.')
