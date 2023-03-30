T = int(input())
for t  in range(T):
    di = {}
    N,L,F = map(int,input().split())
    words = list(input().split())
    for i in range(N):
        ke = str(words[i][L-F:])
        if di.get(ke) == None:
            di[ke] = 0
        di[ke] += 1
    answer = 0
    # print(di)
    for k,v in di.items():
        answer += v//2
    print(answer)




