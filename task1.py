import requests
from bs4 import BeautifulSoup

def scraper(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}
    url = requests.get(url, headers=headers)
    url.status_code
    url.headers
    c = url.content
    soup = BeautifulSoup(c, "html.parser")
    samples2 = soup.find_all(class_="td-post-content")
    for p in samples2:
        price = (p)
        print(price.get_text().strip())
        print()



link  = "https://insights.blackcoffer.com/man-and-machines-together-machines-are-more-diligent-than-humans-blackcoffe/"
scraper(link)
