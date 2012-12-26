__author__ = 'Ash'
import urllib2

from bs4 import BeautifulSoup

baseURL = "http://www.nasdaq.com/markets/ipos/activity.aspx?tab=pricings&month="
months = ["2010-01", "2010-02", "2010-03", "2010-04", "2010-05", "2010-06", "2010-07", "2010-08", "2010-09", "2010-10",
          "2010-01", "2010-12", "2011-01", "2011-02", "2011-03", "2011-04", "2011-05", "2011-06", "2011-07", "2011-08",
          "2011-09", "2011-10", "2011-01", "2011-12", "2012-01", "2012-02", "2012-03", "2012-04", "2012-05", "2012-06",
          "2012-07", "2012-08", "2012-09", "2012-10", "2012-01", "2012-12"]

urlList = [baseURL+month for month in months]
pageList = [urllib2.urlopen(x).read() for x in urlList]
soupList = [BeautifulSoup(page) for page in pageList]
for soup in soupList:
    count = 0
    prntCnt = 0
    for link in soup.find_all('td'):
        if(count<4):
            print('')
        else:
            print(link.get_text()+'|'),
            prntCnt += 1
            if(prntCnt%7 == 0):
                print('')
        count += 1





#p = html5lib.HTMLParser()

str = urllib2.urlopen("http://www.nasdaq.com/markets/ipos/activity.aspx?tab=pricings&month=2010-01").read()

soup = BeautifulSoup(str)
