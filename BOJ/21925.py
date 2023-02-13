"""
21925 짝수 펠린드롬 투포인터 일종

Test Cases
10
1 1 5 6 7 7 6 5 5 5
-> 3

6
1 2 3 3 2 2
-> -1

8
1 1 2 3 3 2 1 1
-> 3

6
1 2 3 3 2 1
-> 1

6
1 2 1 1 2 1
-> 1
"""

N = int(input())
seq = list(map(int,input().split()))

st = 0
answer = 0
flag = False
while st+1 < N:
    k = 0
    # is 펠린드롬?
    while True:
        if seq[st:st+k+1] == seq[st+k+1:st+2*k+2][::-1]:
            answer +=1
            st  += 2*k+2
            break
        if st+2*k+2 >= N:
            flag = True
            break
        k+=1
    if flag:
        break

if flag:
    print(-1)
else:
    print(answer)