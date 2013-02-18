__author__ = 'as17237'

import urllib2
from bs4 import BeautifulSoup
import pprint


baseBoyURL = "http://www.indianhindunames.com/indian-hindu-boy-name-"
baseGirlURL = "http://www.indianhindunames.com/indian-hindu-girl-name-"


def extractNames(url):
    nameDict = {}
    pp = pprint.PrettyPrinter(indent=4)
    global alphabet, letter, urlList, x, pageList, page, soupList, sectionList, section, fragmentList, fragment, item
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
                "v", "w", "x", "y", "z"]
    urlList = [url + letter + ".htm" for letter in alphabet]
    pageList = [urllib2.urlopen(x).read() for x in urlList]
    soupList = [BeautifulSoup(page) for page in pageList]
    sectionList = [x.find("div", {"id": "content_child"}) for x in soupList]
    fragmentList = [section.find("p").contents for section in sectionList]
    for fragment in fragmentList:
        for item in fragment:
            if "=" in item:
                nameDict[str(item.partition("=")[0].strip())] = str(item.partition("=")[2].strip())
    pp.pprint(nameDict)


#extractNames(baseBoyURL)
extractNames(baseGirlURL)

