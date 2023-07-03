#  int swap(int a, int b)
# swap two numbers without using 3rd number
def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


a = 1
b = 200
a,b=swap(a,b)
print(a, b)


