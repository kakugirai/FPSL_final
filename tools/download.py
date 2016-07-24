#/usr/bin/env python
# encoding: utf-8

import os
import urllib

def download(url_list):
    """ Download all URLs """
    if not os.path.exists("Downloads"):
        os.makedirs("Downloads")
    for url in url_list:
        print "Downloading " + url
        content = urllib.urlopen(url)
        filename = str(url_list.index(url)) + ".html"
        with open("Downloads/" + filename, "w+") as webpage:
            webpage.write(content.read())

if __name__ == "__main__":
    test = ["http://www.sfc.wide.ad.jp/IRL/members.html"]
    download(test)

