N = int(input())
di = {
    '10':4,
    '11':3,
    '01':2,
    '00':1
}
for i in range(N):
    t = input()
    answer = 0
    def r(idx, st,isR):
        print(st,idx+1,isR)
        if idx == len(st)-2: 
            ret = di[st[idx:idx+2]]
            if isR: ret = 4 - ret
            return ret
        
        k = 0
        if t[idx+1] == '1':
            k = r(idx+1,st,True)
        else:
            k = r(idx+1,st,False)

        if isR:
            k += 2**(len(t)-1-idx)
        return k
    answer = r(0,t,t[0] == '1')
    print(answer)







