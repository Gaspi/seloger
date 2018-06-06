# -*- coding: utf-8 -*-

"""
@author: Gaspard
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

selogerURL = "https://www.seloger.com/list.htm"

req = {
    'bedrooms' : 2,
    'places' : '[{ci:750112}|{ci:750114}|{ci:750115}]',
    'price' : '1400/1900',
    'projects' : 1,
    'qsversion' : '1.0',
    'types' : '1,2',
    'LISTING-LISTpg' : 1
}


fullURL = selogerURL + "?" + "&".join([k + "=" + str(e) for k, e in req.items() ])


data = urlopen(fullURL, timeout=10)



bs = BeautifulSoup(data,"lxml")



