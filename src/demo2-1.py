from bs4 import BeautifulSoup
from urllib.request import urlopen
##BeautifulSoup开始使用
# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
print(html)

print('*****************************************')
soup = BeautifulSoup(html,features='html.parser')#features是解析方式,lxml是html解析，python内置为：'html.parser'
print(soup.h1)
print('\n', soup.p)#是包括p标签的

print('*****************************************')
all_href = soup.find_all('a')#找到所有的a标签
all_href = [l['href'] for l in all_href]
print('\n', all_href)


print('*****************************************')
all_href = soup.find_all('a')#找到所有的a标签
newAllHref =[]
for l in all_href:
    newAllHref.append(l['href'])  #此方法和上面的相同。这里的l是包含很多属性的。
print('\n', newAllHref)
