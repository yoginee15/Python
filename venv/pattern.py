r = int(input("Enter no. of rows"))
c= int(input("Enter no. of cols"))

# for i in range(r):
#     for j in range(c):
#         print("# ",end="")
#         j+=1
#     print("")
#     i+=1

# for i in range(r):
#     for j in range(i+1):
#         print("# ",end="")
#         j+=1
#     print("")
#     i+=1

# for i in range(r):
#     for j in range(i+1):
#         print("# ",end="")
#         j+=1
#     print("")
#     i+=1

# for i in range(r):
#     print(" ", end="")
#     for j in range(r):
#         print("# ",end="")
#         j+=1
#     print("")
#     i+=1

for i in range(r,0,-1):
    for j in range(i):
        print("# ",end="")
        j-=1
    print("")
    i-=1