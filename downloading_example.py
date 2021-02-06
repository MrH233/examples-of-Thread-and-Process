import urllib
import urllib.request
import gevent
import re


def download(url, path):
    req = urllib.request.urlopen(url)
    img_content = req.read()
    path += '\\' + url[-10:]
    with open(path, "wb") as wstream:
        wstream.write(img_content)


def main(main_url):
    waiting_list = []            # 待下载队列
    main_req = urllib.request.urlopen(main_url)    # 打开网页
    content = str(main_req.read())       # 获取网页源代码
    pattern = re.compile(r"http.*?\.jpg")        # 利用正则表达式来获得img标签中的src
    url_list = re.findall(pattern, content)
    for url in url_list:
        g = gevent.spawn(download, {url}, 'F:\\test')
        g.join()

    # for url in url_list:
    #     waiting_list.append(f"gevent.spawn(download,{url},'F:\\test')")
    # gevent.joinall([eval(i) for i in waiting_list])   # 利用协程来控制下载


if __name__ == "__main__":
    main("http://www.netbian.com/")
