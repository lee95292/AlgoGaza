import math



def solution(numbers):
    nums = set()

    maxv = 10**len(numbers)
    isPrime = [True] * maxv
    
    for i in range(2,math.ceil(math.sqrt(maxv))+1):
        if isPrime[i] == False:
            continue
        for j in range(i,maxv):
            if i * j < maxv:
                isPrime[i*j] = False
            else:
                break
    isPrime[1]= False
    isPrime[0]=False

    def addNums(n, nowNumber):
        if n == 1:
            return [*nowNumber]
        ret = []
        for idx,number in enumerate(nowNumber):
            x = [*nowNumber[0:idx], *nowNumber[idx+1:len(nowNumber)]]
            nnums= addNums(n-1, x)
            for num in nnums:
                ret.append([number,*num])
        return ret
    answer = set()
    ret= []

    for i in range(len(numbers)+1):
        ret.extend(addNums(i,numbers))
    count=0
    for num in ret:
        answer.add(int(''.join(num)))
    for ans in answer:
        if isPrime[ans]:
            count+=1
    print(answer)
    return count

print(solution('3333'))
print(solution('011'))