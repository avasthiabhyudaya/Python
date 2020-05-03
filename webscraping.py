import urllib.request, urllib.parse, urllib.error
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
r=list()
url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('span')
for tag in tags:
    y=re.findall('([0-9]+)' ,str(tag))
    for i in range(0,len(y)):
        r.append(int(y[i]))
s=sum(r)
print(s)


# Retrieve all of the anchor tags
#for tag in tags:
    # Look at the parts of a tag
    #print('TAG:', tag)
    #print('URL:', tag.get('href', None))
    #print('Contents:', tag.contents[0])
    #print('Attrs:', tag.attrs)
