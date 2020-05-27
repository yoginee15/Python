def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        fact = 1
        for i in range(1,n+1):
            fact *= i

    return fact

print(factorial(1))
print(factorial(5))

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(4))