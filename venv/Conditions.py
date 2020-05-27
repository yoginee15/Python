x = int(input("Enter number"))
r = x%2
if r==0:
    print("You entered even number")
else:
    print("You entered odd number")

if x>0:
    print("You entered positive number")
elif x<0 :
    print("You entered negative number")
elif x==0:
    print("You entered zero")
else :
    print("Please enter number. You entered "+ type(x))