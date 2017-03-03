if #give a condition
while # another condition
# == is if you say 'if something equals ( if x == y)
else # use after if command
elif # else if
# indentation tell python that a peice of code is ended = if its a loop it will return to begining, or it will move on to the next code.
#4 spaces is the conventional amount of indentation

#question 1

num_moons = 10
while num_moons < 5:
    print num_moons 

# need a colon at the end of a condition
# indent not on while

#question 2

mylist = [23, "hi", 2.4e-10]
count = 0
while count < 3:
    item = mylist[count]
    print item, mylist.index(item)
    count += 1


#question 3

x = 1
if x: print x, "is true"

if 22.1: print "true"

if "hello": print "true"

if [1,2]: print "true"

if 0: print "true"

if 0.0: print "true"

if []: print "true"

#empty sequences and '0' are considered not true.






