import requests
from bs4 import BeautifulSoup

r=requests.get("https://pythonizing.github.io/data/example.html")
c=r.content
soup=BeautifulSoup(c,"html.parser")
#print(soup.prettify())
all=soup.find_all('div',{"class":"cities"})
#all=soup.find('div',{"class":"cities"}) if you write this code you will get only the first class
#print(all[0].find_all('h2')[0].text)
for item in all:
    print(item.find_all('h2')[0].text)
#for item in all:
#print(item.find_all('h2')[0].text)

