from bs4 import BeautifulSoup
import urllib.request


def getLinks(url):

    source_code = urllib.request.urlopen(url)
    plain_text = source_code
    soup = BeautifulSoup(plain_text, "html.parser")
    print(soup.title.text.strip())
    # to find html a tags
    for text in soup.findAll("a"):
        print(text.get("href"))


if __name__ == '__main__':
    getLinks('https://en.wikipedia.org/wiki/Deep_learning')
