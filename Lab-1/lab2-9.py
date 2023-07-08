def primeNumber(num):
    if num == 2:
        return True

    for col in range(3,(num//2)):

        if num % col == 0:
            return False

        else:
            return True



val = input("Enter a value: ")

print(primeNumber(int(val)))