# lab2 4. Problem

inp1 = str(input("Please enter: "))

vowels = {"a","e","i","o","u","A","E","I","O","U"}

if len(inp1) > 100 or len(inp1) < 0:
    raise ValueError("Please enter value between size [0,100] ")


piece = 0
for col in vowels:
    if col in inp1:
        piece += 1

print(f"your input has piece of vowels letter: {piece}")