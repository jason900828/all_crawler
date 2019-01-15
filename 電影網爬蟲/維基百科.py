import requests
from bs4 import BeautifulSoup
r = requests.get("https://zh.wikipedia.org/wiki/%E6%B0%B4%E8%A1%8C%E4%BF%A0_(%E9%9B%BB%E5%BD%B1)")
c = r.content
soup = BeautifulSoup(c,"html.parser")

title = soup.title.get_text()

Introduction_info_tag = soup.table.find_all('th',scope="row")
Introduction_info_content = soup.table.find_all('td',style="")
Introduction_info = ''
for i in range(len(Introduction_info_tag)):
    Introduction_info = Introduction_info + Introduction_info_tag[i].get_text()+' : '
    Introduction_info = Introduction_info + Introduction_info_content[i].get_text().replace('\n',' ')+'\n'


all_table_info = []
content_table_at = []
content = ''
for info in soup.find('div',class_="mw-parser-output").children:
    if type(info)==str:
        info = info.next_sibling
        continue
    if  info.name == None:
        info = info.next_sibling
        continue
    if  info == soup.find('table',class_="infobox vevent"):
        info = info.next_sibling
        continue
    if info == soup.find('div',class_="reflist columns references-column-width"):
        break  
    if info in soup.find_all('h2') :
        content = content +'\n'+ '='*50 +'\n'
                
                
    if info == soup.find('div',id="toc"):
        info = info.next_sibling
        continue
    
    if info.get_text() == '參考文獻[编辑]' or info.get_text() == '参考资料[编辑]':
        info = info.next_sibling
        break
    if info in soup.find_all('table',class_="wikitable"):
        i=0
        table_info = []
        content_table_at.append(len(content))
        for tr_ in info.find_all('tr'):
            if tr_.find_all('th') !=[]:
                table_info.append(tr_.find_all('th'))
            if  tr_.find_all('td')!=[]:   
                table_info.append(tr_.find_all('td'))
        index = 0
        jump = 0
        for t_info in table_info:
            if jump>0:
                jump=jump-1
                index+=1
                continue
            for t in range(len(t_info)):
                if 'rowspan' in t_info[t].attrs:
                    jump = int(t_info[t]['rowspan'])
                    for pause in range(1,jump):
                        table_info[index+pause].insert(t,t_info[t])
                    jump = jump-1
            index+=1
        for t_info in table_info:
            for t in range(len(t_info)):
                t_info[t] = t_info[t].get_text().replace('\n','')
        all_table_info.append(table_info)
        
        info = info.next_sibling
        continue
        
    content = content + info.get_text().replace('[编辑]',':')
    info = info.next_sibling
content_table_at.append(-1)

import os
path = "./維基/"
if not os.path.isdir(path):
    os.mkdir(path)
f = open('維基/'+title+'.txt','w',encoding='utf-8')
f.write(title+'\n')
f.write(Introduction_info+'\n')
f.write(content[0:content_table_at[0]]+'\n')
for t in range(len(all_table_info)):
    
    for tb_list in all_table_info[t]:
        for tb_write in tb_list:
            f.write(tb_write+'\t')
        f.write('\n')
    
    f.write(content[content_table_at[t]:content_table_at[t+1]]+'\n')
    f.write('\n')
f.close()