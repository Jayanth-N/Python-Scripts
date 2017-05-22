import requests
import json
from bs4 import BeautifulSoup
from random import randint
import time

rnum = randint(1,12)
url="http://123hindijokes.com/very-funny-jokes/"+str(rnum)
wcod=requests.get(url)
beaut=BeautifulSoup(wcod.content,"lxml")
allul =beaut.find_all('ul',{'class':'statusList'})
arr={}
for one in allul:
    para =one.find_all('li')
    for var in para:
        joke=var.get_text()
        arr[1]=joke
with open("joke.json",'w') as joke:
    json.dump(arr,joke,ensure_ascii=False,indent = 4)
    time.sleep(10)
print ("Hindi Jokes Printed randomly from a page "+str(rnum))   

