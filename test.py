import requests
import file_util
import time


def post(pretitle, id):
    url = "https://time.geekbang.org/serv/v1/article"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Cookie': 'Hm_lvt_59c4ff31a9ee6263811b23eb921a5083=1589873993; _ga=GA1.2.2057074915.1590997562; _gid=GA1.2.2007436798.1590997562; _gat=1; LF_ID=1590997562539-6680180-8523689; gksskpitn=c5557c01-3f8d-4537-a359-7bb8d9c4c5fa; GCID=acf42bf-1ec2017-5c617f6-573486d; GRID=acf42bf-1ec2017-5c617f6-573486d; GCESS=BQEI2YUeAAAAAAAJAQECBE6y1F4FBAAAAAAEBAAvDQAHBMu4H1sMAQEDBE6y1F4GBKBRFUwKBAAAAAAIAQMLAgUA; Hm_lpvt_59c4ff31a9ee6263811b23eb921a5083=1590997584; gk_process_ev={%22count%22:4%2C%22utime%22:1590997575183%2C%22referrer%22:%22https://time.geekbang.org/%22%2C%22target%22:%22page_geektime_login%22%2C%22referrerTarget%22:%22page_geektime_login%22}; _ga=GA1.2.2057074915.1590997562; _gid=GA1.2.2007436798.1590997562; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1591004490,1591005579,1591844853,1591856990; Hm_lvt_59c4ff31a9ee6263811b23eb921a5083=1589873993; GRID=607df40-c0c27be-370d6b6-8cc9f0b; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1591858545; gk_process_ev={%22count%22:5%2C%22utime%22:1590997575183%2C%22referrer%22:%22https://time.geekbang.org/%22%2C%22target%22:%22page_geektime_login%22%2C%22referrerTarget%22:%22page_geektime_login%22}; Hm_lpvt_59c4ff31a9ee6263811b23eb921a5083=1591858545; SERVERID=3431a294a18c59fc8f5805662e2bd51e|1591858812|1591858538',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
        'Origin': 'https://time.geekbang.org',
        'Referer': 'https://time.geekbang.org/column/article/' + str(id),
        'Content-Type': 'application/json',
    }

    params = {
        'id': str(id),
        'include_neighbors': True,
        'is_freelyread': True
    }
    response = requests.post(url, headers=headers, json=params)
    data = response.json().get('data')
    content = data.get('article_content')
    title = data.get("article_title")
    title = title.replace("|", "")
    title = title.replace("?", "")
    title = title.replace("、", "")
    title = title.replace("╲", "")
    title = title.replace("/", "")
    title = title.replace("*", "")
    title = title.replace("“", "")
    title = title.replace("”", "")
    title = title.replace("<", "")
    title = title.replace(">", "")
    mp3_url = data.get("audio_download_url")
    file_util.write(pretitle, title, content)
    download_mp3(pretitle, mp3_url, title)

    right = data.get("neighbors").get("right")
    if not right.get('id') is None:
        new_id = right.get('id')
        time.sleep(30)
        post(pretitle, new_id)


def download_mp3(pretitle, url, title):
    if not url is None and not url == "":
        r = requests.get(url)
        with open("d:/jikeshijian/"+pretitle+"/" + title + ".mp3", "wb+") as code:
            code.write(r.content)


if __name__ == '__main__':
    x = input("起始id为：")
    y = input("pretitle:")
    post(y, x)