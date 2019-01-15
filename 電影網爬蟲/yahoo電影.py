import requests
from bs4 import BeautifulSoup
html = 'https://movies.yahoo.com.tw/movieinfo_main/%E7%8F%AD%E6%81%A9%E5%9B%9E%E5%AE%B6-ben-is-back-8863'
r = requests.get(html)
c = r.content
soup = BeautifulSoup(c,"html.parser")

title = soup.find('div',class_='movie_intro_info_r').h1.get_text()

info = ''
a_info = []
a_info_where = [0]
for i in soup.find('div',class_="movie_intro_info_r").children:
    if i == '\n':
        continue
    if i in soup.find_all('div',class_="movie_intro_list"):
        a_info.append(i.get_text().replace('\n','').replace(' ',''))
        a_info_where.append(len(info))
        continue
    info+=i.get_text().replace('\u3000','').replace(' ','')+'\n'   
a_info_where.append(-1)
info_temp = ''
for a in range(len(a_info)):
    info_temp = info_temp+info[a_info_where[a]:a_info_where[a+1]]+a_info[a]+'\n'
info_temp_lst = info_temp.split('\n')
info = ''
for info_ in info_temp_lst:
    if info_!='':
        info = info+info_+'\n'

def do_selenium(html):
    from selenium import webdriver
    browser = webdriver.Chrome( executable_path='./chromedriver.exe')

    browser.get(html)
    clk = browser.find_element_by_class_name('plus_arr')
    clk.click()
    soup = BeautifulSoup(browser.page_source,"html.parser")

    Introduction = soup.find('div',class_="gray_infobox_inner").span.get_text()
    browser.close()
    return Introduction

article = '相關文章: \n'
comment = '網友短評: \n'
done = 0
for i in soup.find_all('div',class_='l_box _c'):
    
    if soup.find('div',class_="plus_arr")!=None and done == 0:
        if 'style' not in soup.find('div',class_="plus_arr").parent.attrs.keys():
            more_intro = do_selenium(html)
            done = 1

    else:
        if i.find('div',class_='title')!=None:
            
            if i.find('div',class_='title').get_text().replace(' ','').replace('\n','')=='劇情介紹':
                more_intro =i.find('div',class_='l_box_inner').span.get_text()
                find_txt = soup.find('div',class_='btn_gray_info gabtn').previous_sibling
                while True:
                    if find_txt == '\n' or find_txt == '\r\n\xa0':
                        find_txt = find_txt.previous_sibling
                    else:
                        more_intro = more_intro+find_txt
                        break
            elif i.find('div',class_='title').span.get_text().replace(' ','').replace('\n','')=='相關文章':
                
                for article_html in i.ul.find_all('li'):
                    article = article+article_html.h2.get_text() +' '+str(article_html.a['href'])+'\n'


import os
path = "./yahoo/"
if not os.path.isdir(path):
    os.mkdir(path)
file_name =title+' Yahoo電影.txt'
f = open('yahoo/'+file_name,'w',encoding='utf-8')
f.write(info+'\n')
f.write('劇情介紹'+more_intro+'\n')
f.write(article+'\n')
f.write(comment+'\n')

f.close()