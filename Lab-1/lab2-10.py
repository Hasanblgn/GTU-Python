def squareRoot(number):
    x = number
    y = 1
    e = 0.000001 # -> Accuracy level
    y = float(y)
    x = float(x)
    while x - y > e :

        x = (x+y)/2
        y = number / x

    return x



print(squareRoot(int(input(":"))))