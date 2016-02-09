# this program counts words in file
# algorithm read userinput open file read each line then read each word in line then move into next line count every word how many times appeared in file
fname = raw_input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print "file cannot be opened", fname
    exit()
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print counts
