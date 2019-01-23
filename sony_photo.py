## ptyhon3 

## osx 용 

## 


```
완료 버전 
```
 

import urllib.request

import os

 

 

 

 

 

os.chdir("/Users/path/Downloads") #your path

 

 

opener=urllib.request.build_opener()

opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]

urllib.request.install_opener(opener)

 

##urllib.request.urlretrieve(url,local)

 

 

 

url = ['yosemite', 'vatican', 'rome', 'porto', 'hani', 'tewahipounamu', 'kinabalu', 'namib', 'hampi', 'thegreatwall', 'guanajuato', 'quito','pyramid', 'potala', 'wulingyuan', 'socotra', 'saintpetersburg', 'fujiantulou', 'cappadocia', 'lijiang', 'ogasawara', 'alhambra', 'split', 'pamukkale', 'rideaucanal', 'venice', 'brugge', 'fujisan', 'yoshino', 'paris', 'segovia', 'valletta', 'ceskykrumlov', 'engadin', 'cuzco',  'amsterdam', 'tajmahal', 'machupicchu', 'plitvice', 'titano', 'dubrovnik', 'sassi', 'tallinn', 'yakushima', 'shirakami', 'sukhothai', 'firenze', 'itchankala', 'lordhoweisland', 'prague', 'amalfi', 'montsaintmichel', 'mounthuangshan', 'berne', 'sanaa', 'halongbay', 'grandcanyon', 'shirakawa-go', 'istanbul', 'halongbay', 'losglaciares', 'iguazu']

 

 

for j in url: 

	i=1;

	while i<10:

	    try:

	        urllib.request.urlretrieve("https://www.sony.net/united/clock/share/img/photo/" + str(j)+ "/fp/0"+ str(i)+".jpg", str(j) + str(i)+".jpg")

	    except:

	        print("not possible" + str(i))

	    i+=1;

