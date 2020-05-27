from functools import reduce

nums = [3,2,6,8,4,2,9]

even = list(filter(lambda n : n%2==0,nums))
print("Filter Even",even)

doubled = list(map(lambda n : n*n,nums))
print("Map",doubled)

sumOfAll = reduce((lambda sum,n:sum+n),nums)
print("Sum using reduce",sumOfAll)
