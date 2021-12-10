from urllib.request import urlopen
from bs4 import BeautifulSoup


def page_access(url):
    html = urlopen(url)  
    global bsoup
    bsoup = BeautifulSoup(html, "html.parser")
    return bsoup


def main():
    global bs
    url = ""
    bs = page_access(url) 


if __name__ == "__main__":
    main()