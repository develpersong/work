# -*- coding: UTF-8 -*-
import url_manager
import html_downloader


class SpiderMain:
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()

    def craw(self):
        print(self.downloader.download("http://www.baidu.com").read())


if __name__ == "__main__":
    SpiderMain().craw()
