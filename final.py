#!/usr/bin/env python
# encoding: utf-8

import json
import argparse
import tools.download

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--download", type=file, dest="download",
                    help="download all resources by URLs listed in a json file")

parser.add_argument("-n", "--number", type=int, dest="number",
                    help="the number of the URLs should be downloaded")

parser.add_argument("-H", "--getHTML", dest="getHTML", action="store_true",
                    help="generate index.html")

parser.add_argument("-L", "--getLog", dest="getLog", action="store_true",
                    help="generate log.txt")
parser.add_argument("-A", "--getAnalysis", dest="getAnalysis", action="store_true",
                    help="analyse the provided web page")
options = parser.parse_args()

if options.download:
    jsonfile = json.load(options.download)
    tools.download.download(jsonfile)
