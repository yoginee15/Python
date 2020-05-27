def fib(n):
    series = []
    if n==0:
        series.append(n)
    else:
        i=2
        a= 0
        b= 1
        series.append(a)
        series.append(b)
        while i<n:
             sum = a+b
             series.append(sum)
             i+=1
             a=b
             b=sum
    return series

print(fib(5))


def fib(n):
    series = []
    if n==0:
        series.append(n)
    else:
        a= 0
        b= 1
        series.append(a)
        series.append(b)
        for i in range(2,n):
             sum = a+b
             series.append(sum)
             a=b
             b=sum
    return series

print(fib(5))

