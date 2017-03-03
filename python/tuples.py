#a TUPLE = a sequence like a list, except it can not be modified once created
# created using normal brackets instead of square brackets
#but still index with square brackets

#emunerate function = produces index and values in pairs.

#question 1

t = (1,)

print t

print t[-1]

tup = range(100, 200)

print tup

tup2 = tuple(tup)

print tup
print tup2

print tup[0], tup[-1]

#question 2

mylist = [23, "hi", 2.4e-10]

for item in mylist:
    print item, mylist.index(item)

for (count, item) in enumerate(mylist):
    print count, item




