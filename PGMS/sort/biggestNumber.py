def solution(numbers):
    numLen = len(numbers)
    answer = ''
    numbers = sorted(numbers, key=lambda number: str(number)[0])
    numbers.reverse()
    for x in range(0, numLen):
        for y in range(numLen-1, x-1, -1):
            if(x == y):
                continue
            if(str(numbers[x])[0] == str(numbers[y])[0]):
                a = ''.join([str(numbers[x]), (str(numbers[y]))])
                b = ''.join([str(numbers[y]), (str(numbers[x]))])
                if(a < b):
                    numbers[x], numbers[y] = numbers[y], numbers[x]

    return answer.join([str(i) for i in numbers])


print(solution([3, 30, 34, 5, 9]))
print(solution([6, 10, 2]))
print(solution([0]))
print(solution([67, 65, 61, 99, 32, 50, 75, 54, 80, 31, 64, 95, 12,
                14, 4, 70, 9, 23, 62, 85, 44, 74, 38, 63, 45, 85, 63, 52, 32]))
