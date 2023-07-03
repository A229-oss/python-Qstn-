# boolean checkWrongOrWrite(char[]a)
# Check whether the string contains more or equal to three vowels(a,e,i,o,u)if yes then string is false, else true

def checkWrongOrWrite(a):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowel_count = 0

    for char in a:
        if char.lower() in vowels:
            vowel_count += 1
            if vowel_count >= 3:
                return False

    return True


string1 = "hello"
result1 = checkWrongOrWrite(string1)
print(result1)

string2 = "apple"
result2 = checkWrongOrWrite(string2)
print(result2)
