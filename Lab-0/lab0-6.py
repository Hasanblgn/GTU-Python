def calculateVolume(radius,height):
    import math
    return "Cylinder Value: {:.2f} m^2".format(math.pi * radius**2  * height)


r = int(input("Radius:"))
h = int(input("Height:"))

print(calculateVolume(r,h))