# create array- 
# 1D array - it is same as 
import numpy as np
arr1 = np.array([1,2,3,4,5])
print(arr1)
print("separations")
b=[1,2,3,4,5]
print(b)

#2D array - the array of arrays 

print("separations")
arr2 = np.array([[1,3,4,4,4],[6,7,8,45,4]])
print(arr2)

#3D array-
print("separations")
arr3 = np.array([[[1,2,3],[4,5,6]],[[3,2,1],[7,8,9]]])
print(arr3)

# check datatypes of array-

print(arr1.dtype)

# check dimension of array-
print(arr2.ndim)
print(arr3.ndim)

# chect array shape-

print(arr3.shape)