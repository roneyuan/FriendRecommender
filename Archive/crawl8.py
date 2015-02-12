## When upload to server, it is important to set the path to #!/home4/chenlin/public_html/friendrecommendations.com/env/bin/python
## It is because I set the library in the this folder for requests and beautifulSoup


import requests
from bs4 import BeautifulSoup
import re

print "Content-type: text/html\r\n\r\n"
print ""

def trade_spider(max_pages):
    ## Make the empty list for title, content, and user id
    titleArray = []
    contentArray = []
    useridArray = []
    personinfoArray = []
    hrefArray = []

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
            hrefArray.append(href)


        page += 1

    #print useridArray
    #print titleArray
    #print contentArray
    #print ageArray
    #print hrefArray
    #print personinfoArray
    return titleArray, contentArray, useridArray, personinfoArray, hrefArray


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

    #dict1 = {}
    #dict2 = {}

    #userid = []
    #title = []
    #content = []

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
    #print userid
    personinfo = data[3]
    #print personinfo

    href = data[4]

    # make to the dictionary
    dict1 = dict(zip(userid, title))
    dict2 = dict(zip(userid, content))
    dict3 = dict(zip(userid, personinfo))
    dict4 = dict(zip(userid, href))
    #print dict1
    #print dict2
    #print dict3
    return dict1, dict2, dict3, dict4



def Algorithm_Age(age, dictionary):
    # Take the first dictionary out
    d = dictionary[2]
    recommend_age = []
    #print d
    # This loop will seperate all the words out and store to the list
    for key in d:
        title = d[key]
        wordList = re.sub("[^\w]", " ", title).split()
        # find if the age is matched
        for word in wordList:
            if age == word:
                recommend_age.append(key)
        #print wordList
    # print "Based on your age, the recommended friends are", recommend_age
    #print recommend_age
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

    #print recommend_relationship
    return recommend_relationship


def Algorithm_location(location, dictionary):
    d = dictionary[0]
    recommend_location = []
    for key in d:
        title = d[key]
        wordList = re.sub("[^\w]", " ", title).split()
        for word in wordList:
            if location == word:
                recommend_location.append(key)
    # print "Based on your location, the recommended friends are", recommend_location
        #print wordList
    #print recommend_location
    return recommend_location

def Algorithm_interest(interest, dictionary):
    d = dictionary[1]
    recommend_interest = []
    for key in d:
        content = d[key]
        wordList = re.sub("[^\w]", " ", content).split()
        if interest in wordList:
            recommend_interest.append(key)

    return recommend_interest


def Algoirhtm_best(recommend_location, recommend_age, recommend_relationship, recommend_interest, dictionary):
    # if age and location have same user, match will be true
    #match = (set(recommend_age) == set(recommend_location))
    count = 1
    count2 = 1
    d = dictionary
    #if match:
    #	best = list(set(recommend_age) & set(recommend_location))
    #	if len(best) > 0:
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
								<li class="active"><a href="project.html">Project Description</a></li>
								<li><a href="BasicInfo.py">Demo</a></li>
							</ul>
						
						</div>
					</div>
			</div>

			<div class = "container">The best recommendation:</div>
			
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
		}(document, 'script', 'facebook-jssdk'));
		</script>	
	"""
    for userid in recommend_age:
        if userid in recommend_location:
            #match = d[userid]
            print "<p>"
            print "There is best recommendation for you! (You have same age and location to the user.)"
            print """<html><p><a href="http://newyork.craigslist.org/%s"> <input type="button" value ="Get your best match!"></a></html>""" % d[userid]
            print "<p>"
        elif userid in recommend_relationship:
            match = userid
            print "There is best recommendation for you! (The user also wants a relationship and both of you have same age.)"
            print """<html><p><a href="http://newyork.craigslist.org/%s"> <input type="button" value ="Get your best match!"></a></html>""" % d[userid]
        elif userid in recommend_interest:
            match = userid
            print "There is best recommendation for you! (The user has same interest as you.)"
            print """<html><p><a href="http://newyork.craigslist.org/%s"> <input type="button" value ="Get your best match!"></a></html>""" % d[userid]
        elif userid in recommend_location and userid in recommend_relationship and userid in recommend_interest:
            match = userid
            print "Wow! You have perfect match with the user!"
            print """<html><p><a href="http://newyork.craigslist.org/%s"> <input type="button" value ="Get your best match!"></a></html>""" % d[userid]
    if recommend_age or recommend_location:
        if len(recommend_location) > 0:
            print "<p>"
            print "Based on your current city, the recommended users are..."
            print "<p>"
        for userid in recommend_location:
            print count
            print "<p>"
            print"""<html><a href="http://newyork.craigslist.org/%s"> <input type="button" value ="Get your best match!"></a></html>""" % d[userid]
            #print "http://newyork.craigslist.org/mnh/m4w/%s.html"%userid
            count = count + 1
            print "<p>"
        if len(recommend_age) > 0:
            print "Based on your age, the recommended users are..."
            print "<p>"
        for userid in recommend_age:
            print count2
            print "<p>"
            print"""<html><a href="http://newyork.craigslist.org/%s"> <input type="button" value ="Get your best match!"></a></html>""" % d[userid]
            #print "http://newyork.craigslist.org/mnh/m4w/%s.html"%userid
            count2 = count2 + 1
            print "<p>"
    else:
        print "Sorry, there are no best recommendation for you. Please enter more information or change to different district."




if __name__ == "__main__":

    data = trade_spider(1)
    #print data
    dictionary = makeDictionary(data)
    recommend_age = Algorithm_Age("25", dictionary)
    recommend_location = Algorithm_location("NYC", dictionary)
    recommend_relationship = Algorithm_relationship("No", dictionary)
    recommend_interest = Algorithm_interest("sex", dictionary)
    Algoirhtm_best(recommend_location, recommend_age, recommend_relationship, recommend_interest, dictionary[3])