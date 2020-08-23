m, n = list(map(int, input().split()))

disjoint_set = [x for x in range(0, m)]


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


for i in range(n):
    node = list(map(int, input().split()))
    union_set(node[0]-1, node[1]-1)

a = []
for i in range(m):
    a.append(find_set(i))

print(len(set(a)))
