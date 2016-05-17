"""
Author:TH
Date:16/05/2016
login to Seeking Alpha
When you try to get or post, please use a headers variable. otherwise you will be considered as a robot and receive a 403
A tutorial for BitBucket: https://kazuar.github.io/scraping-tutorial/
A really good YouTube tutorial: https://www.youtube.com/watch?v=eRSJSKG4mDA
"""

import yaml
import requests
import sys
from lxml import html

def loginSA():
	#we get data from keys
	filepath = "keys.yaml"
	with open(filepath, 'r') as f:
	    keys = yaml.load(f)

	#print(keys['username'])
	#print(keys['password'])
	# Start a session so we can have persistant cookies
	sessionRequests = requests.Session()

	loginUrl = "http://seekingalpha.com/account/login"

	# This is the form data that the page sends when logging in
	loginData = {
		'slugs[]': None,
		'rt':None,
		'user[url_source]':None,
		'user[location_source]':'orthodox_login',
		'user[email]':keys['username'],
		'user[password]':keys['password'],
	   
	}
	# Authenticate
	r = sessionRequests.post(loginUrl, data = loginData, headers={"Referer": "http://seekingalpha.com/",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"})
	# add some more headers, like browsers
	#r = sessionRequests.get('http://seekingalpha.com/account/login')

	return [r.status_code, sessionRequests]

if __name__ == "__main__":
	print(loginSA()[0])
	tempUrl = 'http://seekingalpha.com/article/3973265-apple-can-reverse-revenue-curse'
	userHeader = {"Referer": "http://seekingalpha.com/",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
	print(loginSA()[1].get(tempUrl, headers = userHeader).text)
