#encoding:utf-8
import re
import requests
import redis
import random
# import queue
from bs4 import BeautifulSoup

class Renmin(object):

    def __init__(self):
        self.redisL = redis.Redis(host='127.0.0.1',port=6379,db=5)
    def Cooks(self):
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36 Name',
            'Cookie': 'HttpOnly=true; HttpOnly=true; HttpOnly=true; __jsluid=37a77ab34f3d62de9e9cc737c38d24c1'

        }
        return head

    # def AgencyIP(self):
    #     s_ip = redis.Redis(host='127.0.0.1',port=6379,db=0)
    #     u_len = s_ip.llen('proxies')
    #     urls = s_ip.lrange('proxies' ,0 ,u_len)
    #     ips = random.choice(urls)
    #     ip = str(ips,encoding='utf-8')
    #     return ip

    def Min(self):

        url = 'http://www.sg.gov.cn/zw/gczbtb/zbgg/'
        for i in range(1,200+1):
            urls = url + ('index_'+str(i)+'.html')
            print(urls)
            self.Craw_num(urls)

    def Craw_num(self,urls):
        req = requests.get(urls, headers=self.Cooks()).content.decode('utf-8')
        url = re.compile('<a target="_blank" title="(.*?)" href="(.*?)">.*?</a>', re.S)
        list = url.findall(req)
        for i,j in list:
            urls='http://www.sg.gov.cn/zw/gczbtb/zbgg/'+j[1:]
            self.Craws_num(urls)

    def Craws_num(self,urls):
        print(urls)
        req = requests.get(urls,headers=self.Cooks()).content.decode('utf8')
        # print(req)
        soup = BeautifulSoup(req, 'lxml')
        title = soup.find('h4').get_text()
        date_time = soup.find('div', class_="xl-cont-xx").find('span').get_text()
        content = soup.find('div', class_="TRS_PreAppend").get_text()
        print(title)
        print(date_time)
        print(content)


if __name__=="__main__":
    Renmin().Min()
