import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET
a=list()
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
r=list()
url = input('Enter - ')
xml = urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)
lst = tree.findall(".//count")
for count in lst:
    a.append(int(count.text))
b = sum(a)
print(b)
