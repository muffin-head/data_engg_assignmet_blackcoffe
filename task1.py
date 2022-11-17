import requests
from bs4 import BeautifulSoup
import pandas as pd
df = pd.read_excel('Input.xlsx', sheet_name='Sheet1')


def scraper(url,file_name):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0'}
    url = requests.get(url, headers=headers)
    url.status_code
    url.headers
    c = url.content
    soup = BeautifulSoup(c, "html.parser")
    samples2 = soup.find_all(class_="td-post-content")
    for p in samples2:
        price = (p)
        a = (price.get_text().strip())
        file1 = open(str(file_name),"w")
  
# \n is placed to indicate EOL (End of Line)
        file1.writelines(a)
        file1.close() 


for i in (range(len(df))):
  file_name=df['URL_ID'][i]
  link  = df['URL'][i]
  scraper(link,file_name)

