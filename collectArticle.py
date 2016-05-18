"""
Author:TH
Date:17/05/2016
Download one artile using url.
Naming rules: http://stackoverflow.com/questions/2029358/should-i-write-table-and-column-names-always-lower-case
Table design: Title, DateTime, NumComments, About, Incluses, Name, NumFollowers, Bio, Summary, Content, Disclosure, EmailedTo, Tagged, NumComments
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from login import loginSA
import sys
import codecs

# Set std out encoding
#sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
#print (sys.stdout)

sessionCode = loginSA()[0]
print(sessionCode)
session = loginSA()[1]
userHeader = {"Referer": "http://seekingalpha.com/",
		"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
url = 'http://seekingalpha.com/article/3975401-apple-buffett-wants-stock-drop'
r = session.get(url, headers = userHeader)
#print(r.encoding)

soup = BeautifulSoup(r.content, 'html.parser')

#print(soup)
"""
# Print to txt file
file = open('out.txt','wb')
file.write(soup.prettify().encode('utf-8'))
file.close
"""
title = soup.find_all("h1", {"class":"has-title-test"})[0].text
print("title: ", title)
time = soup.find_all("time", {"itemprop":"datePublished"})[0]
time1 = time.get("content")
time2 = time.text
print("Time is: {0} and {1}".format(time1, time2))
# This part, we could not collect the num of comments. we don't have this field when we download the webpage.
# instead, we have a field with id="a-comments-wrapper"
#numComments = soup.find_all("span", {id:"a-comments"})
#print("Num of comments: ",numComments)
tickersAbout = []
companiesAbout = soup.find_all("a", {"sasource":"article_primary_about"})
for companyAbout in companiesAbout:
    tickersAbout.append(companyAbout.text)
print("Tickers About are: {0}".format(tickersAbout))

tickersIncludes = []
companiesIncludes = soup.find_all("a", {"sasource":"article_about"})
for companyIncludes in companiesIncludes:
    tickersIncludes.append(companyIncludes.text)
print("Tickers Includes are: {0}".format(tickersIncludes))














