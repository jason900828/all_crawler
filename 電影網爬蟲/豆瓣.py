import requests
from bs4 import BeautifulSoup
html = "https://movie.douban.com/subject/26994755/"
r = requests.get(html)
c = r.content
soup = BeautifulSoup(c,"html.parser")

a = str(soup.find_all('script')).find('application/ld+json')
content = str(soup.find_all('script'))[a+21:]
b = content.find('</script>')
content = content[:b].replace('\n','')

import json
jsondata = json.loads(content)

info = soup.find('div',id='info')
info_text = info.get_text()

info_list = str(info_text).split('\n')
info_dict = {
    
}
for i in info_list:
    info_key_value = i.split(':')
    if info_key_value == ['']:
        continue
    info_dict[info_key_value[0]] = info_key_value[1]


des = soup.find('div',id='link-report')
des_text = des.get_text().replace('\n','').replace('\u3000','').replace(' ','')

info_dict['簡介'] = des_text
info_dict['豆瓣評分'] = {}
    
info_dict['豆瓣評分']['評分總數'] = jsondata['aggregateRating']['ratingCount']
info_dict['豆瓣評分']['最高評分'] = jsondata['aggregateRating']['bestRating']
info_dict['豆瓣評分']['最低評分'] = jsondata['aggregateRating']['worstRating']
info_dict['豆瓣評分']['評分平均'] = jsondata['aggregateRating']['ratingValue']
info_dict['名稱'] = jsondata['name']

review = '影評 : \n'
for rev in soup.find('div',class_='review-list').find_all('div',class_='main review-item'):
    
    
    review = review+rev.find('a',class_='name').get_text()+' '
    review = review+rev.find('span',class_ = 'main-meta').get_text()+'\n'
    review = review+rev.find('span',class_ = 'main-meta').previous_sibling.previous_sibling['class'][0]+'\n'
    review = review+rev.find('div',class_='short-content').get_text()+'\n'

comment = '短評 : \n'
for com in soup.find('div',id='comments-section').find_all('div',class_='comment'):#comments-section
    for sub_com in com.find_all('span',class_='comment-info'):
        comment = comment+sub_com.get_text().replace('\n','').replace(' ','')+'\n'
    comment = comment+com.find('span',class_ = 'comment-time').previous_sibling.previous_sibling['class'][0]+'\n'
    comment = comment+com.find('span',class_='short').get_text()+'\n'

r = requests.get(html+"awards/")
c = r.content
soup = BeautifulSoup(c,"html.parser")

awards = '得獎 : '
for awards_html in soup.find_all('div',class_='awards'):
    awards = awards+awards_html.h2.get_text().replace('\n','')+'---'+awards_html.ul.get_text().replace('\n','')

r = requests.get(html+"celebrities")
c = r.content
soup = BeautifulSoup(c,"html.parser")

worker = ''
for worker_html in soup.find_all('div',class_="list-wrapper"):
    worker = worker+worker_html.h2.get_text()+' : '
    for worker_name in worker_html.ul.find_all('li'):
        worker = worker+worker_name.a['title']+'、'
    worker = worker+'\n'

import os
path = "./豆瓣/"
if not os.path.isdir(path):
    os.mkdir(path)
f = open('豆瓣/'+'豆瓣 '+info_dict['名稱']+'.txt','w',encoding='utf-8')
f.write('名稱 : '+info_dict['名稱']+'\n')
f.write(worker+'\n')
f.write('类型 : '+info_dict['类型']+'\n')
f.write('官方网站 : '+info_dict['官方网站']+'\n')
f.write('制片国家/地区 : '+info_dict['制片国家/地区']+'\n')
f.write('语言 : '+info_dict['语言']+'\n')
f.write('上映日期 : '+info_dict['上映日期']+'\n')
f.write('片长 : '+info_dict['片长']+'\n')
f.write('又名 : '+info_dict['又名']+'\n')
f.write('IMDb链接 : '+info_dict['IMDb链接']+'\n')
f.write('豆瓣評分 : \n')
for key in info_dict['豆瓣評分']:
    f.write(key+' : '+info_dict['豆瓣評分'][key]+'\n')
f.write('簡介 : '+info_dict['簡介']+'\n')
f.write(comment+'\n')
f.write(review+'\n')
f.write(awards+'\n')
f.close()