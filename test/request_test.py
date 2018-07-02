import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'
}
res = requests.get('http://www.baidu.com/',headers=headers)
# soup具有jquery选择器的效果 
soup = BeautifulSoup(res.text,'html.parser')
try:
    print(soup.prettify())
except ConnectionError:
    print('拒绝链接')