import requests
from bs4 import BeautifulSoup
r = requests.get('https://www.tiectw.com/sv-alumni/')
c = r.content
soup = BeautifulSoup(c,"html.parser")

company_dict={}
num = 0
for i in soup.find_all(class_ = "Txt clearfix "):
    company_dict[num] = {}
    company_dict[num]["company_name"] = i.h3.string
    company_dict[num]["company_url"] = i.h3.a['href']
    num+=1

r = requests.get('https://www.tiectw.com/pm-alumni/')
c = r.content
soup = BeautifulSoup(c,"html.parser")
for i in soup.find_all(class_ = "Txt clearfix "):
    company_dict[num] = {}
    company_dict[num]["company_name"] = i.h3.string
    company_dict[num]["company_url"] = i.h3.a['href']
    num+=1
import csv
with open('company_台灣創新創業中心.csv', 'w', newline='',encoding = "utf-8") as csvfile:
  # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile,delimiter='#')

  # 寫入一列資料
    writer.writerow(['團隊名稱','官方網站'])
    for num in range(len(company_dict)):
        
        writer.writerow([company_dict[num]['company_name'],company_dict[num]['company_url']])