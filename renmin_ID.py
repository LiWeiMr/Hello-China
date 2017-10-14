#encoding:utf-8
import re
import requests
import redis
import random
from bs4 import BeautifulSoup

class Renmin(object):

    def Cooks(self):
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 Name',
            'Cookie': 'HttpOnly=true; HttpOnly=true; HttpOnly=true; __jsluid=37a77ab34f3d62de9e9cc737c38d24c1'
        }
        return head

    def Min(self):
        req = requests.get('http://www.sg.gov.cn/zw/gczbtb/zbgg/',headers=self.Cooks()).content.decode('utf-8')
        url = re.compile('<a target="_blank" title=".*?" href="(.*?)">.*?</a>', re.S)
        list = url.findall(req)
        for i in list:
            urls = str(i)
            self.Craws_num(urls)
            # print(urls)


if __name__=="__main__":
    Renmin().Min()
