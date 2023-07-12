#-- Base 4 representation
l1 = {0, 1, 2, 3}
def base_4(value):
    value = abs(value)
    for col in l1:
        for cl in l1:
            for y in l1:
                if 4 ** 2 * col +  4**1 * y + 4 ** 0 * cl == value:
                    if col == 0 :
                        return f"{y}{cl}"
                    else:
                        return f"{col}{y}{cl}"
print(base_4(-27))




#%%

