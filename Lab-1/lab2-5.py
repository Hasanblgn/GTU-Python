def sumUp(num1):

    total = 0

    for col in num1:
        col = int(col)
        total += col

    return total

inpt = str(input("Value: "))

print(sumUp(inpt))