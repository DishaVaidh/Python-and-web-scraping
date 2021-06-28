import requests as rq
from bs4 import BeautifulSoup as bs

data=rq.get("https://www.imdb.com/list/ls051981806/")
soup=bs(data.text,"html.parser")

for i in soup.find_all('h3',{"class":"lister-item-header"}):
    #t=i.find('span',{"class":"lister-item-year text-muted unbold"})
    print(i.a.string,i.a.next_sibling.next_sibling.string[1:5],sep='-')
    n=i.next_sibling.next_sibling.span.next_sibling.next_sibling.next_sibling.next_sibling
    print("Time-",n.string,n.next_sibling.next_sibling.next_sibling.next_sibling.string)
    print("Ratings-",i.next_sibling.next_sibling.next_sibling.next_sibling.span.next_sibling.next_sibling.string)
    k=i.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling
    print("Desciption-",k.string)
    #print("Director-",k.next_sibling.next_sibling.a.string)
    #b=k.next_sibling.next_sibling.a.next_sibling.next_sibling.next_sibling.next_sibling
    #print("stars-",b.string)
    a=list(k.next_sibling.next_sibling.find_all('a'))
    print("Director-",a[0].string)
    print("Stars-",end="")
    [print(a[h].string,end=",") for h in range(1,len(a))]
    j=k.next_sibling.next_sibling.next_sibling.next_sibling.children
    print("\nGross-",list(j)[-2].string)
    print("\n\n")




'''div=soup.find_all('div',{'class':'lister-item-content'})
for i in div:
    print(i.h3.a.string,end='-')
    print(i.find('span',{'class':"lister-item-year text-muted unbold"}).string[1:5])
    print("Time-",i.find('span',{'class':"runtime"}).string)
    x=i.find('div',{'class':"ipl-rating-star small"}).span.next_sibling.next_sibling.string
    print("Ratings",x,end="\n")
    t=i.find('div',{"class":'inline-block ratings-metascore'})
    print("Description",t.next_sibling.next_sibling.string)
    #same concept in stars and director as above'''
    
