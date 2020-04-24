#多进程爬虫(不同于多线程)

import multiprocessing as mp
import time
from urllib.request import urlopen, urljoin
from bs4 import BeautifulSoup
import re
# base_url = "https://baike.baidu.com/item/%E4%B8%96%E7%95%8C%E5%9C%B0%E7%90%83%E6%97%A5"
base_url = "https://baike.baidu.com/item/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/217599"

# DON'T OVER CRAWL THE WEBSITE OR YOU MAY NEVER VISIT AGAIN
if base_url != "https://baike.baidu.com/item/%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0/217599":
    restricted_crawl = True
else:
    restricted_crawl = False


def crawl(url):
    response = urlopen(url)
    time.sleep(1)             # slightly delay for downloading
    html = response.read().decode()
    response.close()
    return html

def parse(html):
    try:
        soup = BeautifulSoup(html, 'lxml')
        urls = soup.find_all('a', {"target": "_blank", "href": re.compile("/item/(%.{2})+$")})
        title = soup.find('h1').get_text().strip()
        page_urls = set([urljoin(base_url, url['href']) for url in urls])
        # keywords=soup.find('meta', {'name': "keywords"})['content']
    except TypeError:
        url='主题没有找到'
    # url = soup.find('meta', {'property': "og:url"})['content']
    return title, page_urls
        # , keywords

#添加进程：
def go():
    unseen = set([base_url,])#使用set来存储数据不会重复
    seen = set()
    pool = mp.Pool()
    count, t1 = 0, time.time()

#创建一个字典
    parents ={}
    while len(unseen) != 0:                 # still get some url to visit
        print("已经爬这些网页:"+str(len(seen)))
        if restricted_crawl and len(seen) > 100:
            break
        try:
            # htmls = [crawl(url) for url in unseen]
            count_fater=0;
            results=set()
            page_urls=set()
            print("正在解析网站所有url...>>>")
            # for key in parents:
            #     if parents[key] == "":
            #         continue
            #     if parents[key] in unseen:
            #         print("正在爬取：")
            #         print(parents(key)[-1])
            for url in unseen:
                # print("正在爬取:"+url)
                html = pool.apply_async(crawl, args=(url,)).get()
                result = pool.apply_async(parse, args=(html,)).get()
                count +=1
                if str.strip(result[0]) =='义项' or str.strip(result[0]) =='百度百科：多义词':
                    continue
                print(count,result[0],url)
                for key in result[1]:
                    # print(key)
                    page_urls.add(key)
            # parents[url]=page_urls
            seen.update(unseen)
            unseen.clear()
            unseen.update(page_urls - seen)
            print('\n解析完毕...>>>')
            # seen.update(unseen)         # seen the crawled
            # unseen.clear()              # nothing unseen

        except ConnectionResetError:
            unseen.clear()
            unseen.update(page_urls - seen)
            print('服务器连接超时')
            continue

        # for title, page_urls, keywords,url in results:
        #     if title =='义项':
        #         continue
        #     print(count, title, url)
        #     count += 1
        #     unseen.update(page_urls - seen)     # get new url to crawl
    print('Total time: %.1f s' % (time.time()-t1, ))    # 53 s

if __name__ =='__main__':
    go()
