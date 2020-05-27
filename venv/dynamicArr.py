from array import *

size = int(input("Enter how many elements you want in array"))

arr = array('i',[])
for i in range(0,size):
    ele = int(input("Enter element for "+str(i)+" position"))
    arr.append(ele)

print(arr)

searchEle = int(input("Enter element to search in array"))
for i in range(0,len(arr)):
    if arr[i]==searchEle :
        #print(arr.index(searchEle))
        print("Found element at",i )
        break
else :
    print("Element not found")