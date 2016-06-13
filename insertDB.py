"""
Author:TH
Date:19/05/2016
Insert articles into DB
DB is hosted by Azure
"""

import pymssql
import yaml
from login import loginSA
from collectArticle import collectArticle
import simplespider_session
import datetime

def insertDB(session, url):
	# Load yaml
	keys = yaml.load(open("keys.yaml",'r'))
	# Login Seeking Alpha
	#session = loginSA()[1]
	# Example url
	#url = 'http://seekingalpha.com/article/3972364-adobe-targets-sketch-axure-justinmind'
	# Connect to DB
	server = keys['DBserver']
	user = keys['DBuser']
	password = keys['DBpassword']
	database = 'SeekingAlpha'
	conn = pymssql.connect(server , user, password,database)
	cursor = conn.cursor()

	#collect one article
	article = collectArticle(session, url)
	if type(article) is not dict:
		return article;
	#print(article['title'])
	now = datetime.datetime.now()

	# Insert into database if not exists
	# we have 15 columns in this table
	# Please only add '\' with a white space before them. Otherwiase there maybe a disater as database name and '\' could be concated together
	#print(article['articleUrl2'])
	try:
		"""
		cursor.execute("\
		INSERT dbo.SeekingALpha_Articles (Title, Date, Time, TickersAbout, TickersIncludes, \
			Name, NameLink, Bio, Summary, ImageDummy, BodyContent, Disclosure, Position, CreatedAt, UpdatedAt, BodyAll, ArticleNumber, ArticleUrl) \
			VALUES (%s, %s, %s, %s, \
			%s, %s, %s, %s, %s, \
			%s, %s, %s, %s, %s, %s, %s, %s, %s) \
		", (article['title'], article['date'], article['time'], article['tickersAbout'], article['tickersIncludes'], article['name'], article['nameLink'], article['bio'], article['summary'], article['imageDummy'], article['bodyContent'], article['disclosure'], None, now, now, article['bodyAll'], article['articleNumber'], article['articleUrl2']))
		"""
		cursor.execute(" \
		BEGIN \
		IF NOT EXISTS (SELECT * FROM dbo.SeekingAlpha_Articles \
		WHERE ArticleNumber = %s) \
		BEGIN \
		INSERT dbo.SeekingALpha_Articles (Title, Date, Time, TickersAbout, TickersIncludes, \
			Name, NameLink, Bio, Summary, ImageDummy, BodyContent, Disclosure, Position, CreatedAt, UpdatedAt, BodyAll, ArticleNumber, ArticleUrl) \
			VALUES (%s, %s, %s, %s, \
			%s, %s, %s, %s, %s, \
			%s, %s, %s, %s, %s, %s, %s, %s, %s) \
		END \
		END", (article['articleNumber'], article['title'], article['date'], article['time'], article['tickersAbout'], article['tickersIncludes'], article['name'], article['nameLink'], article['bio'], article['summary'], article['imageDummy'], article['bodyContent'], article['disclosure'], None, now, now, article['bodyAll'], article['articleNumber'], article['articleUrl2']))
		
		conn.commit()
		return "success"
	except Exception as e:
		print(e," insertDB failed.")
		return "fail"



	# If you don't commit, then the inserted results will not be visual to others than local users.

if __name__ == "__main__":
	session = loginSA()[1]
	url = 'http://seekingalpha.com/article/3972364-adobe-targets-sketch-axure-justinmind'
	url2 = 'https://seekingalpha.com/pro/checkout/3973979?notice=pro'
	url3 = 'http://seekingalpha.com/article/3981280-5-things-apple-must-wwdc-keep-stock-tanking'
	print(insertDB(session, url3))