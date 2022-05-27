def solution(s):
    answer = 1
    stack = []
    for i in range(len(s)):
        if len(stack) > 0 and stack[-1] == s[i]:
            stack.pop()
        else:
            stack.append(s[i])

    if stack:
        return 0
    else:
        return 1
print(solution("abccbac"))
print(solution("baabaa"))
print(solution("cdcd"))