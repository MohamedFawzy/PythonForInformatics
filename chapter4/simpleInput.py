x = raw_input("Enter number\n")
try:
    x = int(x)
    if x%2==0:
        print "x is even"
    else:
        print "x is odd"
except:
    print "please enter valid number"