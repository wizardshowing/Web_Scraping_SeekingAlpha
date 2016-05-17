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
