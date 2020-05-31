import requests
from bs4 import BeautifulSoup

# URL to scrape for price monitoring

URL= 'https://www.dickssportinggoods.com/p/callaway-mavrik-driver-19cwymmvrkdrhlm40drv/19cwymmvrkdrhlm40drv'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36' }

page = requests.get(URL, headers= headers)

soup1 = BeautifulSoup(page.content, 'html.parser')

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

#print(soup.prettify()) to for sanity check

price = soup2.find('span', {'class': "product-price ng-star-inserted"}).get_text().strip()  #necessary steps to parse through javascript as html
title = soup2.find('h1', {'class': "title"}).get_text()

#print(price.strip())

#need to convert price to a number rather than a string

converted_price = price[1:7]

print(converted_price)



