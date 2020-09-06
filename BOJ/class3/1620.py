n, m = list(map(int, input().split()))

itoa = {}
atoi = {}

for i in range(1, n+1):
    qs = input()
    itoa[i] = qs
    atoi[qs] = i

for i in range(m):
    qst = input()
    if(qst.isalpha()):
        print(atoi[qst])
    else:
        print(itoa[int(qst)])
