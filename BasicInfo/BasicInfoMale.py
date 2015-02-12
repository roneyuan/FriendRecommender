#!/usr/bin/env python

import cgi
import cgitb; cgitb.enable()

print "Content-type: text/html\r\n\r\n";
print ""

def EnterBasicInfo():
    print '<DOCTYPE html>'
    print """
    <html>
    <head>
        <title>Demo</title>
            <meta charset="utf-8" />
			<meta http-equiv="Content-type" content="text/html; charset=utf-8" />
			<meta name="viewport" content="width=device-width, initial-scale=1" /> 
		<link href="css/bootstrap.min.css" rel="stylesheet">
	
	
		<style type="text/css">
			#loadingmsg {
				top: center;
				right: 50%;
				margin-left: auto;
				text-align: center;
				margin:auto;
				position: absolute;
				z-index: 100;
			}
			  
			#loadingover {
				background: black;
				z-index: 99;
				width: 100%;
				height: 100%;
				position: fixed;
				top: 0;
				left: 0;
				-ms-filter: "progid:DXImageTransform.Microsoft.Alpha(Opacity=80)";
				filter: alpha(opacity=80);
				-moz-opacity: 0.8;
				-khtml-opacity: 0.8;
				opacity: 0.8;
			}
		</style>
	
	
	
	
	
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
                                    <li  class="active"><a href="BasicInfo">Demo</a></li>
                            </ul>               
                    </div>
            </div>
	</div>    
    <center>Please Enter the column below</center>
    <form class="form-horizontal" method = "post" action = "CrawlMale" onsubmit='showLoading();'>
    <table class = "table table-bordered" align = "center">
        
        <tr>
            <td>Interest</td>
            <td> <input type = "text" name = "interest" size = "8"> </td>
        </tr>
        
        <tr>
            <td>Work's industry</td>
            <td>
            <select name = "work" size = "1">
            <option value = ""></option>
            <option value = "agriculture">Agriculture</option>
            <option value = "business">Business</option>
            <option value = "engineering">Engineering</option>
            <option value = "medical">Medical</option>
            <option value = "public">Public Relation</option>
            <option value = "science">Science</option>
            </select>
            </td>
        </tr>        
                
        <tr>
            <td>Education</td>
            <td>
            <select name = "education" size = "1">
            <option value = ""></option>
            <option value = "highschool">High School</option>
            <option value = "undergraduate">Bachelor's degree</option>
            <option value = "graduate">Master's degree</option>
            <option value = "phd">Ph.D</option>
            <option value = "postdoc">Postdoc</option>
            </select>
            </td>
        </tr>
            
        <tr>
            <td>Age</td>
            <td> 
            <select name = "age" size = "1">
            <option value = ""></option>
            <option value = "18">18</option>
            <option value = "19">19</option>
            <option value = "20">20</option>
            <option value = "21">21</option>
            <option value = "22">22</option>
            <option value = "23">23</option>
            <option value = "24">24</option>
            <option value = "25">25</option>
            <option value = "26">26</option>
            <option value = "27">27</option>
            <option value = "28">28</option>
            <option value = "29">29</option>
            <option value = "30">30</option>
            <option value = "31">31</option>
            <option value = "32">32</option>
            <option value = "33">33</option>
            <option value = "34">34</option>
            <option value = "35">35</option>
            <option value = "36">36</option>
            <option value = "37">37</option>
            <option value = "38">38</option>
            <option value = "39">39</option>
            <option value = "40">40</option>
            <option value = "41">41</option>
            <option value = "42">42</option>
            <option value = "43">43</option>
            <option value = "44">44</option>
            <option value = "45">45</option>
            <option value = "46">46</option>
            <option value = "47">47</option>
            <option value = "48">48</option>
            <option value = "49">49</option>
            <option value = "50">50</option>
            <option value = "51">51</option>
            <option value = "52">52</option>
            <option value = "53">53</option>
            <option value = "54">54</option>
            <option value = "55">55</option>
            <option value = "56">56</option>
            <option value = "57">57</option>
            <option value = "58">58</option>
            <option value = "59">59</option>
            <option value = "60">60</option>
            <option value = "61">61</option>
            <option value = "62">62</option>
            <option value = "63">63</option>
            <option value = "64">64</option>
            <option value = "65">65</option>
            <option value = "66">66</option>
            <option value = "67">67</option>
            <option value = "68">68</option>
            <option value = "69">69</option>
            <option value = "70">70</option>
            </select>
            </td>
        </tr>
        
        <tr>
            <td>Location</td>
            <td> <input type = "text" name = "location" size = "8"> </td>
        </tr>      
        
        <tr>
            <td>Relationship</td>
            <td>
            <select name="relationship" size="1">
            <option value="null"></option>            
            <option value="Yes">Yes</option>
            <option value="No">No</option>
            </select>
            </td>
            
        </tr>
        
    <tr><td>
    <input type="submit" id="GetInfo" name="GetInfo" value="Submit" onClick=>
    
    </tr></td>
    </table>
    <div class="container">
		*It may take couple minutes to analyze the data 
	</div>
    </form>   

	<div id='loadingmsg' style='display: none;'>
		<img src="loading.gif" width="120%"/>
	</div>
	
	<div id='loadingover' style='display: none;'></div>


    <div class="container">	
	    <div class="fb-like" data-href="http://friendrecommendations.com/" data-layout="standard" data-action="like" data-show-faces="true" data-share="true"></div>
    </div>
    <script type = "text/javascript">
        function showLoading() {
			document.getElementById('loadingmsg').style.display = 'block';
			document.getElementById('loadingover').style.display = 'block';
		}
    </script>
    
    
    
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

if __name__ == "__main__":

    form = cgi.FieldStorage()

    EnterBasicInfo()