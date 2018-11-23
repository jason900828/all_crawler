import requests
from bs4 import BeautifulSoup
company_list = []  
url_list = []
for p in range(1,47):
    r = requests.get("https://meethub.bnext.com.tw/base/page/"+str(p))
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    data = soup.find_all("article")
    
    for a in data:
        htm = a.h2.a
        company_list.append(htm.get_text())
        url_list.append(htm['href'])

count = 0
company_introduce = {}
for com in company_list:
    
    company_introduce[com] = {
        '團隊基本資料':{
            '團隊名稱':'N/A',
            '成立時間':'N/A',
            '公司地區':'N/A',
            '產業類型':'N/A',
            '募資階段':'N/A',
            '員工人數':'N/A',
            '發展階段':'N/A',
            '募資金額':'N/A'
        },
        '產品／服務資料':{
            '中文名稱':'N/A',
            '英文名稱':'N/A',
            '上線時間':'N/A',
            '主要市場':'N/A'
        },
        '團隊簡介':'N/A'
    }
    r = requests.get(url_list[count])
    count+=1
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    div_ = soup.div
    
    company_tag = []
    company_value = []
    company_subtitle = []
    cut = []
    for all_c in div_.find_all('td'):
        #if all_c =="col-xs-12 col-sm-8 col-md-8 col-lg-8 base-header-center":
        #print(all_c)\
        
        if 'class'in all_c.attrs.keys():
            class_tag = all_c['class'][0]
        else:
            continue

        if "base-header-label" == class_tag:
            company_tag.append(all_c.get_text())
            
        elif "base-header-meta-value" == class_tag:
            company_value.append(all_c.get_text())
            
        elif  "base-subtitle" == class_tag:
            company_subtitle.append(all_c.get_text())
            cut.append(len(company_tag))
            
    cut.append(len(company_tag))       
    
    for top in range(len(company_subtitle)) :
        for i in range(cut[top],cut[top+1]):
            company_introduce[com][company_subtitle[top]][company_tag[i]] = company_value[i].replace('<br/>','\n')
            
    content = ''       
    for content_htm in soup.find_all('div',class_= "col-xs-12 col-sm-12 col-md-12 col-lg-12"):
        p_htm = content_htm.find_all("p")
        p_htm_del = content_htm.find_all("p",class_= "news_og-description")
        for p in p_htm:
            if p in p_htm_del:
                continue
            content = content+p.get_text()
    company_introduce[com]['團隊簡介'] = content
    
    print(count,com+' done!!')
print(company_introduce)



import csv
with open('company_創業小聚.csv', 'w', newline='',encoding = "utf-8") as csvfile:
  # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile,delimiter='#')

  # 寫入一列資料
    writer.writerow(['團隊名稱','產業類型',"團隊簡介"])
    for com in company_list:
        writer.writerow([com,company_introduce[com]['團隊基本資料']['產業類型'],company_introduce[com]['團隊簡介']])