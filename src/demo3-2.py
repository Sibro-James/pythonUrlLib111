#下载图片
import requests
import webbrowser


import os
os.makedirs('./img/', exist_ok=True)
#方法1
IMAGE_URL = "https://pics3.baidu.com/feed/5243fbf2b211931364b26727964cfdd290238d2b.jpeg?token=ed6b5cc6334f3839eb69aac04bc357ff&amp;s=27135C816E1602D60A657C830300E090"
from urllib.request import urlretrieve #取出图片
urlretrieve(IMAGE_URL, 'img/image2.png')      # whole document (地址,名称)


#方法2
import requests
r = requests.get(IMAGE_URL)
with open('img/image3.png', 'wb') as f:
    f.write(r.content)


#方法3 不同于12全部放到内存再下载。此方法为实时下载
r = requests.get(IMAGE_URL, stream=True)    # stream loading
with open('./img/image3.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32): #每次读取字节
        f.write(chunk)