def solution(s):
    answer = 0
    for i in range(0,len(s)):
        k = 1
        temp1 = 0
        while i-k >= 0 and i + k < len(s):
            if s[i-k] == s[i+k]:
                temp1+=1
            else:
                break
            k+=1
        
        k=1
        temp2 = 0 
        while i-k +1>= 0 and i + k < len(s):
            if s[i-k+1] == s[i+k]:
                temp2+=1
            else:
                break
            k+=1

        answer = max(2*temp1+1,2*temp2,answer)
        
    return answer

print(solution("aa"))
print(solution("abba"))