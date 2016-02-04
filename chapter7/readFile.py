__author__ = 'Mohamed fawzy'
try:
    fileName = raw_input("Enter file name: ")
    fileHandle = open(fileName)
except:
    print "Please enter valid filename and exist"
    exit()
count = 0
for line in fileHandle:
    if line.startswith('Subject:'):
        count+=1
print "There were ", count, "subject in ", fileName
