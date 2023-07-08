def divisibility_2(number):
    for col in range(2,number//2):
        if number % 3 == 0 and number % 7 == 0:
            return 3
        elif number % 7 == 0 and number % col != 0:
            return 2
        elif number % 3 == 0 and number % col != 0:
            return 1
        else:
            return "There is no options that you want."

print(divisibility_2(int(input("Value: "))))
