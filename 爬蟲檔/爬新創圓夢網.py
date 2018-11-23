import requests
from bs4 import BeautifulSoup
import json
# 資料
headers = {
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Content-Length': '68',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': '_ga=GA1.3.1583127732.1542608103; _gid=GA1.3.1088398644.1542608103; __zlcmid=pShnqZzvDQFArv',
    'Host': 'sme.moeasmea.gov.tw',
    'If-Modified-Since': 'Thu, 01 Jan 1970 00:00:00 GMT',
    'Origin':'http://sme.moeasmea.gov.tw',
    'Referer': 'http://sme.moeasmea.gov.tw/Startup/modules/highlight/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}
company_dict = {
    
}
num = 0
for page in range(1,7,1):
    my_data = {
        "pageIndex": page,
        "data1":"" ,
        "data2":"" ,
        "data3": "科技產業"}

    # 將資料加入 POST 請求中
    r = requests.post('http://sme.moeasmea.gov.tw/Startup/modules/highlight/getdata1.php', data = my_data,headers = headers)

    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    data = soup.get_text()
    if page == 5:
        data2 = str(data).replace('\\\"','\"').replace('\"[','[').replace(']\"',']').replace('\"\"Green Shepherd\"','\"\\\"Green Shepherd\\\"')

        jsondata = json.loads(data2)
    elif page == 3:
        data2 = str(data).replace('\"\\u59d4','\\\"\\u59d4').replace('\"\\u7684','\\\"\\u7684')
        jsondata = json.loads(data2)
    else:
        jsondata = json.loads(data)
    for i in range(len(jsondata['dataRecords'])):
        company_dict[num] = {}
        company_dict[num]['company_name'] = jsondata['dataRecords'][i]['company']
        try:
            jsondata2 = json.loads(jsondata['dataRecords'][i]['data_records'].replace('\"委託製造\"','\\\"委託製造\\\"',))
        except:
            jsondata2 = jsondata['dataRecords'][i]['data_records']
        company_dict[num]['company_set_up'] = jsondata2[0]['value'][0]['value']


        company_dict[num]['company_owner'] = jsondata2[0]["value"][1]["value"]
        company_dict[num]['company_category'] = jsondata2[0]["value"][5]["value"]
        company_dict[num]['company_summary'] = jsondata2[1]["value"][0]["value"].replace('</span>','').replace('</p>','')
        num+=1
import csv
with open('company_新創圓夢網.csv', 'w', newline='',encoding = "utf-8") as csvfile:
  # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile,delimiter='#')

  # 寫入一列資料
    writer.writerow(['團隊名稱','成立時間','負責人','團隊分類','團隊簡介'])
    for num in range(len(company_dict)):
        
        writer.writerow([company_dict[num]['company_name'],company_dict[num]['company_set_up'],company_dict[num]['company_owner'],company_dict[num]['company_category'],company_dict[num]['company_summary']])