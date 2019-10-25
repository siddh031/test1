import requests
import re
from bs4 import BeautifulSoup as bs
from datetime import datetime
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
conn = mysql.connector.connect(
  host="127.0.0.1",
  user="root",
  passwd="12345",
  database="test"
)

cursor = conn.cursor()

def convert(s): # conver array into string function
      new = "" 
    for x in s: 
        new += x  
    return new 

r = requests.get('https://medium.com')
soup = bs(r.content, 'lxml')
links = soup.find_all('a') 
print("Number links in the Web page : ")
print(len(links))#number of link in the page 
for s1 in links:
  	s2 = s1.get('href')
	if (s2.find('https:') != 0): 
    	  s3 ='https:' + s2
	else:
	  s3 = s2

	query = ("select ifnull(max(web_h1_id),0)+1 as id from test.web_h1")#insert data in web_h1 table

	cursor.execute(query)

	id1 = cursor.fetchone()
	
	edate = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

	id2 = id1[0]
	
	qry = "insert into test.web_h1 (web_h1_id, web_h1_url) values (%s, %s)"
	val = (id2, s3)

	cursor.execute(qry,val)
	conn.commit()


	s4 = requests.get(s3)	
        soup1 = bs(s4.content, 'lxml')			
	
	print("Web page Title :")
	title1 = soup1.title.string
        print(soup1.title.string) #get title web page
	
	print("\n")

	a1 = soup1.find_all('meta')

	print("Description :")
	er = [ meta.attrs['content'] 
	for meta in a1
	if 'name' in meta.attrs and meta.attrs['name'] == 'description'
		]

	des1 = convert(er)
	print(convert(er)) # get description of web page
	
	print("\n")

	#get Header of webpage
	print("List of all the h1 :")
	for heading in soup1.find_all(["h1"]):
		
	    temph1 = heading.text.strip()
	    print(heading.text.strip())# get header of the web page
	    print("\n") 
	qry1 = "insert into test.web_h2 (web_h2_id, web_h2_title,web_h2_header1,web_h2_description) values (%s, %s,%s, %s)"
	val1 = (id2,title1,temph1,des1)

	cursor.execute(qry1,val1)
	conn.commit()

cursor.close()
conn.close()
	
