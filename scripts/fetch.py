#! /usr/bin/env python

import  urllib2

response = urllib2.urlopen('http://114.212.81.5:50070/monitor?whichfile=/user/hadoop/input/8MB')
html = response.read()
print html
lines = html.splitlines()
dict = []
for line in lines:
    strs = line.split(':')
    print strs[0], strs[1]