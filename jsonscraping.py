import urllib.request,urllib.parse,urllib.error
import json
url=input("Enter ~")#list of dictionaries
uh = urllib.request.urlopen(url)
data = uh.read().decode()
a=list()
try:
    js=json.loads(data)
except:
    js=None
for item in js['comments']:
    a.append(item['count'])
s=sum(a)
print(s)
