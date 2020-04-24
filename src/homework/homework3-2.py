#下载国家地理的动物图片

from bs4 import BeautifulSoup
import requests

URL = "http://www.nationalgeographic.com.cn/animals/"
html = requests.get(URL).text
soup = BeautifulSoup(html , features='lxml')
img_ul = soup.find_all('ul',{'class':'img_list'})
print(img_ul)
for ul in img_ul:
    imgs = ul.find_all('img')
    for img in imgs:
        imgurl = img['src']
        r = requests.get(imgurl)
        imgName = imgurl.split('/')[-1]
        with open('../img/%s' % imgName, 'wb') as f: #%s为占位符，由后面的占用
            for chunk in r.iter_content(chunk_size=32):
                f.write(chunk)
        print('Saved %s' % imgName)
