#! python3
# comicDownload.py - Downloads all XKCD comics.
import requests,bs4,os
url='http://xkcd.com'       #Starting url
os.makedirs('XKCD',exist_ok=True)          #Store comics in ./XKCD
for i in range(20):
    #Download the page.
    print('Downloading page %s.....'%url)
    page=requests.get(url)
    page.raise_for_status()

    
    soup=bs4.BeautifulSoup(page.text)

    #Find the url of comic page.
    comicElem=soup.select('#comic img')
    

     
    #Go to comicLink and download the image.    
    if comicElem==[]:
        print('Could not find comic image.')
    else:
        comicUrl='http:'+comicElem[0].get('src')
        print('Downloading image %s ....'%comicUrl)
        comicImage=requests.get(comicUrl)
        comicImage.raise_for_status()

    #save the image to ./XKCD
    imageFile=open(os.path.join('XKCD',os.path.basename(comicUrl)),'wb')
    for chunk in comicImage.iter_content(10000):
        imageFile.write(chunk)
    imageFile.close()

    #Get prev page link.
    prevLink=soup.select('a[rel=prev]')[0]

    url='http://xkcd.com'+prevLink.get('href')
    
