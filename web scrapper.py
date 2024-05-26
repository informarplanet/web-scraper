from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
try:
    html=urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as error: 
    print(error)
except URLError as e:
    print('The server couldnot found ')
else:
    bs= BeautifulSoup(html,'lxml')
    print(bs.html)