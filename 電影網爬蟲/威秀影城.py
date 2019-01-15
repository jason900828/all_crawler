import requests
from bs4 import BeautifulSoup
html = ''
r = requests.get(html)
c = r.content
soup = BeautifulSoup(c,"html.parser")

title = soup.find('div',class_='titleArea').h1.get_text()
info = soup.find('div',class_='titleArea').get_text()

for info_detail in soup.find('div',class_='infoArea').table.find_all('tr'):
    info =  info+info_detail.get_text().replace('\n','')+'\n'

introdution = ''
for i in soup.find('div',class_='bbsArticle').find_all('p'):
    introdution = introdution +i.get_text()

import os
path = "./威秀/"
if not os.path.isdir(path):
    os.mkdir(path)
file_name =title+' 威秀影城.txt'
f = open('威秀/'+file_name,'w',encoding='utf-8')
f.write(info+'\n')
f.write('劇情介紹'+introdution+'\n')
f.close()