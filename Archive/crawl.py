import requests
from bs4 import BeautifulSoup


def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://newyork.craigslist.org/search/w4m'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('p', {'class': 'row'}):
            id = link.get('data-pid')
            print id
        for dataId in soup.findAll('a', {'class': 'i'}):
            age = dataId.string
            href = "http://newyork.craigslist.org/" + dataId.get('href')
        #title = soup.findAll('a', {'data-id': id})
            print href
            print age


            #print title
        page += 1


trade_spider(1)