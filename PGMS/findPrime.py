import math
def findPrime(num):
    prime=[x for x in range(2,num+1)]

    bound=int(math.sqrt(num))+1
    for i in range(2,bound):
        j=2
        while(i*j<=num):
            if(i*j in prime):    
                prime.remove(i*j)
            j+=1
    
    return prime

def solution(numbers):
    answer = 0
    numlist= [int(i) for i in numbers]
    numlist.sort()
    max=0
    for i in range(0,len(numbers)):
        max+=pow(10,i)*numlist[i]
    
    primeList=findPrime(max)
    
    for prime in primeList:
        slicedPrimeList=[int(x) for x in str(prime)]
        print(slicedPrimeList)
        flag=1
        for s in slicedPrimeList:
            if(s not in numlist):
                flag=0
            else:
                slicedPrimeList.remove(s)
        if(flag==1):
            answer+=1
            print(prime)
    return answer

solution("17")


a=[1,2,3,4]

for i in a:
    if(i==1):
        a.remove(4)
        
print(a)    
# 숫자들을 재배열해 가장 큰 수를 만든다. - O(a)
# 헤딩 슷지범위 이내 소수들을 모두 구한다(아리스토테네스의 체) O(sqrt(n))
# 모든 재배열한 순자들에서 소수를 찾는다 - O(a*sqrt(n))