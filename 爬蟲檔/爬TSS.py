import requests
from bs4 import BeautifulSoup
r = requests.get("https://www.startupstadium.tw/startups/")
c = r.content
soup = BeautifulSoup(c,"html.parser")

company_dict = {
    
}
number = 0
for i in soup.find_all(class_ = "summary-content sqs-gallery-meta-container"):
    
    
    j = i.find(class_ = "summary-metadata summary-metadata--primary")
    category = ''
    for k in j.find_all("a"):
        category = category+","+k.string
    company_dict[number] = {
        "company_name":i.find(class_="summary-title-link").string,
        "company_content":category
    }
    number+=1
import csv
with open('company_TSS.csv', 'w', newline='',encoding = "utf-8") as csvfile:
  # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile,delimiter='#')

  # 寫入一列資料
    writer.writerow(['團隊名稱',"團隊簡介"])
    for num in range(len(company_dict)):
        
        writer.writerow([company_dict[num]['company_name'],company_dict[num]['company_content']])