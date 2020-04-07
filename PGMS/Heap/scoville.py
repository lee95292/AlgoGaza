def solution(scoville, K):
    answer=0
    while(scoville[0] < K):
        print(scoville)

        answer=answer+1
        a=scoville[0]
        b=scoville[1]
        del scoville[0]
        del scoville[0]
        n = a+2*b
        for i in range(0,len(scoville)):
            if(scoville[i] > n):
                scoville.insert(i,n)
                break
    
    return answer

print(solution([1,2,3,9,10,12],7))