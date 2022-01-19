#! python3
#search.py - open several search results.
import requests, sys , webbrowser, bs4
print('What do you wish to search:')
search=input() #Get the search topic
print('Googling.....')
res=requests.get('https://google.com/search?q='+search)
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,features='html.parser')
linkElems=soup.select('.r a')

numOpen=min(5,len(linkElems))
for i in range(numOpen):
    webbrowser.open('http"//google.com'+linkElems[i].get('href'))
