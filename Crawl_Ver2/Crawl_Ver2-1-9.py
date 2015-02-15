#!/home4/chenlin/public_html/friendrecommendations.com/env/bin/python

#====================================================================
# shebang path to where beautiful soup was saved. The insturction for
# how to install the beautiful soup refers to the link below
# 1. http://tinyurl.com/l4tffoq
# 2. http://tinyurl.com/kgryrsf
#====================================================================

#====================================================================
# import the libraries

import requests
from bs4 import BeautifulSoup
import re
import cgi
import cgitb;cgitb.enable()
import sys

sys.dont_write_bytecode = True
#====================================================================
  

#====================================================================
# print the HTNL format in the beginning, otherwise it will be unable
# to display html on the web, so it is very important
#====================================================================
print "Content-type: text/html\r\n\r\n"
print ""
#====================================================================


#====================================================================
# function that crawls the data from the website
#====================================================================
def trade_spider(max_pages, url):
    # Make the empty list for title, content, userid, attribute,
    # href, age, location, and district
    titleArray = []
    contentArray = []
    useridArray = []
    attrsArray = []
    hrefArray = []
    ageArray = []
    locationArray = []
    districtArray = []

    
    #url = 'http://newyork.craigslist.org/search/w4w'
    

    # get the url content using request library	
    source_code = requests.get(url)
    # convert the content of web to the text
    plain_text = source_code.text
    # crawl the data from the text using beautifulsoup
    soup = BeautifulSoup(plain_text)

    # use for loop to get each catogory seperately and save in its list
    # The method of soup.findAll can refer to tutorial link below
    # link: https://www.youtube.com/watch?v=XjNm9bazxn8

    for dataId in soup.findAll('span', {'class': 'txt'}):

        # By observing the html format of the website, it can be known
        # the 'href' is part of 'class: 'hdrlnk', so it can be crawl
        # directly, and others vice versa
        href = dataId.find('a', {'class': 'hdrlnk'})['href']
        userid = dataId.find('a', {'class': 'hdrlnk'})['data-id']
        title = dataId.find('a', {'class': 'hdrlnk'}).string

        # Since the author might not offer thier age or location, so
        # it need to set if statement to avoid the error occur
        if dataId.find('span', {'class': 'price'}) == None:
            age = "null"
        else:
            age = dataId.find('span', {'class': 'price'}).text

        if dataId.find('small') == None:
            location = "null"
        else:
            location = dataId.find('small').string

        # Since the output of district does not have its category in craigslit's html format
        # so it need to be taken from the href, which is start from first char to forth char
        district = href[1:4]

        link = "http://newyork.craigslist.org/" + href
        # calling other function to get the content of each user
        Content = getContent(link)
        content = Content[0]
        attrs = Content[1]

        # We are still in for loop! So we need to store every users' information into an array
        # *IMPORTANT: Since beautifulsoup will always return unicode, we need to convert to utf-8
        # by myself, otherwise it will show u'something' which will cause many problem when create
        # a link in html format
        titleArray.append(title.encode("utf-8"))
        useridArray.append(userid.encode("utf-8"))
        hrefArray.append(href.encode("utf-8"))
        ageArray.append(age.encode("utf-8"))
        locationArray.append(location.encode("utf-8"))
        districtArray.append(district.encode("utf-8"))
        contentArray.append(content.encode("utf-8"))
        attrsArray.append(attrs.encode("utf-8"))

    return titleArray, useridArray, hrefArray, ageArray, locationArray, districtArray, contentArray, attrsArray

#======================================================================================
# The function the crawls the information about the content and atrribute of each user
#======================================================================================
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

#===========================================================================================
# The function that collects all the data and make to dictionary
#===========================================================================================
def makeDictionary(data):

    # data = [titleArray, useridArray, hrefArray, ageArray, locationArray ... etc]
    title = data[0]
    userid = data[1]
    href = data[2]
    age = data[3]
    location = data[4]
    district = data[5]
    content = data[6]
    attrs = data[7]

    # make to the dictionary
    # zip is the function to make two array lists to a dictionary
    dict1 = dict(zip(userid, title))
    dict2 = dict(zip(userid, content))
    dict3 = dict(zip(userid, age))
    dict4 = dict(zip(userid, href))
    dict5 = dict(zip(userid, attrs))
    dict6 = dict(zip(userid, location))
    dict7 = dict(zip(userid, district))

    return dict1, dict2, dict3, dict4, dict5, dict6, dict7

#===================================================================================
# The function that seperate every word in each user in order to search the keywords
# When this function is called, the keywords, which user input, and dictionary are
# sent to this function
#===================================================================================
def splitDict(words, dictionary):
    # make the array list to store matched users
    matchedId = []
    # read every userid's information in for loop
    for dict in dictionary:
        # content is equal to dictiony[dict] (ex. dict1[userid])
        content = dictionary[dict]
        # split the words in content
        wordList = re.sub("[^\w]", " ", content).split()
        # if the words which user input is matched the word in content, then return
        # the matched userid and saved in matchedId
        if words in wordList:
            matchedId.append(dict)

    return matchedId

#=======================================================================================
# The function that deal with the matched userid and finding the best recommendation
#=======================================================================================
def recommendation(InputLocation, InputDistrict, InputAge, InputRelationship, InputInterest, InputAnykeywords,
                   dictionary):
    # Call the splitDict function for location, age, interest...etc dictionary
    locationList = splitDict(InputLocation, dictionary[5])
    districtList = splitDict(InputDistrict, dictionary[6])
    ageList = splitDict(InputAge, dictionary[2])
    relationshipList = splitDict(InputRelationship, dictionary[1])
    interestList = splitDict(InputInterest, dictionary[1])
    anykeywordsList = splitDict(InputAnykeywords, dictionary[1])

    # Make an empty array list for saving the link
    locationhref = []
    districthref = []
    agehref = []
    relationshiphref = []
    interesthref = []
    anykeywordshref = []

    # Get the best recommendation by finding whether the matchedid in location, age, interest...etc have same matchedid
    # The method I use is using symmetric difference, difference, and union

    # set() is the function to compare to list

    # In this case, we are looking for the matched userid that in more than two category such as relationship and interest.
    # The way to do this is to find the interection of six set. However, we need to do step by step. We need to find the
    # symmetric difference minus intersection of three set first and do next three set and finally with two set. Therefore
    # Union minus difference of six set

    # First, find the difference of three set
    # a = symmetic difference between location, district, and age minus the central part
    a = set(locationList) ^ set(districtList) ^ set(ageList) - (set(locationList) & set(districtList) & set(ageList))
    # After we get a, we can find the difference for next three set
    b = a ^ set(relationshipList) ^ set(interestList) - (a & set(relationshipList) & set(interestList))
    # Then, we can find the difference between the last one
    c = b ^ set(anykeywordsList)
    # Finally we can find the union of all set and minus c which is the difference of all sets
    d = set(locationList) | set(districtList) | set(ageList) | set(relationshipList) | set(interestList) | set(anykeywordsList)
    # e is the result
    e = d - c
    # Refer to wiki page: http://en.wikipedia.org/wiki/Symmetric_difference. We can have more imaginary thought, but we are finding
    # the reverse result with central part
    

    # The for loop below is to find the matched userid's href and save into the empty list
    for userid in locationList:
        if len(locationList) > 0:
            locationhref.append(dictionary[3][userid])
    for userid in districtList:
        if len(districtList) > 0:
            districthref.append(dictionary[3][userid])
    for userid in ageList:
        if len(ageList) > 0:
            agehref.append(dictionary[3][userid])
    for userid in relationshipList:
        if len(relationshipList) > 0:
            relationshiphref.append(dictionary[3][userid])
    for userid in interestList:
        if len(interestList) > 0:
            interesthref.append(dictionary[3][userid])
    for userid in anykeywordsList:
        if len(anykeywordsList) > 0:
            anykeywordshref.append(dictionary[3][userid])

    # For matched (best recommend) 
    matchList = list(e)
    matchhref = []
    for userid in matchList:
        matchhref.append(str(dictionary[3][userid]))

    return matchhref, locationhref, districthref, agehref, relationshiphref, interesthref, anykeywordshref

def printOut(getRecommend):
    print """
		<html>
		<head>
			<title>Get your best recommendation!</title>
			<meta charset="utf-8" />
			<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
			<meta name="viewport" content="width=device-width, initial-scale=1" />
			<link href="css/bootstrap.min.css" rel="stylesheet">
			<script type="text/javascript" src="jquery-1.11.1.min.js"></script>
			

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
								<li class="active"><a href="SelectGender">Demo</a></li>
							</ul>

						</div>
					</div>
			</div>

			<div class = "container">
			    <div>
				    <h2>Based on your location and district, the recommended users are:</h2>
				 	<div class= "container" >
				        <p id="locationRecommend"></p>
        	        		</div>						    
				    <p></p>
				</div>
				<div>
				    <h2>Based on your age, the recommended users are:</h2>
				 	<div class= "container" >
				        <p id="ageRecommend"></p>
        	        		</div>
				    <p></p>
				</div>
				<div>
				    <h2>Based on your relationship, the recommended users are:</h2>
				 	<div class= "container" >
				        <p id="relationshipRecommend"></p>
        	        		</div>				    				    
				    <p></p>
				</div>
				<div>
				    <h2>Based on your interest, the recommended users are:</h2>
				 	<div class= "container" >
				        <p id="interestRecommend"></p>
        	        		</div>					    
				    <p></p>
				</div>
				<div>
				    <h2>Based on your keywords entered, the recommended users are:</h2>
				 	<div class= "container" >
				        <p id="keywordsRecommend"></p>
        	        		</div>					    
				    <p></p>
				</div>
			</div>
			



			<div style="display: none;" id = "location">"%s"</div>
			<div style="display: none;" id = "age">"%s"</div>
			<div style="display: none;" id = "relationship">"%s"</div>
	        	<div style="display: none;" id = "interest">"%s"</div>
	        	<div style="display: none;" id = "keywords">"%s"</div>


            <script type="text/javascript">
            
            
            
            
            
    // ==============================================================================
    		//console.log(document.getElementById("location").innerHTML);
	            var link="http://newyork.craigslist.org/";
	            if (document.getElementById("location").innerHTML == '"[]"') {
	            	//console.log("There is nothing");
	            	document.getElementById("locationRecommend").innerHTML = "None";
	            
	            } else {	            
	            	    //console.log("There is something");
	            	    var locationT = $('#location').html();	            
		            var location = JSON.parse(locationT);
		            
		            location = location.replace("[", "");
		            location = location.replace("]", ""); 
		            location = location.replace(/u'/g, "");
		            location = location.replace(/'/g, "");
		            location = location.replace(/ /g, "");
		            
	
		            var locationR = [];
		            locationR = location.split(",");
		            location = locationR;
		            console.log(location);
		            //console.log(typeof(ageR));
			
			
	                var href = "http://newyork.craigslist.org";
	                var temp = ""
	                    
	                for (var i = 0; i < location.length; i++) {
	
	                    temp0 = href + location[i];
	
	                    $('#locationRecommend').before('<a class = "btn btn-default" id="link0To" href = "">Link</a>');
	                    var e0 = document.getElementById("link0To");
	                    num0 = i.toString();
	
			    e0.id = "link0To" + num0;
			    var linkstr0 = e0.id;
	                   
	                    $('#'+linkstr0).attr('href',temp0);
	                    		
	                    $('#'+linkstr0).click(function() {
	                    	document.location.href = $('#' + linkstr0).attr('href') ;
	                    });
	                }
	            	
	            }
	            
              
	  	    //====================================================================================
	            var ageT = $('#age').html();	            
	            var age = JSON.parse(ageT);
	            
	            age = age.replace("[", "");
	            age = age.replace("]", ""); 
	            age = age.replace(/u'/g, "");
	            age = age.replace(/'/g, "");
	            age = age.replace(/ /g, "");
	            

	            var ageR = [];
	            ageR = age.split(",");
	            age = ageR;
	            console.log(age);
	            //console.log(typeof(ageR));
		
		
                var href = "http://newyork.craigslist.org";
                var temp = ""
                    
                for (var i = 0; i < age.length; i++) {

                    temp = href + age[i];

                    $('#ageRecommend').before('<a class = "btn btn-default" id="linkTo" href = "">Link</a>');
                    var e = document.getElementById("linkTo");
                    num = i.toString();

			        e.id = "linkTo" + num;
			        var linkstr = e.id;
                   
                    $('#'+linkstr).attr('href',temp);
                    		
                    $('#'+linkstr).click(function() {
                    	document.location.href = $('#' + linkstr).attr('href') ;
                    });
                }
		//======================================================================================
		
		if (document.getElementById("relationship").innerHTML == '"[]"') {
	            	//console.log("There is nothing");
	            	document.getElementById("relationshipRecommend").innerHTML = "None";
	            
	            } else {	            
	            	    //console.log("There is something");
	            	    var relationshipT = $('#relationship').html();	            
		            var relationship = JSON.parse(relationshipT);
		            
		            relationship = relationship.replace("[", "");
		            relationship = relationship.replace("]", ""); 
		            relationship = relationship.replace(/u'/g, "");
		            relationship = relationship.replace(/'/g, "");
		            relationship = relationship.replace(/ /g, "");
		            
	
		            var relationshipR = [];
		            relationshipR = relationship.split(",");
		            relationship = relationshipR;
		            console.log(relationship);
		            //console.log(typeof(ageR));
			
			
	                var href = "http://newyork.craigslist.org";
	                var temp = ""
	                    
	                for (var i = 0; i < relationship.length; i++) {
	
	                    temp2 = href + relationship[i];
	
	                    $('#relationshipRecommend').before('<a class = "btn btn-default" id="link2To" href = "">Link</a>');
	                    var e2 = document.getElementById("link2To");
	                    num2 = i.toString();
	
			    e2.id = "link2To" + num2;
			    var linkstr2 = e2.id;
	                   
	                    $('#'+linkstr2).attr('href',temp2);
	                    		
	                    $('#'+linkstr2).click(function() {
	                    	document.location.href = $('#' + linkstr2).attr('href') ;
	                    });
	                }
	            	
	            }
		
		// ======================================================================================================
		
		if (document.getElementById("interest").innerHTML == '"[]"') {
	 
	            	document.getElementById("interestRecommend").innerHTML = "None";
	            
	        } else {	            
	            	    //console.log(document.getElementById("interest").innerHTML);
	            	    var interestT = $('#interest').html();	            
		            var interest = JSON.parse(interestT);
		            
		            interest = interest.replace("[", "");
		            interest = interest.replace("]", ""); 
		            interest = interest.replace(/u'/g, "");
		            interest = interest.replace(/'/g, "");
		            interest = interest.replace(/ /g, "");
		            
	
		            var interestR = [];
		            interestR = interest.split(",");
		            interest= interestR;
		            console.log(interest);

			
			
	                var href = "http://newyork.craigslist.org";
	                var temp = ""
	                    
	                for (var i = 0; i < interest.length; i++) {
	
	                    temp3 = href + interest[i];
	
	                    $('#interestRecommend').before('<a class = "btn btn-default" id="link3To" href = "">Link</a>');
	                    var e3 = document.getElementById("link3To");
	                    num3 = i.toString();
	
			    e3.id = "link3To" + num3;
			    var linkstr3 = e3.id;
	                   
	                    $('#'+linkstr3).attr('href',temp3);
	                    		
	                    $('#'+linkstr3).click(function() {
	                    	document.location.href = $('#' + linkstr3).attr('href') ;
	                    });
	                }
	            	
	            }
		// =============================================================================================================
			
			//console.log(document.getElementById("keywords").innerHTML);
		if (document.getElementById("keywords").innerHTML == '"[]"') {
	
	            		document.getElementById("keywordsRecommend").innerHTML = "None";
	            
	            } else {	            
				//console.log(document.getElementById("keywords").innerHTML);
	            	    var keywordsT = $('#keywords').html();	            
		            var keywords = JSON.parse(keywordsT);
		            
		            keywords = keywords.replace("[", "");
		            keywords = keywords.replace("]", ""); 
		            keywords = keywords.replace(/u'/g, "");
		            keywords = keywords.replace(/'/g, "");
		            keywords = keywords.replace(/ /g, "");
		            
	
		            var keywordsR = [];
		            keywordsR = keywords.split(",");
		            keywords= keywordsR;

			
			
	                var href = "http://newyork.craigslist.org";
	                var temp = ""
	                    
	                for (var i = 0; i < keywords.length; i++) {
	
	                    temp4 = href + keywords[i];
	
	                    $('#keywordsRecommend').before('<a class = "btn btn-default" id="link4To" href = "">Link</a>');
	                    var e4 = document.getElementById("link4To");
	                    num4 = i.toString();
	
			    e4.id = "link4To" + num4;
			    var linkstr4 = e4.id;
	                   
	                    $('#'+linkstr4).attr('href',temp4);
	                    		
	                    $('#'+linkstr4).click(function() {
	                    	document.location.href = $('#' + linkstr4).attr('href') ;
	                    });
	                    
	                }
	            	
	            }
		
            </script>


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
	""" % (getRecommend[1], getRecommend[3], getRecommend[4], getRecommend[5], getRecommend[6])

if __name__ == "__main__":

	form = cgi.FieldStorage()

	if "GetInfo" in form:
    
		interest = form.getvalue("interest")
		age = form.getvalue("age")
		location = form.getvalue("location")
		relationship = form.getvalue("relationship")
		if relationship == "Yes":
			relationship == "relationship"
		else:
			relationship == ""
			
		education = form.getvalue("education")
		work = form.getvalue("work")
		
		gender = form.getvalue("Gender")
		lookingfor = form.getvalue("LookingFor")

		url = ''
		if gender == 'Male' and lookingfor == 'Female':
			url = 'http://newyork.craigslist.org/search/w4m'
		elif gender == 'Male' and lookingfor == 'Male':
			url = 'http://newyork.craigslist.org/search/m4m'
		elif gender == 'Female' and lookingfor == 'Male':
			url = 'http://newyork.craigslist.org/search/m4w'
		elif gender == 'Female' and lookingfor == 'Female':
			url = 'http://newyork.craigslist.org/search/w4w'
    
		data = trade_spider(2, url)
		dictionary = makeDictionary(data)
		getRecommend = recommendation(location, "mnh", age, relationship, interest, "", dictionary)
		printOut(getRecommend)
