##爬取百度百科
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import random


# base_url = "https://baike.baidu.com"
base_url = "http://biz.smpaa.cn/"
# base_url = "http://172.30.195.105/ysxt/#"


# # his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
# #
# #
# # url = base_url + his[-1]
# #
# # html = urlopen(url).read().decode('utf-8')
# # soup = BeautifulSoup(html, features='lxml')
# # print(soup.find('h1').get_text(), '    url: ', his[-1])
# #
# # sub_urls = soup.find_all("a", {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
# #
# # if len(sub_urls) != 0:
# #     his.append(random.sample(sub_urls, 1)[0]['href'])
# # else:
# #     # no valid sub link found
# #     his.pop()
# # print(his)

# his = ["/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB/5162711"]
his = ["ysxtqx/#"]


for i in range(20):
    url = base_url + his[-1]

    html = urlopen(url).read().decode('utf-8')
    print(html)
    soup = BeautifulSoup(html, features='lxml')
    print(i, soup.find('title').get_text(), '    url: ', his[-1])

    # find valid urls
    sub_urls = soup.find_all("a")

    if len(sub_urls) != 0:
        a=random.sample(sub_urls, 1)[0]['href']
        his.append(a)
    else:
        # no valid sub link found
        his.pop()