import pandas as pd
doc_name = input("輸入檔名：")
tag_name = input("輸入讀取位置：")

df = pd.read_excel(doc_name)

all_company = df[tag_name]
all_comp = []
for i in all_company:
    all_comp.append(i.replace('\n',''))

num = 0
for i in all_comp:
    print(str(num)+","+i)
    num+=1

import requests
from bs4 import BeautifulSoup
import json
repeat = []
num = 0

data_company = {}

for name in all_comp:
    already_insert = 0
    r = requests.get('http://company.g0v.ronny.tw/api/search?q='+ name.replace('有限公司',''))  
    c = r.content
    jsondata = json.loads(c)
    
    
    print(num,name)
    num +=1
    data_company[num] = {
        "公司狀況":"N/A",
        "統一編號":"N/A",
        "公司所在地":"N/A",
        "代表人姓名":"N/A",
        "核准設立日期":"N/A",
        "公司名稱":"N/A",
        "資本總額":"N/A"
    }
    if int(jsondata['found'])>1 :
        for i in range(jsondata['found']):
            if i>9:
                #print('多餘10個資料')
                break
            dict_key = jsondata["data"][i].keys()
            dict_company = jsondata["data"][i]
            if "公司名稱" in dict_key: 
                if name in dict_company['公司名稱'] and (dict_company['公司狀況'] =='核准設立' or dict_company['公司狀況'] =='核准認許'):
                    data_company[num]['公司名稱'] = dict_company['公司名稱']
                    data_company[num]['公司狀況'] = dict_company['公司狀況']
                    data_company[num]['統一編號'] = dict_company['統一編號']
                    already_insert = 1
                if "資本總額(元)" in dict_key:
                    data_company[num]['資本總額'] = dict_company['資本總額(元)']
                elif '在中華民國境內營運資金'in dict_key:
                    data_company[num]['資本總額'] = dict_company['在中華民國境內營運資金']
                if '公司所在地' in dict_key:
                    data_company[num]['公司所在地'] = dict_company['公司所在地']
                elif '分公司所在地' in dict_key:
                    data_company[num]['公司所在地'] = dict_company['分公司所在地']
                if '代表人姓名' in dict_key:
                    data_company[num]['代表人姓名'] = dict_company['代表人姓名']
                elif '訴訟及非訴訟代理人姓名' in dict_key:
                    data_company[num]['代表人姓名'] = dict_company['訴訟及非訴訟代理人姓名']
                if '核准設立日期' in dict_key:
                    data_company[num]['核准設立日期'] = str(dict_company['核准設立日期']['year'])+'/'+str(dict_company['核准設立日期']['month'])+'/'+str(dict_company['核准設立日期']['day'])
                elif '核准認許日期'  in dict_key:
                    data_company[num]['核准設立日期'] = str(dict_company['核准認許日期']['year'])+'/'+str(dict_company['核准認許日期']['month'])+'/'+str(dict_company['核准認許日期']['day'])
                
                    
            elif '商業名稱' in dict_key:
                if dict_company['商業名稱'] == name and jsondata['data'][i]['現況'] == '核准設立':
                    data_company[num]['公司名稱'] = dict_company['商業名稱']
                    data_company[num]['公司狀況'] = dict_company['現況']
                    data_company[num]['統一編號'] = dict_company['統一編號']
                    data_company[num]['資本總額'] = dict_company['資本額(元)']
                    data_company[num]['公司所在地'] = dict_company['地址']
                    data_company[num]['代表人姓名'] = dict_company['負責人姓名']
                    data_company[num]['核准設立日期'] = str(dict_company['核准設立日期']['year'])+'/'+str(dict_company['核准設立日期']['month'])+'/'+str(dict_company['核准設立日期']['day'])
                    already_insert = 1
                    
            else:
                data_company[num]['公司名稱'] = name
                data_company[num]['公司狀況'] = '資料不好讀取'
                already_insert = 1

    elif jsondata['found'] == 1:
        dict_key = jsondata["data"][0].keys()
        dict_company = jsondata["data"][0]
        if "公司名稱" in dict_key: 
            if name in dict_company['公司名稱'] and dict_company['公司狀況'] =='核准設立':
                data_company[num]['公司名稱'] = dict_company['公司名稱']
                data_company[num]['公司狀況'] = dict_company['公司狀況']
                data_company[num]['統一編號'] = dict_company['統一編號']
                already_insert = 1
            if "資本總額(元)" in dict_key:
                data_company[num]['資本總額'] = dict_company['資本總額(元)']
            elif '在中華民國境內營運資金'in dict_key:
                data_company[num]['資本總額'] = dict_company['在中華民國境內營運資金']
            if '公司所在地' in dict_key:
                data_company[num]['公司所在地'] = dict_company['公司所在地']
            elif '分公司所在地' in dict_key:
                data_company[num]['公司所在地'] = dict_company['分公司所在地']
            if '代表人姓名' in dict_key:
                data_company[num]['代表人姓名'] = dict_company['代表人姓名']
            elif '訴訟及非訴訟代理人姓名' in dict_key:
                data_company[num]['代表人姓名'] = dict_company['訴訟及非訴訟代理人姓名']
            if '核准設立日期' in dict_key:
                data_company[num]['核准設立日期'] = str(dict_company['核准設立日期']['year'])+'/'+str(dict_company['核准設立日期']['month'])+'/'+str(dict_company['核准設立日期']['day'])
            elif '核准認許日期'  in dict_key:
                data_company[num]['核准設立日期'] = str(dict_company['核准認許日期']['year'])+'/'+str(dict_company['核准認許日期']['month'])+'/'+str(dict_company['核准認許日期']['day'])
            
                    
        elif '商業名稱' in dict_key:
            if dict_company['商業名稱'] == name and jsondata['data'][i]['現況'] == '核准設立':
                data_company[num]['公司名稱'] = dict_company['商業名稱']
                data_company[num]['公司狀況'] = dict_company['現況']
                data_company[num]['統一編號'] = dict_company['統一編號']
                data_company[num]['資本總額'] = dict_company['資本額(元)']
                data_company[num]['公司所在地'] = dict_company['地址']
                data_company[num]['代表人姓名'] = dict_company['負責人姓名']
                data_company[num]['核准設立日期'] = str(dict_company['核准設立日期']['year'])+'/'+str(dict_company['核准設立日期']['month'])+'/'+str(dict_company['核准設立日期']['day'])
                already_insert = 1
                    
        else:
            data_company[num]['公司名稱'] = name
            data_company[num]['公司狀況'] = '資料不好讀取'
            already_insert = 1
        
    if already_insert == 0:
        print("查不到===================================================================================")

with open('new_company_infor.csv', 'w', newline='',encoding = 'utf-8') as csvfile:

  # 以空白分隔欄位，建立 CSV 檔寫入器
    writer = csv.writer(csvfile, delimiter='#')

    writer.writerow(['公司名稱', '公司狀況', '統一編號','資本總額(元)','公司所在地','代表人姓名','核准設立日期'])
    
    
    for i in range(len(data_company)):
        infor = data_company[i]
        writer.writerow([infor['公司名稱'],infor['公司狀況'],infor['統一編號'],infor['資本總額'],infor['公司所在地'], infor['代表人姓名'],infor['核准設立日期']])