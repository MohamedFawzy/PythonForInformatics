__author__ = 'Mohamed fawzy'
# open file
# count lines in file
# print those lines
fhand = open('mbox.txt')
fileData = fhand.read()
count =0
for line in fileData:
    print fileData
print 'Line Count: ', count
