def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

def main(a,b):
    print(add(a,b))
    print(sub(a,b))
    print(mul(a,b))
    print(div(a,b))

if __name__ == "__main__":
    main(9,3)

print("Module name",__name__)