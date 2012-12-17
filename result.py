#!/usr/bin/env python
import cgi
import MySQLdb

#open database using try excepy sentence
db = MySQLdb.connect(host="localhost", user="cha", passwd="test623",db='testdb')
cursor = db.cursor() #make cursor
cursor.execute('''use testdb''') #sql syntax. means 'using testdb'
cursor.execute('''create table if not exists address
                (name char(10), number char(50), etc char(10))''')#create table in testdb
#open database using try excepy sentence


#using cgi sentence, take variables in hello.py

form = cgi.FieldStorage()
data = []

for name in form.keys():
        data.append(form[name].value)
#save in mysql database table
cursor.execute(u'''insert into `address` values (%s, %s, %s)''',(data[1],data[2],data[0]))
db.commit() 

#using cgi sentence, take variables in hello.py
print "Content-Type: text/html"
print
print """\
<!DOCTYPE HTML>
<html>
  <head>
    <meta charset="UTF-8">	
    <link rel="stylesheet" type="text/css" href="./bootstrap(1)/bootstrap/css/bootstrap.css"> 	
    <link rel="stylesheet" type="text/css"  href="./bootstrap(1)/bootstrap/css/bootstrap-responsive.css">     
  </head>
  <body>
    
    <ul class="nav nav-list well" style="width:100">
      
      <li><a href="#"> name number  etc <li><a href="#">
      <li><a href="#">"""

cursor.execute('''select*from address''')
screen = cursor.fetchall()


datap = []

for result in screen:
	datap = result
	name = datap[0]
	number = datap[1]
	etc = datap[2]
	print (name + " " + number + " " + etc)
	print """<li><a href="#">"""

print""" </a></li>
      
    </ul>
    <script type="text/javascript"  src="http://code.jquery.com/jquery-1.8.2.min.js"></script>
    <script type="text/javascript" src="./bootstrap(1)/bootstrap/js/bootstrap.js"></script>
  </body>

</html>
"""



#save in mysql database table
db.close()
print "Finished!"



