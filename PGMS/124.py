import math
def solution(n):
    answer = ''
    k=math.log(n,3)//1
    l=['4','2','1']
    while n > 0:
        for i in range(3,0,-1):
            if i * k**3 <= n:
                n-= i* k**3
                answer+=l[i-1]
                break
        k-=1
    return answer[::-1]

for i in range(4,10):
    print(i, solution(i))