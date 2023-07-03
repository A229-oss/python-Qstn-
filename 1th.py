

# 1. Boolean checkZero(int[] numberList) check the array numberList has one and only one zero in it.Only use a single For loop.Assume there are n numbers in the array


def checkZero(numberList):
    zeroCount = 0
    for num in numberList:
        if num == 0:
            zeroCount += 1
            if zeroCount > 1:
                return False

    return zeroCount == 1
arr1=[1,2,3,4]
print(checkZero(arr1))
arr2=[0,1,2,3]
print(checkZero(arr2))