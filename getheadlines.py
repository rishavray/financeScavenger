from goose import Goose
import urllib2
from BeautifulSoup import BeautifulSoup
from datetime import datetime
from datetime import timedelta
import re
import time

#This is the base url. The date is just appened at the end of it

base_url = 'http://archive.financialexpress.com/livearchive/business-news/'
start_date = '01/01/2009'
stop_date = '30/06/2009'

g = Goose()

start = datetime.strptime(start_date, "%d/%m/%Y")
stop = datetime.strptime(stop_date, "%d/%m/%Y")

#Generating the archive pages
archive_pages = []
start_time = time.time()
while start <= stop:
	#print start.strftime("%d/%m/%Y") + ' '+ base_url+start.strftime("%d/%m/%Y")
	archive_pages.append([start.strftime("%d/%m/%Y"),base_url+start.strftime("%d/%m/%Y")])
	start = start + timedelta(days=1)

for pages in archive_pages:
	links = []
	date , link = pages
	html_page = urllib2.urlopen(link)
	s = BeautifulSoup(html_page)
	check = s.findAll(text=re.compile('No records found'),limit=1)
	if len(check) == 1:
		continue
	mydivs = s.findAll("div", { "class" : "archive_tab_list1" })
	for divs in mydivs:
		l = BeautifulSoup(str(divs),convertEntities=BeautifulSoup.HTML_ENTITIES)
		for u in l.findAll('ul'):
			cat = (u.li.span.string).strip()
			for anchor in u.findAll('a'):
				links.append([anchor.get('href'),cat])

	for tup in links:
		url , cat = tup
		article = g.extract(url=url)
		print date + ' :: ' + (article.title).encode('UTF-8') + ' :: ' + (article.meta_description).encode('UTF-8') + ' :: ' + cat.encode('UTF-8')
print("--- %s seconds ---" % (time.time() - start_time))