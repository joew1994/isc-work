#with open(txt. etc, r) as reader:
#    data = reader.read()
#    print len (data)   = will print the length of the data

#with open(txt. etc) as reader:
#    data = reader.read(64) = reads at 64bites
#    print data

#this is not good for large files

#to read one line at a time:
#with open(txt. etc) as reader:
#    line = reader. read
#    print data
 
#to put data into a file:

#with open(txt. etc) as writer:
#    writer.write(x)
#   writer. wrtielines

#question 1
x = 5

print x

with open("weather.csv", "r") as reader:
    data = reader.read()
    
print data

print len (data) # print length of data(bytes)

#question 2

with open("weather.csv", "r") as reader:
    line = reader.readline()
    print line

with open("weather.csv", "r") as reader:
    line = reader.readline()
    while line:
        print line
        line = reader.readline()

print "its over"
##
#
#
with open("weather.csv", "r") as reader:# with file open with r under reader
    line = reader.readline() # the value 'line' is given as the first line read
    while line: # whilst line is true (a value)
        print line # print line
        line = reader.readline() # reader reads next line and loops

print "its over" # once no further line is read - so line is not true print "end"
#
#
#

#question 3

with open("weather.csv", "r") as reader:
    line = reader.readline()
    for line in reader.readlines():
        print line
        
rain = ()


