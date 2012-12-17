#!/usr/bin/env python


print "Content-Type: text/html"
print
print """\
<html>
  <head>
    <meta charset="UTF-8">
    <title>web sql test </title>

	<link rel="stylesheet" type="text/css" href="./bootstrap(1)/bootstrap/css/bootstrap.css"> 	
	<link rel="stylesheet" type="text/css"  href="./bootstrap(1)/bootstrap/css/bootstrap-responsive.css">    
  

  </head>
  
  <body>

	<header class="hero-unit" style="width:300">
	      <h1> Test </h1>
	      <p> My address list <p>	
        </header>
    
	<form action="result.py" method="get">
	<header class="hero-unit" style="width:300">
        <p> insert and click 'add' button </p>

	<div id ="new_id">
	    <br/><label for="usernamelabel">name</label>
	    <input id = "textname" type="text" name = "name" value="">
	    <br/><label for="usernumber">number</label>   	
	    <input id = "textnumber" type="text" name = "number" value="">	 
	    <br/><label for="useretc">etc</label> 
	    <input id = "textetc" type="text" name = "etc" value="">
	    <br/><input type="submit" value="add">
	</div>
        

            

 

  </body>
</html>
"""

print(textname)
