import requests


if __name__ == '__main__':
    proxies = {
        'http': "http://127.0.0.1:1080",
        'https': "https://127.0.0.1:1080",
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
    }
    r = requests.get("https://download.vpngate.jp/common/cd.aspx/vpngate-client-2020.05.17-build-9745.147195.zip",
                     timeout=10000, proxies=proxies, headers=headers)
    with open("d:/test/vpngate-client-2020.05.17-build-9745.147195.zip", "wb+") as code:
        code.write(r.content)