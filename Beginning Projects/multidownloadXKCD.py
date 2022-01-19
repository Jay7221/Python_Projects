#! python3
# multiDownload.py - Downloads XKCD comics using multiple threads.
import os , requests, bs4, threading
def downloadXkcd(startComic,endComic):
    for urlNumber in range(startComic,endComic):
        #Dowmload the page
        print('Downloading page http://xkcd.com/%s'%(urlNumber))
        res=requests.get('http://xkcd.com/%s'%(urlNumber))
        res.raise_for_status()
        soup=bs4.BeautifulSoup(res.text)
        comicElem=soup.select('#comic img')
        if comicElem==[]:
            print('Could not find comic page')
        else:
            comicUrl=comicElem[0].get('src')
            #Download image
            print('Downloading image %s ....'%(comicUrl))
            res=requests.get(comicUrl)
            res.raise_for_status()
            #Save the image to ./xkcd
            imageFile=open(os.path.join('xkcd',os.path.basename(comicUrl)))
            for chunk in res.iter_content(10000):
                imageFile.write(chunk)
            imageFile.close()

#Create and start the Thread objects
downloadThreads=[]
for i in range(0,20,4):
    downloadThread=threading.Thread(target=downloadXkcd,args=(i,i+9))
    downloadThreads.append(downloadThread)
    downloadThread.start()


#Wait for all threads to end
for downloadThread in downloadThreads:
    downloadThread.join()

print('Done!')


