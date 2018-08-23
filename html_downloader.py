# coding:utf8

import urllib


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        response = urllib.urlopen(url)  # 下载器的第一种方法，得到response

        if response.getcode() != 200:
            return None

        return response.read()
