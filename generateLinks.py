from datetime import datetime
from datetime import timedelta
from BeautifulSoup import BeautifulSoup

base_url = 'http://archive.financialexpress.com/livearchive/business-news/'
start_date = '01/02/2008'
stop_date = '01/03/2008'

start = datetime.strptime(start_date, "%d/%m/%Y")
stop = datetime.strptime(stop_date, "%d/%m/%Y")

while start <= stop:
	print start.strftime("%d/%m/%Y") + ' '+ base_url+start.strftime("%d/%m/%Y")
	start = start + timedelta(days=1)
    