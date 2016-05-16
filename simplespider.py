"""
Author: TH 
Date: 16/05/2016
simple web spider that returns array of urls. 
To install mechanize
python -m pip install mechanize
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def collectFromUrl(url):
	baseUrl = "http://seekingalpha.com"
	print(url)
	r = requests.get(url)
	#print(r.content)
	
	soup = BeautifulSoup(r.content,'html.parser')
	#soup2 = BeautifulSoup(requests.get('http://seekingalpha.com/article/3975071-apple-thinking-critically-iphone-7-rumors').content,'html.parser')
	print(soup)
	#print(type(soup.find_all("h1")[0].text))
	try:
		if '403' in soup.find_all("h1")[0].text:
		    print('403 Not Found', ticker, page)
	except:
		pass
	articles = soup.find_all("div",{"class":"symbol_article"})
	#articles = soup.body.div.findall({"class":"symbol_article"})
	#print(articles)
	file = open('out.txt','w')
	for article in articles:
	    #print(article)
	    link = article.find_all("a", {"sasource":"qp_focused"})
	    try:
	        #print(link[0])
	        linkAdr = link[0].get("href")
	        linkTxt = link[0].text
	        #print(linkTxt, linkAdr)
	        print("linkTxt", linkTxt)
	        print("urljoin", urljoin(baseUrl, linkAdr))
	        file.write(linkTxt+'\n')
	        file.write(urljoin(baseUrl, linkAdr)+'\n')
	    except Exception as e:
	        print(e)
	file.close
def collectFromTicker(ticker, page):
	baseUrl = "http://seekingalpha.com"
	url = 'http://seekingalpha.com/symbol/'+ticker+'/focus/'+page
	print(url)
	r = requests.get(url)
	#print(r.content)
	
	soup = BeautifulSoup(r.content,'html.parser')
	#soup2 = BeautifulSoup(requests.get('http://seekingalpha.com/article/3975071-apple-thinking-critically-iphone-7-rumors').content,'html.parser')
	print(soup)
	#print(type(soup.find_all("h1")[0].text))
	try:
		if '403' in soup.find_all("h1")[0].text:
		    print('403 Not Found', ticker, page)
	except:
		pass
	articles = soup.find_all("div",{"class":"symbol_article"})
	#articles = soup.body.div.findall({"class":"symbol_article"})
	#print(articles)
	file = open('out.txt','w')
	for article in articles:
	    #print(article)
	    link = article.find_all("a", {"sasource":"qp_focused"})
	    try:
	        #print(link[0])
	        linkAdr = link[0].get("href")
	        linkTxt = link[0].text
	        #print(linkTxt, linkAdr)
	        print("linkTxt", linkTxt)
	        print("urljoin", urljoin(baseUrl, linkAdr))
	        file.write(linkTxt+'\n')
	        file.write(urljoin(baseUrl, linkAdr)+'\n')
	    except Exception as e:
	        print(e)
	file.close

#collectFromTicker('ABT','1')
collectFromUrl('http://seekingalpha.com/symbol/AAPL/focus/')
















