# Last word length

def lastWordLength(value):
    value = str(value)
    value = value.split(sep=" ")

    return len(value[-1])



print(lastWordLength(input("Enter a string: ")))