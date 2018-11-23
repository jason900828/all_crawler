import requests
from bs4 import BeautifulSoup
r = requests.get('https://tec.ntu.edu.tw/teams/')
c = r.content
soup = BeautifulSoup(c,"html.parser")

num = 0
company_dict = {}
for i in soup.find_all(class_ = "esg-media-cover-wrapper"):
    content = ''
    company_dict[num] = {
        '團隊名稱':'N/A',
        '官方網站':'N/A',
        '產品名稱':'N/A',
        '團隊簡介':'N/A'
    }
    for j in i.find_all("p"):
        #print(j)
        
        if '團隊名稱' in str(j.contents[0]):
            company_dict[num]['團隊名稱'] = j.contents[-1].string.replace('\n','')
        elif '官方網站' in str(j.contents[0]):
            company_dict[num]['官方網站'] = j.contents[-1].string.replace('\n','')
        elif '產品名稱' in str(j.contents[0]):
            company_dict[num]['產品名稱'] = j.contents[-1].string.replace('\n','')
        elif '團隊簡介' in str(j.contents[0]):
            for s in j.strings:
                content = content+s
            company_dict[num]['團隊簡介'] = content.replace('團隊簡介\n','').replace('\n','')
    num +=1

import csv
with open('company_台大創創中心.csv', 'w', newline='',encoding = "utf-8") as csvfile:
  # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile,delimiter='#')

  # 寫入一列資料
    writer.writerow(['團隊名稱','官方網站','產品名稱',"團隊簡介"])
    for num in range(len(company_dict)):
        
        writer.writerow([company_dict[num]['團隊名稱'],company_dict[num]['官方網站'],company_dict[num]['產品名稱'],company_dict[num]['團隊簡介']])