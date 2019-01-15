import requests
from bs4 import BeautifulSoup
html = 'https://www.u2mtv.com/movie/info/?mid=13094'
r = requests.get(html)
c = r.content
soup = BeautifulSoup(c,"html.parser")

titleinfo = soup.find('div',class_='title_div clearfix').h1.get_text().replace(' ','').replace('\n',' ')
title = soup.find('div',class_='title_div clearfix').h1.get_text().replace(' ','').replace('\n','')
info = []
info_tag = []
info_ul = soup.find('div',class_='movie_info_attr_div clearfix')
info.append(info_ul.find('ul',class_='movie_info_direct_ul').get_text().replace('\n',''))
info.append(info_ul.find('ul',class_='movie_info_actor_ul').get_text().replace('\n',' '))
for i in info_ul.find_all('span',class_='movie_info_table_content'):
    info.append(i.get_text().replace('\n',' '))
info.append(info_ul.find('ul',class_='movie_info_tag_ul').get_text().replace('\n',' '))
for i in info_ul.find_all('span',class_='label'):
    info_tag.append(i.get_text().replace('\n',' '))
if len(info)!=len(info_tag):
    for pause in range(len(info_tag)-len(info)):
        info.append('') 
content = ''
for con_html in soup.find('div',class_='movie_info_content_div').find_all('p'):
    content = content+con_html.get_text()
import os
path = "./U2/"
if not os.path.isdir(path):
    os.mkdir(path)
file_name =title+"U2.txt"
f = open("U2/"+file_name,'w',encoding='utf-8')
for i in range(len(info)):
    f.write(info_tag[i]+info[i]+'\n')
f.write('簡介 : '+content+'\n')

f.close()