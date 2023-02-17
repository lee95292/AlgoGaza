"""
BOJ 1759 암호 만들기
Combination라이브러리 사용해도 되지만, Combination 직접구현 오랜만에 해봄
"""
r,n = map(int,input().split())
li = list(input().split())
li.sort()
answer = []
strs = [False for _ in range(n)]
answer = []
mo = ['a','e','i','o','u']
def addAnswerFromBool():
    jcnt, mcnt = 0,0
    ret = ''
    for i in range(n):
        if strs[i]:
            ret += li[i]
            if li[i] in mo: mcnt+=1
            else: jcnt+=1
    if mcnt > 0 and jcnt >1:
        print(ret)
        

    
def bt(n, r, cur, pick):
    if r == pick:
        addAnswerFromBool()
        return
    if pick > r or cur >= n: return
    strs[cur] = True
    bt(n, r,cur+1, pick+1)
    strs[cur] = False
    bt(n, r,cur+1, pick)

bt(n,r,0,0)