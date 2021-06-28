import requests as rq
from bs4 import BeautifulSoup as bs

data=rq.get("https://www.indiatoday.in/")
soup=bs(data.text,"html.parser")

t=soup.find('ul',{'class':"itg-listing"})
k=list(t.children)
print(k[0].a.string)
print(k[0].next_sibling.a.string)#print(k[1].a.string)
print(k[0].next_sibling.next_sibling.a.string)
print(k[0].next_sibling.next_sibling.next_sibling.a.string)
print(k[0].next_sibling.next_sibling.next_sibling.next_sibling.a['title'])
print(k[0].next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.a['title'])

