h, w = list(map(int, input().split()))

for x in range(h):
    arr.append(list(map(int, input())))

visit = [[0 for x in range(w)] for y in range(h)]
level = {}

level[(0, 0)] = 1


def step(x, y):
    if(visit[y][x] == -1):  # -1: visit, 0 : not visit
        level[(x, y)] = min(step(x, y)+1, visit[y][x] + 1)

    step
