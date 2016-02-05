__author__ = 'Mohamed fawzy'
t = ['a', 'b', 'c', 'd']
print t[1:3]
print t[:4]
print t[3:]
t[1:3] = ['x', 'y']
print t
# add new element at end of the list
t.append('m')
print t
t2 = ['f','w']
# add list to another list
t.extend(t2)
print "After add t2 to t2", t
# sort list
t.sort()
print 'After sort', t
# delete element and pass index for it
x = t.pop(1)
print 'Element deleted is', x
print 'After delete : ', t
# delete last element
lastElement = t.pop()
# remove element without return removed value
del t[1]
print t
# remove element by value not key
t.remove('w')
print t
# remove range
del t[1:3]
print t
# get length for list
numbers = [1, 2, 3, 4, 5]
print len(numbers)
# get max
print max(numbers)
# get min
print min(numbers)
# sum items in list
print sum(numbers)
# get average
print sum(numbers) / len(numbers)
# convert from string to list
string = 'spam'
t4 = list(string)
print t4
s = 'this is new'
t5 = s.split()
print t5
s2 = 'spam-spam-spam'
t6 = s2.split('-')
print t6
# convert list into string
t7 = ['hello', 'world']
delimiter = ' ' # space between them
result = delimiter.join(t7)
print result


