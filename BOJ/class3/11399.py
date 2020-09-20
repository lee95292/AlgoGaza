n = int(input())
l = list(map(int, input().split()))

l.sort()
k = [l[0]]
for i in range(1,len(l)):
    k.append(l[i] + k[i-1])

print(sum(k))
