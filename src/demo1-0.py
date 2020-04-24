from urllib.request import urlopen

# if has Chinese, apply decode()
html = urlopen("https://morvanzhou.github.io/static/scraping/basic-structure.html").read().decode('utf-8')
# html = urlopen("https://www.bilibili.com/video/BV1MW411B7rv?p=2").read().decode('utf-8')
print(html)

import re
res = re.findall(r"<title>(.+?)</title>", html)
print("\nPage title is: ", res[0])