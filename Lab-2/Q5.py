def reversingString(val):

    val = val[::-1]
    return val

rstring = input("Enter a string: ")

assert len(rstring) >= 0 and 100 >= len(rstring)

print(reversingString(rstring))


