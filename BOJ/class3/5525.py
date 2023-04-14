## 5525번 IOI: I와 O로 이루어진 문자열 S에서 N+1개의 I와 N개의 O가 교차로 이루어진 문자열이 몇개 존재하는지 출력
## 일반적으로 순회하면 2번 부분문제까지 풀지 못함.
## 기본단위인 IOI가 몇번 매칭되었는지 숫자를 카운트하면서 N개가 넘어갈때마다 정답 카운트 한개씩 추가

n = int(input())
m = int(input())
s = input()

cnt=0
ucnt = 0

idx = 3
while idx  <= m:
    k = s[idx-3:idx]
    if s[idx-3:idx] == 'IOI':
        ucnt = ucnt + 1
        if ucnt >= n :
            cnt = cnt + 1
        idx = idx + 2
    else:
        ucnt = 0
        idx= idx +1
print(cnt)