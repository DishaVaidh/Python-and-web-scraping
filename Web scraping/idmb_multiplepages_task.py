import requests as rq
from bs4 import BeautifulSoup as bs

data=rq.get("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&ref_=adv_prv")
soup=bs(data.text,"html.parser")


n=1
for k in range(5):
    data=rq.get("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start="+str(n)+"&ref_=adv_nxt")
    n=n+50
    soup=bs(data.text,"html.parser")

    div=soup.find_all('div',{'class':"lister-item-content"})
    for i in div:
        print(i.h3.a.string,end='-')
        print(i.find('span',{'class':"lister-item-year text-muted unbold"}).string[1:-1]




'''import requests as rq
from bs4 import BeautifulSoup as bs

data=rq.get("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&ref_=adv_prv")
soup=bs(data.text,"html.parser")

for k in range(4):
    div=soup.find_all('div',{'class':"lister-item-content"})
    for i in div:
        print(i.h3.a.string,end='-')
        print(i.find('span',{'class':"lister-item-year text-muted unbold"}).string[1:-1])
    a = soup.find('a',{'class':"lister-page-next next-page"})
    hh = a.get('href')
    link = "https://www.imdb.com"+hh
    soup=bs(rq.get(link).text,"html.parser"'''


