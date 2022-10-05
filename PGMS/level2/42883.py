def solution(number, k):
    nums = [[] for _ in range(10)]

    for idx, n in enumerate(number):
        nums[int(n)].append(idx)

    answer = ''
    print(nums)
    for i in range(len(number)-k):
        for j in range(9,-1,-1):
            if len(nums[j]) > 0 and nums[j][0] <= i :
                print(nums[j][0],i)
                nums[j].pop(0)
                answer += str(j)
                break
    return answer


print(solution("1231234", 3))