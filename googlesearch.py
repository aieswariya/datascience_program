# import requests
# from bs4 import BeautifulSoup
# try: 
#     from googlesearch import search
# except ImportError:  
#     print("No module named 'google' found") 
  

# query = "A computer science portal"
  
# for j in search(query, tld="com", num=10, stop=1, pause=2): 
#     print(j) 

# import requests, sys,webbrowser,bs4
# res=requests.get('https://google.com/search?q='+''.join(sys.argv[1:]))

# res.raise_for_status()
# soup=bs4.BeautifulSoup(res.text ,"html.parser")
# linkElements=soup.select('.r a')
# linkToOpen=min(5,len(linkElements))
# for i in range(linkToOpen):
#      webbrowser.open('https://google.com'+linkElements[i].get('href'))
# res.raise_for_status()
# soup=bs4.beautifulSoup(res.text,"html")

import requests 
import webbrowser
from bs4 import BeautifulSoup

user=input("enter to search:")
print("googleing....")
search=requests.get("https://www.google.com/search?q="+''+user)
soup=BeautifulSoup(search.text,'lxml')
try:
  search_results=soup.select(' .kCrYT  a')
except exceptionError:
  print("no module named'google' found")
for link in search_results[:10]:
    print(link)
    #webbrowser.open('https://google.com/'+actual_link)