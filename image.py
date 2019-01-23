


import urllib.request
import os
import requests


os.chdir("/Users/path/Downloads/") #your path
i=1

while i < 199:
    urllib.request.urlretrieve("http://www.nexusbook.com/studymail/image/"+ str(i) + "ho.jpg", str(i)+".jpg")
    i+=1


