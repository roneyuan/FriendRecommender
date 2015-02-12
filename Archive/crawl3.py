## When upload to server, it is important to set the path to #!/home4/chenlin/public_html/friendrecommendations.com/env/bin/python
## It is because I set the library in the this folder for requests and beautifulSoup


import requests
from bs4 import BeautifulSoup


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

    #print useridArray
    #print titleArray
    #print contentArray
    return titleArray, contentArray, useridArray


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

def makeDictionary(data):
    # Make dictionary for userid:title and userid:content

    dict1 = {}
    dict2 = {}

    userid = []
    title = []
    content = []

    # data[0] = title from readExcelfile()
    title = data[0]
    # Start from second row because first row is the name of title
    #title = title[1:]

    # data[1] = content from readExcelfile()
    content = data[1]
    # Start from second row because first row is the name of content
    #content = content[1:]

    # data[2] = user id from readExcelfile()
    # get rid of "post id: " so do row[9:] and start from second row
    # because first row is the name of user id
    #for row in data[2]:
    #    userid.append(row[9:])
    #userid = userid[1:]

    userid = data[2]
    # data1 = userid,title

    # make to the dictionary
    dict1 = dict(zip(userid, title))
    dict2 = dict(zip(userid, content))

    return dict1, dict2




if __name__ == "__main__":
    data = trade_spider(1)
    #print data
    dictionary = makeDictionary(data)
    print dictionary

##############################################################################################
    #dictionary = makeDictionary(data)

    #print dictionary


# def makeDictionary(data):
#     # Make dictionary for userid:title and userid:content
#
#     dict1 = {}
#     dict2 = {}
#     userid = []
#     title = []
#     content = []
#
#     # data[0] = title from readExcelfile()
#     title = data[0]
#     # Start from second row because first row is the name of title
#     #title = title[1:]
#
#     # data[1] = content from readExcelfile()
#     content = data[1]
#     # Start from second row because first row is the name of content
#     #content = content[1:]
#
#     # data[2] = user id from readExcelfile()
#     # get rid of "post id: " so do row[9:] and start from second row
#     # because first row is the name of user id
#     #for row in data[2]:
#     #    userid.append(row[9:])
#     #userid = userid[1:]
#
#     userid = data[2]
#     # data1 = userid,title
#
#     # make to the dictionary
#     dict1 = dict(zip(userid, title))
#     dict2 = dict(zip(userid, content))
#
#     return dict1, dict2




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

    #return titleArray, contentArray, useridArray
