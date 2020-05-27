def greet(name):
    print("Hello ",name)

greet("Yoginee")

def update(x):
    print(x,id(x))
    x=8
    print(x,id(x))

x=10
print(x,id(x))
update(x)