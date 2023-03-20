H,K,R = map(int,input().split())
works = [[] for _ in range(2**(H+1))]
for i in range(2**H, 2**(H+1)):
    works[i] = list(map(int,input().split()))
day = 0
def msort(level, day):
    if 2**H <= level <2**(H+1) :
        return works[level]
    l,r = msort(level*2,day-1), msort(level*2+1,day-1)
    if day%2 == 0: l,r = r,l
    for i in range(len(l)):
        works[level].append(l[i])
        works[level].append(r[i])
    return works[level]
msort(1,H+1)
answer = 0
for i in range(min(R-H,len(works[1]))):
    answer += works[1][i]
print(answer)
"""
3 1 4
1
2
3
4
5
6
7
8
"""
