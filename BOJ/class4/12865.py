"""
평범한 배낭, 0-1 knapsack
"""
N,K = map(int,input().split())
dp = []
products=[]
for i in range(N):
    products.append(list(map(int,input().split())))

products.sort(key = lambda  x: x[0])

for i in range(N):
    w, v = products[i]
    for j in range(w,K+1):
        dp[j] = v
    for j in range(K+1,w-1,-1):
        dp[j] = 

print(dp)

