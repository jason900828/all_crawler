import requests
from bs4 import BeautifulSoup
r = requests.get('https://ustart.yda.gov.tw/files/11-1000-97.php')
c = r.content
soup = BeautifulSoup(c,"html.parser")
num = 0
company_list = []
for i in soup.find(class_ = 'ptcontent clearfix floatholder').find_all(style="font-size:14px;"):
    if num>4:
        if num%3 == 1:
            company_list.append(i.get_text())
        if num%3 == 2:
            if int(i.get_text())<104:
                break
    num+=1
import csv
with open('company_教育部青年署U-start創新創業計畫.csv', 'w', newline='',encoding = "utf-8") as csvfile:
  # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile,delimiter='#')

  # 寫入一列資料
    writer.writerow(['團隊名稱'])
    for num in range(len(company_list)):
        
        writer.writerow([company_list[num]])