"""
세 용액, 투포인터
"""
N = int(input()) # < 5000, n**2
numbers = list(map(int, input().split()))
numbers.sort()
minValue = 10**9 * 3 +1
answer = []
for i in range(N-2):
    l,r = i+1, N-1

    while l  < r:
        numberSum = numbers[l] + numbers[r] + numbers[i]
        if abs(numberSum) < minValue:
            minValue = abs(numberSum)
            answer = [numbers[l] , numbers[r] ,numbers[i]]

        if numberSum == 0 :
            answer.sort()
            print(*answer)
            exit(0)
        elif numberSum < 0:
            l +=1
        else:
            r-=1

answer.sort()
print(*answer)