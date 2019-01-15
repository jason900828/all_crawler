import requests
from bs4 import BeautifulSoup
movie_id = 'fpen55093026'
r = requests.get("http://www.atmovies.com.tw/movie/"+movie_id+"/")
c = r.content
soup = BeautifulSoup(c,"html.parser")

title = soup.find('div',class_ = 'filmTitle').get_text().replace('\n','').replace('\r','').replace('\t','')

des_top = soup.find('div',id='filmTagBlock').find_all('span')[2]
des_top_str = str(des_top) 
a = des_top_str.find('<span>')
b = des_top_str.find('<ul')
des_top_str = des_top_str[a+6:b].replace('\n','').replace('\r','').replace('\t','')

li_des = soup.find('div',id='filmTagBlock').find_all('span')[2].find('ul').find_all('li')
li_text = ''
for li_ in li_des:
    li_text = li_text+li_.get_text()+'\n'

des_down_str = soup.find('div',style='width:90%;font-size: 1.1em;').get_text().replace('\n','').replace('\r','').replace('\t','').replace('劇情簡介              ','')

ul_info = soup.find('div',id='filmCastDataBlock').find_all('ul')[1]
IMDb_info = ul_info.get_text().replace('\t','').replace('\xa0','').replace('\r','').replace('\u3000','').replace('  ','').split('\n')

r = requests.get("http://app2.atmovies.com.tw/film/cast/"+movie_id+"/")
c = r.content
soup = BeautifulSoup(c,"html.parser")

actor_li = soup.find('div',class_='row').find('ul').find_all('li')
actor_all_text = ''
for actor in actor_li:
    actor_text = actor.get_text()
    actor_all_text = actor_all_text+actor_text
actor_all_text = actor_all_text.replace('\n　............','............')

r = requests.get('http://app2.atmovies.com.tw/eweekly/film/'+movie_id+'/')
c = r.content
soup = BeautifulSoup(c,"html.parser")

comment = '相關影評/專題文章:\n'
for com_html in soup.find_all('article',class_='box post'):
    comment = comment+com_html.header.h3.a.get_text()+' http://app2.atmovies.com.tw'+com_html.header.h3.a['href']+'\n'
    
r = requests.get('http://app2.atmovies.com.tw/news2/film/'+movie_id+'/')
c = r.content
soup = BeautifulSoup(c,"html.parser")

comment = comment+'相關新聞:\n'
for com_html in soup.find_all('article',class_='box post'):
    comment = comment+com_html.header.h3.a.get_text()+' http://app2.atmovies.com.tw'+com_html.header.h3.a['href']+'\n'

r = requests.get('http://cfapp.atmovies.com.tw/cfrating/film_ratingdata.cfm?filmid='+movie_id)
c = r.content
soup = BeautifulSoup(c,"html.parser")

td_rating = soup.table.find_all('td')
all_rate = '平均分數/總投票數:'+td_rating[1].get_text().replace('\xa0','')
good_rate = '覺得不錯:'+td_rating[2].get_text().replace('\xa0','')
bad_rate = '覺得普通:'+td_rating[3].get_text().replace('\xa0','')
like_rate = '讚數:'+td_rating[4].get_text().replace('\xa0','')

import os
path = "./開眼/"
if not os.path.isdir(path):
    os.mkdir(path)
f = open('開眼/'+'開眼電影網 '+title+'.txt','w',encoding = 'utf-8')
f.write('名稱 : '+title+'\n')
f.write(''+li_text+'\n')
for IM_info in IMDb_info:
    if IM_info ==''or IM_info =='IMDb':
        continue
    f.write(''+IM_info+'\n')

f.write('簡介 : '+des_top_str+des_down_str+'\n')
f.write(''+actor_all_text+'\n')

f.write(''+all_rate+'\n')
f.write(''+good_rate+'\n')
f.write(''+bad_rate+'\n')
f.write(''+like_rate+'\n')
f.write(''+comment+'\n')

f.close()