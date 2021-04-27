def tringle_type(a, b, c):
    if a == b == c:
        print("isoscele")
    elif a == b:
        print("equal triangle")
    elif a != b != c:
        print("simple")
    else:
        print("There is no such a tringle")
        return a, b, c


print(tringle_type(3, 4, 6))
