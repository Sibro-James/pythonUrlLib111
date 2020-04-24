from bs4 import BeautifulSoup
from urllib.request import urlopen
##BeautifulSoup开爬取Css

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/list.html").read().decode('utf-8')
print(html)
print('*****************************************')
soup = BeautifulSoup(html, features='lxml')

# use class to narrow search
month = soup.find_all('li', {"class": "month"}) #只选取class为month的数据
for m in month:
    print(m.get_text())  #print(m) 是包含标签的