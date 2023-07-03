#Boolean cheakUnique(char[]word)
#Check if all charcters in the string are unique

def checkUnique(word):
    char_set = set(word)
    return len(char_set) == len(word)

word = "mobile"
result = checkUnique(word)
print(result)

word_with_duplicates = "calculator"
result_with_duplicates = checkUnique(word_with_duplicates)
print(result_with_duplicates)
