import requests
from bs4 import BeautifulSoup
import pandas
r=requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s=0.html")
c=r.content
soup=BeautifulSoup(c,"html.parser")
page_nr=soup.find_all('a',{"class":"Page"})[-1].text

l=[]


base_url="https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="
for page in range(0,int(page_nr)*10,10):
   r=requests.get(base_url+str(page)+".html")
   c=r.content
   soup=BeautifulSoup(c,"html.parser")
   all=soup.find_all('div',{'class','propertyRow'})

   for item in all:
      d={}
      
      d["Price"]=item.find('h4',{"class","propPrice"}).text.strip()
      d["Address"]=item.find_all('span',{"class",'propAddressCollapse'})[0].text
      d["Locality"]=item.find_all('span',{"class",'propAddressCollapse'})[1].text
      try:

         d["Beds"]=item.find('span',{'class','infoBed'}).find('b').text
      except:
         d["Beds"]="None"
      try:

         d["SqFt"]=item.find('span',{'class','infoSqFt'}).find('b').text
      except:
         d["Sqft"]="None"
      try:
         d["Full Bath"]=item.find('span',{'class','infoValueFullBath'}).find('b').text
      except:
         d["Full Bath"]="None"
      for column_group in item.find_all('div',{'class':'columnGroup'}):
         for feature_Group,feature_Name in zip(column_group.find_all("span",{"class":"featureGroup"}),column_group.find_all('span',{'class':'featureName'})):
               if "Lot Size" in feature_Group.text:
                  d["Lot Size"]=feature_Name.text
      l.append(d)


df=pandas.DataFrame(l)


df.to_csv("Web Scrapping/Scrapped from webs.csv")


        
           
       
    
    

   
    
