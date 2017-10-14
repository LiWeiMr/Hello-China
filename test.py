# encoding:utf-8
import requests,json,re,redis,random,time,pymysql
from bs4 import BeautifulSoup
from useragent import agent


class Gove(object):

    # def Ips(self):
    #     redisL = redis.Redis(host='127.0.0.1', port='6384', db=0)
    #     red_len=redisL.llen('proxies')
    #     ips=redisL.lrange('proxies',0,red_len)
    #     ip=random.choice(ips)
    #     return ip

    def __init__(self):

        self.head = {'User-Agent': random.choice(agent),
                     'Cookie':'HttpOnly=true; __jsluid=f405a1c207e2802fe2fe01377770e791; Hm_lvt_d7682ab43891c68a00de46e9ce5b76aa=1507715633,1507726280; HttpOnly=true'
                     }
        self.db=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='test',charset='utf8')
        self.cursor=self.db.cursor()

    def Main(self):
        url='http://www.sg.gov.cn/zw/gczbtb/zbgg/index.html'
        req=requests.get(url,headers=self.head).content.decode('UTF-8')
        max_page=re.compile('createPageHTML\(.*?, (.*?), .*?, .*?, .*?\);').findall(req)
        print max_page[0]
        urls = 'http://www.sg.gov.cn/zw/gczbtb/zbgg/index.html'
        for page in range(1,int(max_page[0])+1):
                print '第'+str(page)+'页'
                reqs = requests.get(urls, headers=self.head).content.decode('UTF-8')
                soup = BeautifulSoup(reqs, 'lxml')
                list_url=soup.find('ul',class_="comlist-wgk ").find_all('a')
                for i in list_url:
                    all_url='http://www.sg.gov.cn/zw/gczbtb/zbgg'+i['href'][1:]
                    self.Crawl_cont(all_url)
                urls = 'http://www.sg.gov.cn/zw/gczbtb/zbgg/index_'+str(page)+'.html'
    #
    def Crawl_cont(self,all_url):
        print all_url
        req = requests.get(all_url, headers=self.head).content.decode('UTF-8')
        time.sleep(1)
        soup = BeautifulSoup(req, 'lxml')
        title = soup.find('h4').text
        times = soup.find('div', class_="xl-cont-xx").find('span').text
        cont = soup.find('div', class_="TRS_PreAppend").text.strip()
        print title + '\n', times + '\n', cont
        # sql='insert into info(title,times,cont) VALUES ("%s","%s","%s")'%(title,times,cont)
        # self.cursor.execute(sql)
        # self.db.commit()



if __name__=="__main__":
    Gove().Main()