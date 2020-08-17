import requests
from lxml import etree


def do():
    url = "https://www.kancloud.cn/gredsea/lly_api_v1/1210962"

    response = requests.get(url)
    data = response.content
    html = etree.HTML(data)
    html_data = html.xpath('//li/a/@href')
    print(html_data)
    getMd(html_data)


def getMd(html_data):
    for id in html_data:
        url = 'https://www.kancloud.cn/gredsea/lly_api_v1/' + id
        headers = {
            'accept': 'application/json, text/plain, */*',
            'Cookie': '__jsluid_s=952843fdd161b31cafd823dec0968abf; _ga=GA1.2.992453570.1587109996; remember_cc248a61b22205317666319f4fffa9146988fb4b=436861%7CJro4WfvrR2ppGKlLVZZR7NFbDdgUFJknZefXATn9gsqvu1HeqNEXV6u4pyAL; PHPSESSID=87278ko2ngk0gefa370ml63e0h; _gid=GA1.2.46821517.1591924814; intercom-session-lw0ts0bk=TE9BYkN2UkVEa1lUMUtSV05FT1N6eldXS2t2cU9OK0MzeFdTRkZ6S2NGRWRDdFJidDVSZEZQQTVJQ0NHVHBQbi0tY1IrSWF1VnFaQUpBZmxGaHV6RGhIZz09--4542d8ff939c28ab2d5d85f79e6227e5c4586b2f; _gat_web=1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
            'Origin': 'www.kancloud.cn',
            'Referer': 'https://www.kancloud.cn/gredsea/lly_api_v1/' + str(id),
            'Content-Type': 'application/json',
        }

        response = requests.get(url=url, headers=headers)
        data = response.json()
        saveMd(data)


def saveMd(data):
    url = 'http://192.168.8.93:4999/server/index.php?s=/api/page/save'
    headers = {
        'accept': 'text/html; charset=UTF-8',
        'Cookie': 'cookie_token=cfbbf168058873a645e394b6116facee1d2ba8414152907ea0d070d1fd16f2f9; XXL_JOB_LOGIN_IDENTITY=7b226964223a312c22757365726e616d65223a2261646d696e222c2270617373776f7264223a226531306164633339343962613539616262653536653035376632306638383365222c22726f6c65223a312c227065726d697373696f6e223a6e756c6c7d; lang=zh; token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6Ijk2NTQ3OTA0MUBxcS5jb20iLCJpYXQiOjE1OTUyMDg1NzgsInVzZXJuYW1lIjoiaHVhbmd3ZW5yb25nIn0.8B9a5KVDBuyrUeV4Sr1kUx4Q79oDT1Yqf1l9Dsl6UtU; currentUser=huangwenrong; currentUser.sig=9YvL-rvLgvrT9PRCbXN-5-GO3zA; JSESSIONID=c67cabaf-e673-40d1-a6ce-21aba74fd879; think_language=zh-CN; PHPSESSID=a40e52ff8cdbc346cb999f79722048a4',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
        'Connection': 'keep-alive',
        'Accept-Encoding': 'gzip, deflate, br',
        'Host': '192.168.8.90:31414',
        'Origin': 'http://192.168.8.90:31414',
        'Referer': 'http://192.168.8.90:31414/web/'
    }
    data = {
        'page_id': 0,
        'item_id': 6,
        'page_title': data['title'],
        'page_content': data['content'],
        'is_urlencode': 1,
        'cat_id': None
    }
    response = requests.post(url=url, headers=headers, data=data)
    print(response.json())


if __name__ == '__main__':
    do()