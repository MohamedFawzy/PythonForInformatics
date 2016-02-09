#author mohamed fawzy
#A tuple1 is a sequence of values much like a list. The values stored in a tuple can be any type,
# and they are indexed by integers. The important difference is that tuples are immutable.
# Tuples are also comparable and hashable
#  so we can sort lists of them and use tuples as key values in Python dictionaries
t = tuple()
print t # empty tuple
t1 = tuple('demohere')
print t1
print t1[0] #print index zero element
print t1[1:3] # note that it will print range between 1,3 without last element 3
t1= ('A',) + t1[1:]
print 'after replacement ',t1
print (0, 1, 2) < (0, 3, 4) # compare two tuples