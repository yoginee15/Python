r = int(input("Enter no. of rows"))
c= int(input("Enter no. of cols"))
i=1
# num=1;
# while i<=r:
#     j=0
#     while j<c:
#         print(num,end=" ")
#         j=j+1
#         num = num + 1;
#     print("\n")
#     i=i+1

while i<=r:
    j=1
    while j<=i:
        print(" * ",end="")
        j=j+1
    i=i+1
    print("")