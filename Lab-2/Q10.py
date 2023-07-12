# Maze

def maze(value):
    w = 0
    s = 0
    n = 0
    e = 0
    coordinate = (0,0,0,0)
    for col in value:
        if col == "w":
            w += 1
        elif col == "s":
            s += 1
        elif col == "n":
            n += 1
        elif col == "e":
            e += 1

    coordinate = coordinate + (w, n, e, s)

    direction_y = -s + n
    direction_x = -e + w

    direction = (direction_y ** 2 + direction_x **2) ** 0.5

    return direction


print(maze(input("Enter the exit route: ")))
