__author__ = 'Mohamed fawzy'
# read any string start with from
import re
hand = open('mbox-short.txt')
for line in hand:
    line=line.rstrip()
    if re.search('^From:', line):
        print line

