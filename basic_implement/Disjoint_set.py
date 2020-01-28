size = 10
disjoint_set = [x for x in range(0, size)]


def find_set(x):
    if(disjoint_set[x] == x):
        return x
    else:
        return find_set(disjoint_set[x])


def union_set(x, y):
    xRoot = find_set(x)
    yRoot = find_set(y)

    if(xRoot > yRoot):
        disjoint_set[yRoot] = xRoot
    else:
        disjoint_set[xRoot] = yRoot


union_set(3, 2)
union_set(3, 4)
union_set(4, 6)
