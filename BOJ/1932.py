import sys
input = sys.stdin.readline
n = input()
n = int(n)

p = []
for i in range(n):
    p.append(list(map(int, input().split())))

for i in range(1, n):
    plen = len(p[i])-1
    p[i][0] = p[i][0]+p[i-1][0]
    p[i][plen] = p[i][plen]+p[i-1][plen-1]

    for j in range(1, plen):
        p[i][j] = p[i][j]+max(p[i-1][j-1], p[i-1][j])

print(max(p.pop()))
