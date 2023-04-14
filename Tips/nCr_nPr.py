
def nPr(n,r):
    answer=[]
    visit = [False]*n
    P = [x for x in range(1,n+1)]
    def recursion(n,r,rc,pt):
        if pt >= n: return
        if rc == r: 
            ret = []
            for i in range(n):
                if visit[i]: ret.append(P[i]+1)
            answer.append(ret)
            return
        
        for i in range(pt,n):
            visit[i] = True
            recursion(n,r,rc+1,i+1)
            visit[i] = False
    recursion(n,r,0,0)
    return answer


print(nPr(4,2))