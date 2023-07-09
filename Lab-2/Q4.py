
def lucasNumber(number):

    if number == 0:
        return 2
    elif number == 1:
        return 1
    elif number > 0:
        l2 = lucasNumber(number-2) + lucasNumber(number-1)
        return l2


lcNum = int(input("Value: "))
assert lcNum >= 0 and 1E6 >= lcNum
print(lucasNumber(lcNum))