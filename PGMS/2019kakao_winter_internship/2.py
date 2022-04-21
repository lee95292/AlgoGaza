from typing import Set


s="{{2},{2,1},{2,1,3},{2,1,3,4}}"	

# 문자열 파싱 : An 을 원소로 하는 리스트로 만들기
s= s[1:len(s)-1].replace('{','')
s = s.split('},')
s[len(s)-1] = s[len(s)-1].replace('}','')

# 문자열 길이로 정렬
s = sorted(s, key = len) 

answer = [int(s[0])]
for i in range(len(s)):
    s[i] = s[i].split(',')    

    if i == 0:
        continue
    answer.append(int(list(set(s[i]) -set(s[i-1]))[0]))
print(answer)