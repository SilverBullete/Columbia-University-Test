import urllib.request
import re
import sys
from part1 import is_alpha,is_alnum,startswith,is_in
start_url = sys.argv[1].lower()
n = int(sys.argv[2])
response = urllib.request.urlopen(start_url)
response = response.read().decode('utf-8')
info = response.split(r'<a href="')
url = []
title = []
for i in range(1,len(info)):
    u = info[i].split(r'"')[0]
    if len(u) < 15:
        u = "http://www.cs.columbia.edu/~jikk/index.html" + u
    url.append(u)
    t = info[i].split(r'>')[1]
    t = t.split(r'</a>')[0].split()
    title.append(" ".join(t))
if len(url) > n:
    for i in range(0, n):
        print("Title:%s \tURL:%s"%(title[i],url[i]))
    print("...")
else :
    for i in range(0,len(url)):
        print("Title:%s \tURL:%s"%(title[i],url[i]))
if is_alpha(title[0]) and title[0].is_alpha:
    print("Ture")
if is_alnum(title[0]) and title[0].is_alnum:
    print("Ture")
if startswith(title[0],"Kangkook") and title[0].startswith("Kangkook"):
    print("Ture")
if is_in(title[0],"Kangkook") and "Kangkook" in title[0]:
    print("Ture")