def perimiterCircle(edge):
    """
    The function main duty is calculate the perimeter of square

    Args:
        num1 (float, integer): length of square edge.

    """
    return f"The perimeter of square is {4 * edge:.1f}."


sideOfEdge = float(input("Edge of square :"))
print(perimiterCircle(sideOfEdge))