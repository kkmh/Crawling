```
사이트 이미지 다운 :에러 버전 
```


import urllib.request
import os


os.chdir("/Users/path/Downloads") #your path
i=1;

while i<200:
    try:
        urllib.request.urlretrieve("http://www.nexusbook.com/studymail/image/"+ str(i)+"ho.jpg",str(i)+".jpg")
    except:
        print("not possible" + str(i))
    i+=1;
