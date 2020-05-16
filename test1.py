import requests


if __name__ == '__main__':
    r = requests.get("www.github.com/protocolbuffers/protobuf/releases/download/v3.11.4/protoc-3.11.4-win64.zip")
    with open("d:/test/protoc-3.11.4-win64.zip", "wb+") as code:
        code.write(r.content)