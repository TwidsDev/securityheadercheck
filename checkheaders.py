#!/usr/bin/python3

import requests,sys
requestHeaders = ["Strict-Transport-Security","X-Xss-Protection","X-Content-Type-Options","X-Frame-Options","Content-Security-Policy","Public-Key-Pins"]

for url in open("sites.txt"):
	try:
		print ("Site Headers Being Checked:", url)
		r = requests.head(url.rstrip())
		for i in requestHeaders:
			if i in r.headers:
				print(i, r.headers[i])
			else:
				print(i + " Not Present")
	except:
		print("Unknown Exception:" + sys.exc_info()[0])
