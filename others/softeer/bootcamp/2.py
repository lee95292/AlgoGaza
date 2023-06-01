import heapq
n = int(input())

que = []
cnt = {}


def getMaxCnt():
    max = 0
    for k,v in cnt.items():
        if max < v:
            max = v
    return max


for i in range(n):
    op = input()
    alp = ''
    if len(op) > 7:
        op, alp = op.split()

    if op =='enqueue':
        que.append(alp)
        if cnt.get(alp) == None : cnt[alp] =1 
        else: cnt[alp] +=1
    else:
        maxcnt = getMaxCnt()
        if len(que) == 0: 
            print('*')
            continue
        for i,q in enumerate(que):
            if cnt[q] == maxcnt:
                que.remove(q)
                cnt[q]-=1
                print(q, end= ' ')
                break


