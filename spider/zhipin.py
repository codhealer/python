import requests
import re
import time
import os
from utils import httpUtils
def get_links(url,pattern):
    wb_data = requests.get(url,headers=httpUtils.getHeader())
    print(wb_data)
get_links('https://www.zhipin.com/c101280600/?page=1&ka=page-2','')