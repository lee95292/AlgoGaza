n = input()
n = int(n)
ans = 0
for i in range(1, 15):
    if(5**i <= n):
        ans = ans+n//5**i

print(ans)
