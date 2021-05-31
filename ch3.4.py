#-*- codeing = utf-8 -*- 
#@Time: 2021/4/24 10:42
#@Author : dapao
#@File : ch3.4.py
#@Software: PyCharm

import requests

def get_one_page(url):
    headers = {
        "User-Agent":'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 90.0.4430.85 Safari / 537.36'
    }
    response  = requests.get(url,headers=headers)
    if response.status_code ==200:
        return response.text
    return None


def main():
    url = 'https://maoyan.com/board/4'
    html = get_one_page(url)
    print(html)

if __name__ == '__main__':
    main()


