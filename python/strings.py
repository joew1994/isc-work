#STRINGS
#sequences of charactors
#indexed same as index lists

#name = darwin
#for c in name:
#    print c
#d
#a
#r
#w
#i
#n

#can use double or single quotes for strings - doesnt matter which you use as long as its the same at begining and end of string

#stings cant be changed once made = are immutable

#name = "charles" + " " + "darwin" = charles darwin  = concatenates strings

#question 1

s = "I love to write python"

print s

for x in s:
    print x

print s[5]
print s[-1]

print len(s)
print s[0], s[0][0], s[0][0][0]

#question 2


split_s = s.split()
print split_s
for word in split_s:
    if word.find("i"):
        print "I found 'i' in: '{0}'".format(word)

split_s = s.split()
print split_s
for word in split_s:
    if word.find("i") >-1:
        print "I found 'i' in: '{0}'".format(word)

#question 3

something = "completely different"
print dir(something)

print something.count('t')

print something.find('plete')






