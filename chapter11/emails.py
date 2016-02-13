import re
__author__ = 'Mohamed fawzy'
# find emails in file using regular expression
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+', line)
    if len(x) > 0:
        print x
