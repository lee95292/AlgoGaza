n = int(input())
pv, cur = 1,1
MOD = 10**9 + 7
answer = 1
for i in range(3, n+1):
	tmp = cur
	cur = cur + pv
	pv = tmp
	if n%2 == i%2:
		answer = (answer + cur) % MOD
print(answer)