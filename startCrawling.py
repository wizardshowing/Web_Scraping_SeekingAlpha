"""
Author: TH 
Date: 19/05/2016
Login to Seeking Alpha, use simplespider_session to collect urls on the page, use collectArticle to collect 
the articles associated with the urls and use insertDB to insert into database.
"""

from login import loginSA
from simplespider_session import collectFromTicker
from collectArticle import collectArticle
from insertDB import insertDB
import tickers

def collectFromOnePage(ticker, page):
	
	session = loginSA()[1]
	res = collectFromTicker(session,ticker,str(page))
	print(ticker, ' ',str(page))
	file = open("NotCollected.txt","a")
	for a in res:
		#print(a["linkTxt"].replace(u"\u2018", "'").replace(u"\u2019", "'"))
		try:
			resDB = insertDB(session, a["linkAdr"])
			if resDB != "success":
				file.write(resDB+'\n')
		except Exception as e:
			print("isertDB error, ",e)
	file.close()


def collectFromSnP500(tickers):
	
	#session = loginSA()[1]
	for ticker in tickers:
		session = loginSA()[1]
		for page in range(1, 11):
			res = collectFromTicker(session,ticker,str(page))
			print(ticker, ' ',str(page))
			file = open("NotCollected.txt","a")
			for a in res:
				#print(a["linkTxt"].replace(u"\u2018", "'").replace(u"\u2019", "'"))
				try:
					resDB = insertDB(session, a["linkAdr"])
					if resDB != "success":
						file.write(resDB+'\n')
				except Exception as e:
					print("isertDB error, ",e)
			file.close()
if __name__ == "__main__":
	#collectFromOnePage('AAPl',3)
	tickers = tickers.tickers
	collectFromSnP500(tickers)