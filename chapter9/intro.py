# dictionary is simple just like like but with a key value pairs
test = dict()
test['one'] = 'one1'
print test
print test['one']

# init another dictionary with multiple values and different data types
myitmes = {'one': 'value1', 'two': 2, 'three': 'three value'}
print myitmes # note that print output does not return values in order as same input it's return every time with a different one
print myitmes['one'] #access item inside dictionary with key
# print length for dictionary
print len(myitmes)

print 'one' in myitmes # check if key exist in dictionary or not

values = myitmes.values(); # get dictionary values
print 2 in values # check if value exist in dictionary or not