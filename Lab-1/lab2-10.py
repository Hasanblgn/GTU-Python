
def squareRoots(number):
    for a in range(2,number//2,0.1):
        if number / 2*a**2 == 0:
            return a


number = squareRoots(float(input("Enter a Value: ")))
print(number)

