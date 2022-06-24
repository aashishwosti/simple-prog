import requests
from bs4 import BeautifulSoup
url="https://www.w3schools.com/"

r=requests.get(url)
print(r)
print(r.status_code)
print(r.url)
htmlcontent=(r.content)
print(htmlcontent)

soup=BeautifulSoup(htmlcontent, 'html.parser')
print(soup.prettify())
print(soup.title)


print(type(soup.title))# 1.Tag
print(type(soup.title.string))# 2.NavigableString
print(soup)# 3.BeautifulSoup

soup2=BeautifulSoup('<p><!--how does this comment work --></p>')
print(soup2.p) 
print(soup2.p.string)
print(type(soup2.p.string)) 

title=soup.title
print(title)
print(type(title))
print(title.string)
print(type(title.string))