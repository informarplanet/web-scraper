from urllib.request import urlopen
from bs4 import BeautifulSoup
html=urlopen('https://www.google.com')
bs= BeautifulSoup(html,'lxml')
print(bs.html)
