# encoding:utf-8
import requests,json,re,redis,random
from bs4 import BeautifulSoup
head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}
url='http://www.sg.gov.cn/zw/gczbtb/zbgg/201710/t20171011_394067.html'
req=requests.get(url,headers=head).content.decode('UTF-8')
soup=BeautifulSoup(req,'lxml')
title=soup.find('h4').text
times=soup.find('div',class_="xl-cont-xx").find('span').text
cont=soup.find('div',class_="TRS_PreAppend").text
print title+'\n',times+'\n',cont.strip()
# print req