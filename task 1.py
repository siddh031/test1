import requests
from bs4 import BeautifulSoup as bs
url = "https://medium.com"

r = requests.get(url)
soup = bs(r.content, 'lxml')

print("Web page Title : ")
#print(soup.select_one('title').text) # get title web page
print(soup.title.string)# get title web page
 

a1 = soup.find_all('meta')

print("Description :")
er = [ meta.attrs['content'] 
for meta in a1
	if 'name' in meta.attrs and meta.attrs['name'] == 'description'
		]


print(er) # get description of web page



#get Header of webpage
print("List of all the h1 :")
for heading in soup.find_all(["h1"]):
    print( heading.text.strip()) 



