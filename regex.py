import re
f=input("Enter the file name:")
fh=open(f)
r=list()
j=0
for line in fh:
    y=re.findall('([0-9]+)' ,line)
    print(y)
    for i in range(0,len(y)):
        r.append(int(y[i]))
s=sum(r)
print(s)
