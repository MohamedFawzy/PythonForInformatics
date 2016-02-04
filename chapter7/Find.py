__author__ = 'Mohamed fawzy'
fhandle = open('mbox.txt')
for line in fhandle:
    line = line.rstrip()
    if line.find('@uct.ac.za') == -1:
        continue
    print line
