import requests
from bs4 import BeautifulSoup
from time import sleep
for each in range(1,9):
    url = 'https://pczone.ge/product-category/%E1%83%99%E1%83%9D%E1%83%9B%E1%83%9E%E1%83%98%E1%83%A3%E1%83%A2%E1%83%94%E1%83%A0%E1%83%94%E1%83%91%E1%83%98/intel-core-i9/page/{}/'.format(each)
    r = requests.get(url)
    txt = r.text

    soup = BeautifulSoup(txt, 'html.parser')
    ul_tag = soup.find('ul', {'class': 'products columns-4'})
    f = open('content.csv', 'a')
    for i in ul_tag.find_all("li"):
        print(i.h2.text)
        content = f.write(i.h2.text + '\n')
    sleep(20)
