import urllib2
from BeautifulSoup import BeautifulSoup
f = open('links.txt','r')
for line in f.readlines():
	date , link = line.split()
	html_page = urllib2.urlopen(link)
	#html_page = urllib2.urlopen('http://archive.financialexpress.com/livearchive/business-news/01/01/2008')
	s = BeautifulSoup(html_page)
	mydivs = s.findAll("div", { "class" : "archive_tab_list1" })
	for i in mydivs:
		link = BeautifulSoup(str(i))
		for j in link.findAll('a'):
			print date + ' ' + j.get('href')
#for link in f.readlines():
	#html_page = urllib2.urlopen()