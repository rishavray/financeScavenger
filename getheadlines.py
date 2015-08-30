from goose import Goose
import urllib2
from BeautifulSoup import BeautifulSoup
from datetime import datetime
from datetime import timedelta

#This is the base url. The date is just appened at the end of it

base_url = 'http://archive.financialexpress.com/livearchive/business-news/'
start_date = '01/03/2008'
stop_date = '31/03/2008'

g = Goose()

start = datetime.strptime(start_date, "%d/%m/%Y")
stop = datetime.strptime(stop_date, "%d/%m/%Y")

#Generating the archive pages
archive_pages = []

while start <= stop:
	#print start.strftime("%d/%m/%Y") + ' '+ base_url+start.strftime("%d/%m/%Y")
	archive_pages.append([start.strftime("%d/%m/%Y"),base_url+start.strftime("%d/%m/%Y")])
	start = start + timedelta(days=1)

for pages in archive_pages:
	links = []
	date , link = pages
	html_page = urllib2.urlopen(link)
	s = BeautifulSoup(html_page)
	mydivs = s.findAll("div", { "class" : "archive_tab_list1" })
	for divs in mydivs:
		l = BeautifulSoup(str(divs))
		for k in l.findAll('a'):
			links.append(k.get('href'))

	for url in links:
		article = g.extract(url=url)
		print date + ' :: ' + (article.title).encode('UTF-8') + ' :: ' + (article.meta_description).encode('UTF-8')
