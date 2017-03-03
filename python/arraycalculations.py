#question 1

import numpy as np

a = np.array([range(4), range(10, 14)])

b = np.array([2, -1, 1, 0])

print a
print ""
print b

print ""

print a * b

b1 = b * 100

print ""

print b1

b2 = b * 100.0

print ""

print b2

print b1 == b2

print b1.dtype
print b2.dtype

#question 2

arr = np.array(range(0, 10))

print arr

#print arr < 3
print np.less(arr, 3)


condition = np.logical_or(arr < 3, arr >8) 

#created a condition where it checks array if it is less than 3 or greater than 8. # the 'or' tells the condtition that it looks for two paramaters = < 3 as well as >8.

new_arr = np.where(condition, arr * 5, arr * -5)

 #where condition is true multiply by 5, wherre condition is false multiply by -5 - ( , ) which side of the comma inside brackets determines true(left) and false(right)

print new_arr

#question 3





