import requests
from bs4 import BeautifulSoup
import re

def trade_spider(max_pages):
    ## Make the empty list for title, content, and user id
    titleArray = []
    contentArray = []
    useridArray = []
    attrsArray = []
    hrefArray = []
    ageArray = []
    locationArray = []
    districtArray = []

    url = 'http://newyork.craigslist.org/search/w4m'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)

    for dataId in soup.findAll('span', {'class': 'txt'}):

        href = dataId.find('a', {'class': 'hdrlnk'})['href']
        userid = dataId.find('a', {'class': 'hdrlnk'})['data-id']
        title = dataId.find('a', {'class': 'hdrlnk'}).string

        if dataId.find('span', {'class': 'price'}) == None:
            age = "null"
        else:
            age = dataId.find('span', {'class': 'price'}).text

        if dataId.find('small') == None:
            location = "null"
        else:
            location = dataId.find('small').string

        district = href[1:4]

        link = "http://newyork.craigslist.org/" + href
        Content = getContent(link)
        content = Content[0]
        attrs = Content[1]

        titleArray.append(title)
        useridArray.append(userid)
        hrefArray.append(href)
        ageArray.append(age)
        locationArray.append(location)
        districtArray.append(district)
        contentArray.append(content)
        attrsArray.append(attrs)

    return titleArray, useridArray, hrefArray, ageArray, locationArray, districtArray, contentArray, attrsArray

def getContent(url):

    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    content = ""
    attrs = ""

    for data in soup.findAll('section', {'class': 'userbody'}):
        content = data.find('section', {'id': 'postingbody'}).text
        attrs = data.find('div', {'class': 'mapAndAttrs'}).text

    return content, attrs

def makeDictionary(data):

    title = data[0]
    userid = data[1]
    href = data[2]
    age = data[3]
    location = data[4]
    district = data[5]
    content = data[6]
    attrs = data[7]

    # make to the dictionary
    dict1 = dict(zip(userid, title))
    dict2 = dict(zip(userid, content))
    dict3 = dict(zip(userid, age))
    dict4 = dict(zip(userid, href))
    dict5 = dict(zip(userid, attrs))
    dict6 = dict(zip(userid, location))
    dict7 = dict(zip(userid, district))

    return dict1, dict2, dict3, dict4, dict5, dict6, dict7


def splitDict(words, dictionary):

    matchedId = []
    for dict in dictionary:
        content = dictionary[dict]
        wordList = re.sub("[^\w]", " ", content).split()
        if words in wordList:
            matchedId.append(dict)

    return matchedId

def recommendation(InputLocation, InputDistrict, InputAge, InputRelationship, InputInterest, InputAnykeywords, dictionary):

    locationList = splitDict(InputLocation, dictionary[5])
    districtList = splitDict(InputDistrict, dictionary[6])
    ageList = splitDict(InputAge, dictionary[2])
    relationshipList = splitDict(InputRelationship, dictionary[1])
    interestList = splitDict(InputInterest, dictionary[1])
    anykeywordsList = splitDict(InputAnykeywords, dictionary[1])

    # if set(locationList) & set(districtList):
    #     LandD = list(set(locationList) & set(districtList))
    # if set(relationshipList) & set(interestList):
    #     RandI = list(set(relationshipList) & set(interestList))

    a = set(locationList) ^ set(districtList) ^ set(ageList) - (set(locationList) & set(districtList) & set(ageList))
    b = a ^ set(relationshipList) ^ set(interestList) - (a & set(relationshipList) & set(interestList))
    c = b ^ set(anykeywordsList)
    d = set(locationList) | set(districtList) | set(ageList) | set(relationshipList) | set(interestList) | set(anykeywordsList)
    e = d - c

    matchList = list(e)

    # if (set(locationList) | set(districtList) | set(ageList)) - (set(locationList) ^ set(districtList) ^ set(ageList)):
    #     returnText1 = "You may have same location and age"
    # else:
    #     returnText1 = "null"
    #
    # if (set(relationshipList) | set(interestList) | set(anykeywordsList)) - (set(relationshipList) ^ set(interestList) ^ set(anykeywordsList)):
    #     returnText2 = "You may have same relationship, interest or keyword"
    # else:
    #     returnText2 = "null"

    return matchList, locationList, districtList, ageList, relationshipList, interestList, anykeywordsList

    # bestMatchList = []
    # secondMatchList = []
    # thirdMatchList = []
    # forthMatchList = []
    # fifthMatchList = []

def printOut(getRecommend, href):
    print getRecommend
    print href[getRecommend[0][1]]
    print """
		<html>
		<head>
			<title>Get your best recommendation!</title>
			<meta charset="utf-8" />
			<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
			<meta name="viewport" content="width=device-width, initial-scale=1" />
			<link href="css/bootstrap.min.css" rel="stylesheet">
		</head>
		<body>
			<div class="navbar navbar-inverse">
					<div class="container">
						<div class="navbar-header">
							<a href="" class="navbar-brand"> Welcome to the FriendRecommender ! </a>
							<button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
							<span class="sr-only">Toggle navigation</span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							<span class="icon-bar"></span>
							</button>
						</div>

						<div class="collapse navbar-collapse">
							<ul class="nav navbar-nav">
								<li><a href="home.html">Home</a></li>
								<li><a href="aboutus.html">About Us</a></li>
								<li><a href="project.html">Project Description</a></li>
								<li class="active"><a href="BasicInfo">Demo</a></li>
							</ul>

						</div>
					</div>
			</div>

			<div class = "container">
				<h1>The best recommendation:</h1>
			</div>

			<div class = "top"></div>

			<div class="container">
			    <div class="fb-like" data-href="http://friendrecommendations.com/" data-layout="standard" data-action="like" data-show-faces="true" data-share="true"></div>
			</div>
			<!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
			<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
			<!-- Include all compiled plugins (below), or include individual files as needed -->
			<script src="js/bootstrap.min.js"></script>

		</body>
		</html>

		<div id="fb-root"></div>
		<script>
		(function(d, s, id) {
		    var js, fjs = d.getElementsByTagName(s)[0];
		    if (d.getElementById(id)) return;
		    js = d.createElement(s); js.id = id;
		    js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=1495984630617535&version=v2.0";
		    fjs.parentNode.insertBefore(js, fjs);
		} (document, 'script', 'facebook-jssdk'));
		</script>
	"""

if __name__ == "__main__":

    data = trade_spider(2)
    #print data
    dictionary = makeDictionary(data)
    getRecommend = recommendation("", "mnh", "28", "relationship", "sex", "", dictionary)
    printOut(getRecommend, dictionary[3])
    #splitDict(dictionary[1])
    #print dictionary