#requests: an alternative to urllib
import requests
import webbrowser
# param = {"wd": "莫烦Python"}
# r = requests.get('http://www.baidu.com/s', params=param)
# print(r.url)
# webbrowser.open(r.url)


# data = {'firstname': 'zrc', 'lastname': '123'}
# r = requests.post('http://pythonscraping.com/pages/files/processing.php', data=data)
# print(r.text)
# webbrowser.open(r.url)

#
# file = {'uploadFile': open('a.jpg', 'rb')}
# r = requests.post('http://pythonscraping.com/pages/files/processing2.php', files=file)
# print(r.text)


# payload = {'username': 'Morvan', 'password': 'password'}
# r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', data=payload)
# print(r.cookies.get_dict())
# print(r.text)
# r = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
# webbrowser.open(r.url)

#每个网站都要    requests.get( 'html' ,cookies=r.cookies)，很繁琐。这里直接用session,直接保存登录信息
session = requests.Session()
payload={'loginName':'yy1001','password':'111111'}
r = session.post('http://localhost:8080/ysxt/workspace/main.action', data=payload)
print(r.cookies.get_dict())
r = session.get("http://localhost:8080/ysxt/login.jsp")
print(r.text)