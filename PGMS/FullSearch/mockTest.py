def solution(answers):
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    correct = [0, 0, 0, 0]
    answer = []
    l1, l2, l3 = len(supo1), len(supo2), len(supo3)

    for i in range(0, len(answers)):
        if(supo1[i % l1] == answers[i]):
            correct[1] += 1
        if(supo2[i % l2] == answers[i]):
            correct[2] += 1
        if(supo3[i % l3] == answers[i]):
            correct[3] += 1
    print(correct)

    maxc = max(correct)
    for i in range(0, len(correct)):
        if(correct[i] == maxc):
            answer.append(i)
    return answer


print(solution([1, 2, 3, 4, 5]))
print(solution([1, 3, 2, 4, 2]))
