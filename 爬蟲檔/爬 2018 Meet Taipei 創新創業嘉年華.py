import requests
from bs4 import BeautifulSoup
r = requests.get('https://meettaipei.tw/exhibition.php')
c = r.content
soup = BeautifulSoup(c,"html.parser")

company_dict = {
    
}
num = 0
for i in soup.find_all(class_ = 'booths animation all I'):
    company_dict[num] = {}
    
    company_dict[num]['company_name'] = i.find(class_ = "booth-company").get_text()
    company_dict[num]['company_product'] = i.find(class_ = "booth-title").get_text()
    company_dict[num]['company_summary'] = i.find(class_ = "booth-summary").get_text()
    num+=1

for i in soup.find_all(class_ = 'booths animation all F'):
    company_dict[num] = {}
    
    company_dict[num]['company_name'] = i.find(class_ = "booth-company").get_text()
    company_dict[num]['company_product'] = i.find(class_ = "booth-title").get_text()
    company_dict[num]['company_summary'] = i.find(class_ = "booth-summary").get_text()
    num+=1
for i in soup.find_all(class_ = 'booths animation all M'):
    company_dict[num] = {}
    
    company_dict[num]['company_name'] = i.find(class_ = "booth-company").get_text()
    company_dict[num]['company_product'] = i.find(class_ = "booth-title").get_text()
    company_dict[num]['company_summary'] = i.find(class_ = "booth-summary").get_text()
    num+=1
for i in soup.find_all(class_ = 'booths animation all C'):
   
    company_dict[num] = {}
    
    company_dict[num]['company_name'] = i.find(class_ = "booth-company").get_text()
    company_dict[num]['company_product'] = i.find(class_ = "booth-title").get_text()
    company_dict[num]['company_summary'] = i.find(class_ = "booth-summary").get_text()
    num+=1
    
for i in soup.find_all(class_ = 'booths animation all T'):
   
    company_dict[num] = {}
    
    company_dict[num]['company_name'] = i.find(class_ = "booth-company").get_text()
    company_dict[num]['company_product'] = i.find(class_ = "booth-title").get_text()
    company_dict[num]['company_summary'] = i.find(class_ = "booth-summary").get_text()
    num+=1
for i in soup.find_all(class_ = 'booths animation all A'):
   
    company_dict[num] = {}
    
    company_dict[num]['company_name'] = i.find(class_ = "booth-company").get_text()
    company_dict[num]['company_product'] = i.find(class_ = "booth-title").get_text()
    company_dict[num]['company_summary'] = i.find(class_ = "booth-summary").get_text()
    num+=1
for i in soup.find_all(class_ = 'booths animation all H'):
   
    company_dict[num] = {}
    
    company_dict[num]['company_name'] = i.find(class_ = "booth-company").get_text()
    company_dict[num]['company_product'] = "N/A"
    company_dict[num]['company_summary'] = i.find(class_ = "booth-summary").get_text()
    num+=1
for i in soup.find_all(class_ = 'booths animation all X'):
   
    company_dict[num] = {}
    
    company_dict[num]['company_name'] = i.find(class_ = "booth-company").get_text()
    company_dict[num]['company_product'] = i.find(class_ = "booth-title").get_text()
    company_dict[num]['company_summary'] = i.find(class_ = "booth-summary").get_text()
    num+=1
for i in soup.find_all(class_ = 'booths animation all TL'):
   
    company_dict[num] = {}
    
    company_dict[num]['company_name'] = i.find(class_ = "booth-company").get_text()
    company_dict[num]['company_product'] = i.find(class_ = "booth-title").get_text()
    company_dict[num]['company_summary'] = i.find(class_ = "booth-summary").get_text()
    num+=1

import csv
with open('company_2018 Meet Taipei 創新創業嘉年華.csv', 'w', newline='',encoding = "utf-8") as csvfile:
  # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile,delimiter='#')

  # 寫入一列資料
    writer.writerow(['團隊名稱','產品名稱','產品/團隊介紹'])
    for num in range(len(company_dict)):
        
        writer.writerow([company_dict[num]['company_name'],company_dict[num]['company_product'],company_dict[num]['company_summary']])