#!/usr/bin/env python

import cgitb;cgitb.enable()
import sys

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
				    <p></p>
				</div>
				<div>
				    <h2>Based on your age, the recommended users are:</h2>
				    <p></p>
				</div>
				<div>
				    <h2>Based on your relationship, the recommended users are:</h2>
				    <p></p>
				</div>
				<div>
				    <h2>Based on your interest, the recommended users are:</h2>
				    <p></p>
				</div>
				<div>
				    <h2>Based on your keywords entered, the recommended users are:</h2>
				    <p></p>
				</div>
			</div>

			<p id="arrayString"></p>



            <script type="text/javascript">
	            var link="http://newyork.craigslist.org/search/w4m/";
	            var location=%s;
	            var age = %s;
	            var relationship = %s;
	            var interest = %s;
	            var keywords = %s;
	            if location.length > 0 {
                    for (var i = 0; i < location.length; i++) {
                        href = link + location[i];
                        document.getElementById("arrayString").innerHTML=arrayString;
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
	""" % (getRecommend[0], getRecommend[1], getRecommend[2], getRecommend[3], getRecommend[4], getRecommend[5])

if __name__ == "__main__":

    printOut(([], ['/mnh/w4m/4829757949.html', '/brk/w4m/4829698589.html', '/brk/w4m/4829757738.html', '/brk/w4m/4829020231.html', '/fct/w4m/4823434531.html'],
                  ['/mnh/w4m/4829650820.html', '/lgi/w4m/4828842050.html', '/brk/w4m/4829626677.html', '/mnh/w4m/4829761857.html', '/mnh/w4m/4828384217.html',
                   '/wch/w4m/4829320228.html', '/brk/w4m/4829311179.html', '/mnh/w4m/4821685711.html', '/mnh/w4m/4810785328.html', '/mnh/w4m/4829558341.html',
                   '/brk/w4m/4829698589.html', '/mnh/w4m/4829510502.html', '/mnh/w4m/4821725638.html', '/mnh/w4m/4824366539.html', '/brk/w4m/4829595756.html',
                   '/mnh/w4m/4829705621.html', '/mnh/w4m/4829173177.html', '/brx/w4m/4829625965.html', '/lgi/w4m/4829471884.html', '/mnh/w4m/4829617306.html',
                   '/brk/w4m/4829757738.html', '/brk/w4m/4829020231.html', '/fct/w4m/4823434531.html', '/brx/w4m/4829295436.html', '/jsy/w4m/4828944935.html'],
                  ['/brk/w4m/4829797387.html', '/wch/w4m/4820772064.html'], [], ['/brk/w4m/4829797387.html', '/wch/w4m/4820772064.html']))