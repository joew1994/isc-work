#question 1

import numpy as np
#by importing as 'np' we only have to write np instead of numpy when using a function from the numpy library

x = range(1, 11)

a1 = np.array(x, np.int32)
a2 = np.array(x, np.float32)

print a1.dtype
print a2.dtype

#questions 2

ar1 = np.zeros((2, 3, 4))
ar2 = np.ones((2, 3, 4))
ar3 = np.arange((1000))

print ar1
print ar2
print ar3

#question 3

a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])

print a

print a[1]

print a[1:4]

a = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4], [1, 22, 4, 0.1, 5.3, -9], [3, 1, 2.1, 21, 1.1, -2]])

print a
print "."
print a[:, 3]
print "."
print a[1:4, 0:4]
print "."
print a[1:, 2]



