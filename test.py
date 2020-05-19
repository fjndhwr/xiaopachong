import requests
import file_util
import time


def post(id):
    url = "https://time.geekbang.org/serv/v1/article"
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Cookie': '__guid=69774229.368026214742951000.1586956905994.9211; _ga=GA1.2.1948507358.1586956907; LF_ID=1586956906761-4111131-5998673; GCID=a923c9e-110dacc-84d108c-18cea38; GRID=a923c9e-110dacc-84d108c-18cea38; gksskpitn=8722f8d1-d8c6-4588-9cd6-03b29490c0f4; _gid=GA1.2.1684164300.1588860081; GCESS=BQoEAAAAAAYE.7HDcQEI_JMXAAAAAAACBMQUtF4DBMQUtF4MAQELAgUABwTzwRQqBQQAAAAACAEDCQEBBAQALw0A; Hm_lvt_022f847c4e3acd44d4a2481d9187f1e6=1586956907,1586956930,1588860081,1588860108; monitor_count=10; _gat=1; Hm_lpvt_022f847c4e3acd44d4a2481d9187f1e6=1588862058; SERVERID=1fa1f330efedec1559b3abbcb6e30f50|1588862053|1588860074',
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
    mp3_url = data.get("audio_download_url")
    file_util.write(title, content)
    download_mp3(mp3_url, title)

    right = data.get("neighbors").get("right")
    if not right.get('id') is None:
        new_id = right.get('id')
        time.sleep(10)
        post(new_id)


def download_mp3(url, title):
    if not url is None and not url == "":
        r = requests.get(url)
        with open("d:/jikeshijian/进阶攻略/" + title + ".mp3", "wb+") as code:
            code.write(r.content)


if __name__ == '__main__':
        post(12148)