#破解百度翻译


import requests

import json

from requests.api import post


if __name__ == "__main__":
    #1指定url
    post_url = "https://fanyi.baidu.com/sug"
    #进行UA伪装
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36"
    }
    #3.post请求参数处理（同get请求一样）
    word = input("input a word:")
    data = {
        'kw': word
    }
    #4.请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #5.获取响应数据：json（）方法返回的obj（如果确认响应的数据类型为json，才可以使用。json（）
    dic_obj = response.json()

    #持久化存储
    filename  = word+".json"
    fp = open(f"bilibili/{filename}",'w',encoding='utf-8')
    json.dump(dic_obj,fp=fp,ensure_ascii=False)
    print('over!')
