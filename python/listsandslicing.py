#COMMON OPERATORS
#"and","not","or" - allows us to test multiple conditions

#if name == "Jemma" and age >= 23 and height >= 1.63
#print "it is definitely you Jemma!"

#if not name == "hannah"
#print "Not allowed in"

#can also be "is not""not in"

#None - is an individual data type that python sees as "false"

#LISTS
#square brackets = lists

#index starts from 0 not from 1!

#print len(listname) = give you the ammount of values in the list

#can change the list once made
#list[3] = car will change the 4th value to "car"

#list can have multiple types of values - strings integers etc

#can build lists from other lists

#for loop: 
#list =[...]
#for x in list:
#    print x

#del list[0] = deletes first entry to list

#list.append(x) = adds to the end of list
#add

#print list.sort() = will then have to do print list to see sorted list
#print list.reverse() = puts in reverse order, and will have to print list like above

#alternative built in sorting for list = s_list or r_list = but creates new list

#in = tests membership of list - print x in list = true or false reply
# if x in list:
#print y

#range function is to create a list

#print range(5) = start at 0 and go print until 5
#print range(2, 5) = start at 2 and go to 5
#print range(0, 10, 3) = will start 0 go to 10 in steps of 3.
#print range(10, 0, -1) = will start at 10 and count backwards to 0 in steps of -1

#SLICING

#strings are also a sequence - if you do [] can find within string
# element = "uranium"
#print element[1:4] = will print ran
#print element[:4] = print before 4th = uran
#print element[4:] = print ium
#print element[-4:] = will start from 4th from the end and print all after it
#if ask for 400th in sequence but there isnt one = error, but ask for all between 1st and 400th will give values = slice.

#slicing always creates a new collection!

#list2 = lists[1:-1] = create a new list using the values from value 1 (2nd in sequence) to last value of first list.
# 

#question 1
mylist = [1, 2, 3, 4, 5]

print mylist

print mylist[1]

print mylist[0:]

print mylist[1:4]

#question 2

one_to_ten = range(1, 11)

print one_to_ten

one_to_ten[0] = 10

print one_to_ten

one_to_ten.append(11)

print one_to_ten

one_to_ten.extend([12, 13, 14])

print one_to_ten

#question 3

forward = []
backward = []

print forward
print backward

values = ["a","b","c"]

print values

for item in values:
    print item
    

for item in values:
    forward.append(item)
    backward.insert(0,item)
    print forward, backward
print "forward is", forward
print "backward is", backward

print forward
print backward
forward.reverse()
#forward.reverse reverses internally but does not show anything.
print forward
print backward
print forward==backward


#question 4

countries = ["uk", "usa", "uk", "uae"]

print countries

print dir(countries)

#print help(countries.count)

# L.count(value) -> integer

print countries.count("uk")








