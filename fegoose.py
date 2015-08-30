from goose import Goose
#url = 'http://archive.financialexpress.com/news/ceat-q3-fy-08-net-up-63-/267478'
g = Goose()
f = open('url2.txt','r')

for line in f.readlines():
	date, url = line.split()
	article = g.extract(url=url)
	print date + ' :: ' + (article.title).encode('UTF-8') + ' :: ' + (article.meta_description).encode('UTF-8')
#print (article.cleaned_text).encode('UTF-8')

