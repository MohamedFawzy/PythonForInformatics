# author mohamed fawzy
# advanced parsing file
# remove punctuation and count words in file then return result using dictionary with hash table algorithm
import string
fname = raw_input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print 'cannot open file', fname
    exit()
counts = dict()
for line in fhand:
    line = line.translate(None, string.punctuation)
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
print counts
