from numpy import *

#Aliasing
arr = array([1,2,3,4,5])
arr1 = arr;
print(arr)
print(arr1)

print(id(arr))
print(id(arr1))

#Copy
arr3 = arr1.view()
print(arr3)

#Deep copy:
arr4 = arr1.copy()

print(arr1.size)

arrMatrix = array([
    [1,2,3,4],
    [5,6,7,8]
])
print(arrMatrix)
m= matrix('1,2,3,4;5,6,7,8')
print(m)
print(m.min())
print(m.max())
m3 = m*m

