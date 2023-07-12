# Problem -8 Valid Bracket.

def train(value):

    length = len(value)

    if length % 2 != 0:
        return False

    length_v2 = length / 2
    length_v2 = int(length_v2)

    for col in range(length_v2):

        if value[col] == value[-(col+1)]:

            return True

        else:

            return False



print(train(input(("Enter input: "))))
