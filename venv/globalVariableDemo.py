a=10

def update(a):
    a = globals()['a']
    print(a)

print(a)
update(a)
print(a)
