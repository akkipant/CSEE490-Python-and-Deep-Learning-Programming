import requests
from bs4 import BeautifulSoup

page = requests.get("https://catalog.umkc.edu/course-offerings/graduate/comp-sci")
#print(page)
#print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

html = list(list(soup.children)[2].children)
#print(html)
#print(soup.find("p", class_="courseblockdesc").string)
#print(soup.p.string)
for x,y in zip(soup.find_all("span", class_="title"), soup.find_all("p", class_="courseblockdesc")):
    print(x.string, y.string)
    print()