lst = [20,25,14,19,16,24,28,26]

def evenOdd(list):
    even = []
    odd = []
    for i in lst:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd

even,odd = evenOdd(lst)
print("Even with count",even,len(even))
print("Odd with count",odd,len(odd))