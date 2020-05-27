from Calc import  *

def decorator(func):
    def swapNums(a,b) :
        if a<b:
            a,b = b,a
        return func(a,b)
    return swapNums

div = decorator(div)
print("Div ",div(2,12))

sub = decorator(sub)
print("Sub ",sub(2,12))

print("Module name",__name__)