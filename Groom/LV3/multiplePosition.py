num = input()
unit = [int(x) for x in num]
lu = len(unit)
cands = []
for i in range(1, len(num)):
    cands.append([unit[x] for x in range(0, i)])
    cands[i-1].extend([9 for x in range(i, lu)])
    cands[i-1][i-1] = cands[i-1][i-1]-1
cands.append(unit)

ans = 0

for c in cands:
    tmp = 1
    for x in c:
        if(x != 0):
            tmp *= x
    ans = max(tmp, ans)
print(ans)
