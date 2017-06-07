import requests
from bs4 import BeautifulSoup
import re

f = open('英文录音链接地址.txt','w')
host = 'http://k6.kekenet.com/'
p = re.compile('Sound/[0-9]+.+mp3')
url = 'http://www.kekenet.com/Article/201412/350296.shtml'
html_ = requests.get(url).content
html = html_.decode('utf-8')
soup = BeautifulSoup(html_,'html.parser',from_encoding = 'utf-8')
list_main = soup.find('div',id = 'List1').find_all('div')
list_all = []
for i in list_main:
    for j in i.find_all('div'):
        list_all.append('http://www.kekenet.com' + j.find('a')['href'])

count = 0
for i in list_all:
    html = requests.get(i).content
    html_ = html.decode('utf-8')
    soup = BeautifulSoup(html,'html.parser',from_encoding = 'utf-8')
    f.write(host + re.search(p,html_).group() + '\t' + soup.find('h1',id = 'nrtitle').get_text().replace(' ','').replace('\n','').replace('\r','').replace('\t','') + '\n')
    f.flush()
    name = soup.find('h1',id = 'nrtitle').get_text().replace(' ','').replace('\n','').replace('\r','').replace('\t','') + '.mp3'
    f1 = open( name[22:].replace(':','-'),'wb' )
    f1.write(requests.get(host + re.search(p,html_).group()).content)
    f1.close()
    count += 1
    print (name[22:] + '\t' + str(count) + '网页已经被爬取！')
