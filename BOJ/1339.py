N = int(input())
alphaSet = set()
line = []
for i in range(N):
    line.append(input())
    alphaSet.update(list(line[-1]))