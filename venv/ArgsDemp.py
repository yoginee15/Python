def PrintPersonInfo(**person):
    print("Person Info",person)
    for key,value in person.items():
        print(key,value)

PrintPersonInfo(name="Yoginee",age="27",city="Pune")

def PrintPersonInfo(name,**info):
    print("Person Info",info)
    print("name", name)
    for key,value in info.items():
        print(key,value)

PrintPersonInfo(name="Yoginee",age="27",city="Pune")


def sumOfNumber(a,*b):
    sum = a
    for nums in b:
        sum+=nums
    print("Sum=",sum)

sumOfNumber(2,3,4,5,6)
