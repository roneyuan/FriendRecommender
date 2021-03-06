#!/usr/bin/env python

import cgitb;

cgitb.enable()
import sys
import json

sys.dont_write_bytecode = True

print "Content-type: text/html\r\n\r\n"
print ""


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
								<li class="active"><a href="BasicInfo">Demo</a></li>
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
		            location = location.replace(/'/g, "");
		            location = location.replace(/ /g, "");
	
		            var locationR = [];
		            locationR = location.split(",");
		            location = locationR;
		            //console.log(ageR);
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
	            age = age.replace(/'/g, "");
	            age = age.replace(/ /g, "");

	            var ageR = [];
	            ageR = age.split(",");
	            age = ageR;
	            //console.log(ageR);
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
		            relationship = relationship.replace(/'/g, "");
		            relationship = relationship.replace(/ /g, "");
	
		            var relationshipR = [];
		            relationshipR = relationship.split(",");
		            relationship = relationshipR;
		            //console.log(ageR);
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
		            interest = interest.replace(/'/g, "");
		            interest = interest.replace(/ /g, "");
	
		            var interestR = [];
		            interestR = interest.split(",");
		            interest= interestR;
		            //console.log(interest);

			
			
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
	""" % (getRecommend[0], getRecommend[1], getRecommend[2], getRecommend[3], getRecommend[4])


if __name__ == "__main__":
	printOut(([], ['/mnh/w4m/4829757949.html', '/brk/w4m/4829698589.html', '/brk/w4m/4829757738.html',
                   '/brk/w4m/4829020231.html', '/fct/w4m/4823434531.html'],
                  ['/mnh/w4m/4829650820.html', '/lgi/w4m/4828842050.html', '/brk/w4m/4829626677.html',
                   '/mnh/w4m/4829761857.html', '/mnh/w4m/4828384217.html',
                   '/wch/w4m/4829320228.html', '/brk/w4m/4829311179.html', '/mnh/w4m/4821685711.html',
                   '/mnh/w4m/4810785328.html', '/mnh/w4m/4829558341.html',
                   '/brk/w4m/4829698589.html', '/mnh/w4m/4829510502.html', '/mnh/w4m/4821725638.html',
                   '/mnh/w4m/4824366539.html', '/brk/w4m/4829595756.html',
                   '/mnh/w4m/4829705621.html', '/mnh/w4m/4829173177.html', '/brx/w4m/4829625965.html',
                   '/lgi/w4m/4829471884.html', '/mnh/w4m/4829617306.html',
                   '/brk/w4m/4829757738.html', '/brk/w4m/4829020231.html', '/fct/w4m/4823434531.html',
                   '/brx/w4m/4829295436.html', '/jsy/w4m/4828944935.html'],
                  ['/brk/w4m/4829797387.html', '/wch/w4m/4820772064.html'], []))