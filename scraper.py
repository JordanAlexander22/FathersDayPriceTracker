import requests
from bs4 import BeautifulSoup

# URL to scrape for price monitoring

URL= 'https://www.golfgalaxy.com/p/callaway-mavrik-driver-19cwymmvrkdrhlm40drv/19cwymmvrkdrhlm40drv'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36' }

page = requests.get(URL, headers= headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())
