import urllib2
from BeautifulSoup import BeautifulSoup
#html_page = urllib2.urlopen('http://archive.financialexpress.com/livearchive/business-news/01/01/2008')
f = open('links.txt','r')
for hyp in f.readlines():
	date, hlink = hyp.split()
	html_page = urllib2.urlopen(hlink)
	s = BeautifulSoup(html_page)
	mydivs = s.findAll("div", { "class" : "archive_tab_list1" })
	for i in mydivs:
		link = BeautifulSoup(str(i),convertEntities=BeautifulSoup.HTML_ENTITIES)
		for u in link.findAll('ul'):
			cat = (u.li.span.string).strip()
			for anchor in u.findAll('a'):
				print anchor.get('href') + ' :: ' + date + ' :: ' + cat
#for link in f.readlines():
	#html_page = urllib2.urlopen()