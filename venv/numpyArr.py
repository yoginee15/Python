from numpy import *
arr = array([1,2,3,4,5])
print(arr)
print(arr.dtype)

arr1 = array([1,2,3,4,5.0])
print(arr1)
print(arr1.dtype)

linArr = linspace(0,15)
print(linArr)
# print('%.2f%',linArr[5])

arangeArr = arange(0,15,2)
print(arangeArr)

zerosArr = zeros(5)
print(zerosArr)

onesArr = ones(5)
print(onesArr)
