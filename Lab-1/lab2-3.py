#%%
# Slicing name variables

name = str(input("Name: "))
idx1 = int(input("First Index: "))
idx2 = int(input("Second Index: "))
# -> It getten mod due to get rid of negatif value 
idx1 = idx1 % len(name)
idx2 = idx2 % len(name)

indexMin = min(idx1, idx2)
indexMax = max(idx1, idx2)

print(name[indexMin:indexMax+1])