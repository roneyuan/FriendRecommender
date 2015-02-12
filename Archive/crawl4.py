## When upload to server, it is important to set the path to #!/home4/chenlin/public_html/friendrecommendations.com/env/bin/python
## It is because I set the library in the this folder for requests and beautifulSoup


import requests
from bs4 import BeautifulSoup
import re


def trade_spider(max_pages):
    ## Make the empty list for title, content, and user id
    titleArray = []
    contentArray = []
    useridArray = []
    personinfoArray = []

    page = 1
    while page <= max_pages:
        url = 'http://newyork.craigslist.org/search/w4m'
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)

        for dataId in soup.findAll('a', {'class': 'hdrlnk'}):

            userid = dataId.get('data-id')
            #print userid
            href = dataId.get('href')
            #print href
            title = dataId.string
            #print title

            link = "http://newyork.craigslist.org/" + href
            ContentAndAge = get_single_item_data(link)
            content = ContentAndAge[0]
            personinfo = ContentAndAge[1]

            #print content


            titleArray.append(title)
            contentArray.append(content)
            useridArray.append(userid)
            personinfoArray.append(personinfo)

        page += 1

    #print useridArray
    #print titleArray
    #print contentArray
    #print ageArray
    return titleArray, contentArray, useridArray, personinfoArray


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

    personinfo = data[3]

    # make to the dictionary
    dict1 = dict(zip(userid, title))
    dict2 = dict(zip(userid, content))
    dict3 = dict(zip(userid, personinfo))

    return dict1, dict2, dict3



def Algorithm_Age(age, dictionary):
    # Take the first dictionary out
    d = dictionary[2]
    recommend_age = []

    # This loop will seperate all the words out and store to the list
    for key in d:
        title = d[key]
        wordList = re.sub("[^\w]", " ", title).split()
        # find if the age is matched
        for word in wordList:
            if age == word:
                recommend_age.append(key)
    # print "Based on your age, the recommended friends are", recommend_age
    print recommend_age
    return recommend_age

def Algorithm_relationship(relationship, dictionary):
    d = dictionary[1]  # Choose from content
    recommend_relationship = []
    if relationship == "Yes":
        match = "relationship"
        for key in d:
            content = d[key]
            wordList = re.sub("[^\w]", " ", content).split()
            for word in wordList:
                if match == word:
                    recommend_relationship.append(key)

    print recommend_relationship
    return recommend_relationship

def Algoirhtm_best(recommend_age, recommend_relationship):
    # if age and location have same user, match will be true
    #match = (set(recommend_age) == set(recommend_location))
    count = 1
    count2 = 1
    #if match:
    #	best = list(set(recommend_age) & set(recommend_location))
    #	if len(best) > 0:

    for userid in recommend_age:

        if userid in recommend_relationship:
            match = userid
            print "There is best recommendation for you! (The user also wants a relationship and both of you have same age.)"
            print """<html><p><a href="http://newyork.craigslist.org/jsy/m4w/%s.html"> <input type="button" value ="Get your best match!"></a></html>""" %match




if __name__ == "__main__":
    data = trade_spider(1)
    #print data
    dictionary = makeDictionary(data)
    recommend_age = Algorithm_Age("30", dictionary)
    recommend_relationship = Algorithm_relationship("Yes", dictionary)
    Algoirhtm_best(recommend_age, recommend_relationship)
