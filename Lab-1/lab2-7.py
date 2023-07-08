def divisibility(num):

    if num % 3 == 0 and num % 7 == 0:
        return True
    else:
        return False

print(divisibility(int(input("Value: "))))
