import os


def write(title, text):
    dirs = "d:/jikeshijian/进阶攻略/"
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    dirs += title + ".md"
    fd = open(dirs, mode="wb+")
    fd.write(text.__str__().encode(encoding="utf-8", errors="strict"))
    fd.close()
