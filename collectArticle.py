"""
Author:TH
Date:17/05/2016
Download one artile using url.
Naming rules: http://stackoverflow.com/questions/2029358/should-i-write-table-and-column-names-always-lower-case
Table design: Title, Date, Time, TickersAbout, TickersIncludes, Name, NameLink, Bio, Summary, ImageDummy, BodyContent, Disclosure, Position 
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from login import loginSA
import sys
import codecs

def collectArticle(session, url): 
	# Set std out encoding
	#sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
	#print (sys.stdout)

	#sessionCode = loginSA()[0]
	#print(sessionCode)
	#session = loginSA()[1]
	userHeader = {"Referer": "http://seekingalpha.com/",
			"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36"}
	
	r = session.get(url, headers = userHeader)
	#print(r.encoding)

	soup = BeautifulSoup(r.content, 'html.parser')

	#print(soup)

	# Print to txt file
	"""
	file = open('out.txt','wb')
	file.write(soup.prettify().encode('utf-8'))
	file.close
	"""
	pro = soup.find_all("div",{"class":"checkout-header-text"})
	if len(pro)!=0:
		print("Ignore a pro article.")
		return "pro"
	try:
		title = soup.find_all("h1", {"itemprop":"headline"})[0].text
	except:
		print("Wrong url: ",url)
		return "wrongUrl"
	###print("title: ", title)
	dateTime = soup.find_all("time", {"itemprop":"datePublished"})[0]
	time1 = dateTime.get("content")
	time2 = dateTime.text
	date = dateTime.get("content").split('T')[0]
	time = dateTime.get("content").split('T')[1].split('Z')[0]
	###print("Date time is: {0} and {1}".format(date, time))
	# This part, we could not collect the num of comments. we don't have this field when we download the webpage.
	# instead, we have a field with id="a-comments-wrapper"
	#numComments = soup.find_all("span", {id:"a-comments"})
	#print("Num of comments: ",numComments)

	#instead, I find another place for num of comments

	tickersAbout = []
	companiesAbout = soup.find_all("a", {"sasource":"article_primary_about"})
	for companyAbout in companiesAbout:
		if "(" in companyAbout.text:
			tickersAbout.append(companyAbout.text.split("(")[1].split(")")[0])
		else:
			tickersAbout.append(companyAbout.text)
	#print("Tickers About are: {0}".format(', '.join(tickersAbout)))
	tickersAboutStr = ', '.join(tickersAbout)

	tickersIncludes = []
	companiesIncludes = soup.find_all("a", {"sasource":"article_about"})
	for companyIncludes in companiesIncludes:
	    tickersIncludes.append(companyIncludes.text)
	###print("Tickers Includes are: {0}".format(', '.join(tickersIncludes)))
	tickersIncludesStr = ', '.join(tickersIncludes)

	author = soup.find_all("a",{"class":"name-link", "sasource":"auth_header_name"})
	authorUrl = author[0].get("href")
	authorName = author[0].contents[0].text
	###print("Name is: {0}, {1}".format(authorUrl, authorName))

	bio = soup.find_all("div", {"class":"bio hidden-print"})[0].text
	###print("Bio is: {0} ".format(bio))

	summary = []
	try:
		summaryByParagraphes = soup.find_all("div", {"class":"a-sum", "itemprop":"description"})[0].find_all("p")
		for p in summaryByParagraphes:
		    summary.append(p.text);
		###print("Summary: ",' '.join(summary))
	except Exception as e:
		print(e, ', No Summary')
	summaryStr = ' '.join(summary)

	image = soup.find_all("span", {"class":"image-overlay"})
	if len(image) > 0:
	    imageDummy = 1
	else:
	    imageDummy = 0
	###print("ImageDummy: ",imageDummy)

	body = soup.find_all("div", {"id":"a-body"})[0].find_all("p")
	bodyContent = ''
	for p in body:
	    bodyContent += (p.text+' ')
	bodyContent = bodyContent.split("Disclosure")[0]
	"""
	# If you use 'wb', then you have to associate it with 'encode'
	file = open('out.txt','wb')
	file.write(bodyContent.encode('utf-8'))
	file.close
	"""
	"""
	# Print to txt file
	file = open('out.txt','wb')
	for p in body:
	    file.write((p.text+' ').encode('utf-8'))
	file.close
	"""

	try:
		disclosure = soup.find_all("p", {"id":"a-disclosure"})[0].find_all("span")[0].text
		###print("Disclosure: ", disclosure)
	except Exception as e:
		print(e, ', No Disclosure')
		disclosure = ''
	return {"title": title,
			"date": date,
			"time": time, 
			"tickersAbout": tickersAboutStr,
			"tickersIncludes": tickersIncludesStr,
			"name": authorName,
			"nameLink": authorUrl,
			"bio": bio,
			"summary": summaryStr,
			"bodyContent": bodyContent,
			"imageDummy": imageDummy,
			"disclosure": disclosure}

if __name__ == "__main__":
    session = loginSA()[1]
    url1 = 'http://seekingalpha.com/article/3975401-apple-buffett-wants-stock-drop'
    url2 = 'http://seekingalpha.com/article/3972353-debt-integration-buyers-remorse-can-abbott-pull-deals'
    #url3 links to an articles which needs pro subscription
    url3 = 'https://seekingalpha.com//article/3973979-ptcs-misunderstood-transformation-creates-rare-investment-opportunity'
    #url4 is an empty page
    url4 = 'http://seekingalpha.com/symbol/BIIB/focus/10'
    collectArticle(session, url4)















