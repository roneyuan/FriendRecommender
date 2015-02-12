## When upload to server, it is important to set the path to #!/home4/chenlin/public_html/friendrecommendations.com/env/bin/python
## It is because I set the library in the this folder for requests and beautifulSoup


import requests
from bs4 import BeautifulSoup
import cgitb;cgitb.enable()


def trade_spider(max_pages):

    ## Make the empty list for title, content, and user id
    titleArray = []
    contentArray = []
    useridArray = []

    page = 1
    while page <= max_pages:
        url = 'http://newyork.craigslist.org/search/w4m'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        #for link in soup.findAll('p', {'class': 'row'}):
        #    id = link.get('data-pid')
            #print id
        for dataId in soup.findAll('a', {'class': 'hdrlnk'}):
            #age = dataId.string
            userid = dataId.get('data-id')
            #print userid
            href = dataId.get('href')
            #print href
            title = dataId.string
            #print title

            link = "http://newyork.craigslist.org/" + href
            ContentAndAge = get_single_item_data(link)
            content = ContentAndAge[0]
            age = ContentAndAge[1]
            #print content
            #print age

            titleArray.append(title)
            contentArray.append(content)
            useridArray.append(userid)




            #href = "http://newyork.craigslist.org/" + dataId.get('href')
        #title = soup.findAll('a', {'data-id': id})
            #print href
            #print age
            #get_single_item_data(href)


            #print title
        page += 1

    print useridArray[3]
    print titleArray[3]
    print contentArray[3]



    #page = 1
    # while page <= max_pages:
    #     url = 'http://newyork.craigslist.org/search/w4m'
    #     source_code = requests.get(url)
    #     plain_text = source_code.text
    #     soup = BeautifulSoup(plain_text)
    #     for link in soup.findAll('p', {'class': 'row'}):
    #         id = link.get('data-pid')
    #         #print id
    #     for dataId in soup.findAll('a', {'class': 'i'}):
    #         age = dataId.string
    #         href = "http://newyork.craigslist.org/" + dataId.get('href')
    #     #title = soup.findAll('a', {'data-id': id})
    #         #print href
    #         #print age
    #         get_single_item_data(href)
    #
    #
    #         #print title
    #     page += 1


def get_single_item_data(item_url):
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    content = ""
    age = ""
    for item_name in soup.findAll('section', {'id': 'postingbody'}):
        content = item_name.text
        #print(content)
    for item_name2 in soup.findAll('span', {'class': 'personals_attrbubble personals_physical'}):
        age = item_name2.text
        #print age

    return content, age


trade_spider(1)