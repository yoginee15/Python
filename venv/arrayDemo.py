# from numpy import  *
# arr = array([1,2,3,4,5])
# print(arr)
# print(arr.dtype)
#
# vals = 1
# print(vals.buffer_info())
#
# arr1 = array([1,2,3,4,5],float)
# print(arr1)
# print(arr1.dtype)

from array import  *
arr = array('i',[1,2,3,4,5])
print(arr)
print(arr.typecode)

print(arr.buffer_info())

arr1 = array('f',[1,2,3,4,5])
print(arr1)
print(arr1.typecode)

arr1.reverse();
print(arr1)

arr3 = array(arr1.typecode,(a for a in arr1))
print(arr3)

for i in arr3 :
    print(i)

