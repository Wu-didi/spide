#肯德基店名查询

import requests
import json

if __name__ == "__main__":
    url = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword"
    para = {
        "cname":"", 
        "pid": "",
        "keyword": "南京",
        "pageIndex": "1",
        "pageSize": "10"
    }
     #进行UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    response = requests.get(url=url,params=para,headers=headers)
    list_data = response.json()
    fp = open("./kfc",'w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)
    print('over!')

