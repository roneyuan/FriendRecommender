#!/usr/bin/env python

import time
import cgi
import cgitb;cgitb.enable()

print "Content-type: text/html\r\n\r\n";
print ""
 
def SelectGender():

    print '<!DOCTYPE html>'

    print """
    <html>
    
    <head>  
        <meta charset="utf-8" />
		<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1" /> 
		<link href="css/bootstrap.min.css" rel="stylesheet">
    </head>
    
    <div id="fb-root"></div>
		<script>(function(d, s, id) {
			var js, fjs = d.getElementsByTagName(s)[0];
			if (d.getElementById(id)) return;
			js = d.createElement(s); js.id = id;
			js.src = "//connect.facebook.net/en_US/sdk.js#xfbml=1&appId=1495984630617535&version=v2.0";
			fjs.parentNode.insertBefore(js, fjs);
			}(document, 'script', 'facebook-jssdk'));
		</script>
    
    <title>Friend Recommendation</title>
	
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
                                    <li  class="active"><a href="SelectGender">Demo</a></li>
                            </ul>               
                    </div>
            </div>
	</div> 
    <form class="form-horizontal" method ="post" action ="">
    <table class = "table table-bordered" align = "center">
    
	<tr>
            <td>Please select your gender</td>
            <td>
            <select name="Gender" size = "1">
            <option value = "null"></option>
            <option value = "Male">Male</option>
            <option value = "Female">Female</option>
            </select>
            </td>
 	</tr>

	<tr>
            <td>Your are looking for</td>
            <td>
            <select name="LookingFor" size = "1">
            <option value = "null"></option>
            <option value = "Male">Male</option>
            <option value = "Female">Female</option>
            </select>
            </td>
 	</tr>	

    <tr><td>    
        <input type="submit" name="DistAndGender" value="Submit">
    </tr></td>
    
    </table>
    </form>
    <p>
    <p>
    <p>
    <div class="fb-like" data-href="http://friendrecommendations.com/" data-layout="standard" data-action="like" data-show-faces="true" data-share="true"></div>
    </body>
    </html>

    """

def whenMale():
	print """
    <html>
    <head><meta http-equiv="refresh" content="0; url=http://www.friendrecommendations.com/BasicInfoMale"></head>
    </html>
    """

def whenFemale():
	print """
    <html>
    <head><meta http-equiv="refresh" content="0; url=http://www.friendrecommendations.com/BasicInfoFemale"></head>
    </html>
    """        

def whenMaleForMale():
	print """
    <html>
    <head><meta http-equiv="refresh" content="0; url=http://www.friendrecommendations.com/BasicInfoMaleForMale"></head>
    </html>
    """

def whenFemaleForFemale():
	print """
    <html>
    <head><meta http-equiv="refresh" content="0; url=http://www.friendrecommendations.com/BasicInfoFemaleForFemale"></head>
    </html>
    """   

if __name__ == "__main__":

    form = cgi.FieldStorage()

    SelectGender()

    if "DistAndGender" in form:
        Gender = form.getvalue("Gender")
		LookingFor = form.getvalue("LookingFor")

        if Gender == "Male":
			if LookingFor == "Female":
				whenMale()
			else:
				whenMaleForMale()
        elif Gender =="Female":
			if LookingFor == "Male":
				whenFemale()
			else:
				whenFemaleForFemale()
        if LookingFor =="null" and Gender != "null":
			print "<center>*Please Enter Second Column</center>"
		elif Gender =="null" and LookingFor != "null":
			print "<center>*Please Enter First Column</center>"
		elif LookingFor == "null" and Gender =="null":
			print "<center>*Please Enter Both Column</center>"

    
