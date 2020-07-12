#coding:utf-8

import requests

url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language':'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'pgv_pvid=7838988661; ptcz=a749c13713fc703b48592a49922470ed1eda1bcc7b68d2cf5be6fa79c731b76d; pgv_pvi=9718182912; RK=vkrweAJtMM; o_cookie=763074310; pac_uid=1_763074310; luin=o0763074310; lskey=000100007d08c463d9cc757cc4c5ae2cf3732897a65bf7de58e88b9524158f61b02e143bcf6124869366ea7d; tvfe_boss_uuid=e1c916f5e5e6e6bd; _txjk_whl_uuid_aa5wayli=58f307f1d8264ccb8aeb92b2f6225b14',
    'referer': 'https://news.qq.com/zt2020/page/feiyan.htm',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36 Edg/83.0.478.61'
}

response = requests.get(url, headers=headers)

print(response.text)