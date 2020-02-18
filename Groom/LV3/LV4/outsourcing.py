n = input()
n = int(n)

request = []
deadlineMax = 0

for i in range(n):
    request.append(list(map(int, input().split())))
    if(request[i][1] > deadlineMax):
        deadlineMax = request[i][1]
request.sort(key=lambda x: x[1])

schedule = [[] for _ in range(n+1)]
for r in request:
    schedule[r[1]].append(r[0])

ans = 0
rev = []
for i in range(deadlineMax, 0, -1):
    rev.extend(schedule[i])
    lrev = len(rev)
    if(lrev == 0):
        continue
    if(lrev > 2*i):
        rev.sort()
        rev = rev[i-1:]
    m = max(rev)
    rev.remove(m)
    ans = ans+m

print(ans)
