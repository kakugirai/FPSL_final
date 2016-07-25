#!/usr/bin/env python
# encoding: utf-8

import os
import json
import argparse
import glob

from prettytable import PrettyTable

import tools.download
import tools.html2json

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--download", type=file, dest="download",
                    help="download all resources by URLs listed in a json file")

parser.add_argument("-j", "--jsonify", dest="jsonify", action='store_true',
					help="return html resources to json")

parser.add_argument("-s", "--search", nargs='*', dest="search",
					help="return the searching result in the json file")

options = parser.parse_args()

if options.download:
	jsonfile = json.load(options.download)
	tools.download.download(jsonfile)

if options.jsonify:
	os.chdir("Downloads")
	data = []
	for html_file in glob.glob("*.html"):
		with open(html_file, "r") as html:
			data.append(tools.html2json.html2json(html))

	with open("../data.json", "w+") as json_data:
		json_data.write(json.dumps(data))

if options.search:
	with open("data.json") as data_file:
		data = json.load(data_file)
	result = []
	for i in xrange(len(data)):
		for j in xrange(len(data[i])):
			for k in xrange(len(data[i][j])):
				for element in options.search:
					if element.lower() in data[i][j][k].lower():
						result.append(list(course for course in data[i][j]))
	p = PrettyTable()
	if 0 < len(result) < 3:
		p.add_column("Course Number", ["Course Name", "Teacher", "Full or Half", "Semester", "GIGA or not", "Time", "Language"])
		for column in result:
			p.add_column(column[0],column[1:])
		print p.get_string(header=True)
	elif len(result) == 0:
		print "Not Found!"
	else:
		p.add_column("Course Name", [course[1] for course in result])
		print p.get_string(header=True)






