def removingUnwanted(val):
    unwantedVal = "!#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~" + '"'
    for va in unwantedVal:
        if va in val:
            val = val.replace(f"{va}","")
    return val


print(removingUnwanted(str(input("Enter a string: "))))
