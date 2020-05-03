# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re
def name(pos,u):
    p=0
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    html = urllib.request.urlopen(u, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        p=p+1
        if p==pos:
            u=tag.get('href', None)
            break
    return u
# Ignore SSL certificate errors
url = input('Enter - ')
rep = int(input("Repetitions: "))
pos = int(input("Position: "))
for i in range(rep):
    url=name(pos,url)
b=re.findall("_([A-Za-z]+)\.html",url)
print(str(b))
