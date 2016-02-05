__author__ = 'Mohamed fawzy'
fhandle = open('mbox-short.txt')
for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print words[2]


