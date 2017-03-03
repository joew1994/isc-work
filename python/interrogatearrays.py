import numpy as np

#with numpy there are two ways to write things - both work (look at question2)

#question 1

arr = np.array([range(4), range(10, 14)])
print arr.shape
print arr.size
print arr

print arr.max()
print arr.min()

#question 2

print arr.reshape(2, 2, 2)
#print np.reshape(arr, (2, 2, 2))

print np.transpose(arr)
#print arr.transpose()

print arr.ravel() #ravel = flattened

print arr.astype(np.float64)






