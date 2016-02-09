def print_hist(h):
    for c in h:
        print c, h[c]

dic1 = dict()
dic1 = {'one': 'one', 'two': 2}
print_hist(dic1)

print '==============='
# sorted version sort by keys in alphabetical order
def print_sorted_hist(h):
    lst = h.keys()
    lst.sort()
    for c in lst:
        print c, h[c]

print_sorted_hist(dic1)
