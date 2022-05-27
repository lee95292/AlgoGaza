n, m = list(map(int,input().split()))

if m > n//2:
    m = n-m
ans= 1
l = []
for i in range(m):
    ans *= n-i
    l.append(i+1)
    while len(l) > 0 and ans % l[-1] == 0 :
        ans //= l.pop()
while len(l) > 0 and ans % l[-1] == 0 :
    ans //= l.pop()
    
print(ans)
