def solution(flowers):
    answerMap = [0] * 366
    
    for flowerDates in flowers:
        for day in range(flowerDates[0], flowerDates[1]):
            answerMap[day] = 1

    answer = sum(answerMap)
    return answer
