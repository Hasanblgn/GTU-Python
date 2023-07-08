def factorial(num):

    if num < 0:
        raise ValueError("please enter pozitive value")
    elif num == 1 :
        return 1
    elif num == 0:
        return 1
    return num * factorial(num-1)

number = int(input("Please enter number: "))
try:
    print(factorial(number))

except Exception as e:
    print("Error code: ",e)

