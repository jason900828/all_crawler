import requests
from bs4 import BeautifulSoup
r = requests.get("https://appworks.tw/investments/")
c = r.content
soup = BeautifulSoup(c,"html.parser")
company_dict = {
    
}
number = 0
for i in soup.find_all(class_ = "vc_row wpb_row vc_inner vc_row-fluid invest-block"):
    company_dict[number] = {
        "company_name" : i.h3.string,
        "company_content":str(i.p).replace("<p>","").replace("</p>","").replace('\n','')
    }
    number += 1
import csv
with open('company_appworks.csv', 'w', newline='',encoding = "utf-8") as csvfile:
  # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile,delimiter='#')

  # 寫入一列資料
    writer.writerow(['團隊名稱',"團隊簡介"])
    for num in range(len(company_dict)):
        
        writer.writerow([company_dict[num]['company_name'],company_dict[num]['company_content']])
