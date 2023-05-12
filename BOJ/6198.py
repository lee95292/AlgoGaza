import sys
input = sys.stdin.readline
n = int(input())
arr = []
accsum = []
stack = []
answer = 0
for i in range(n):
    arr.append(int(input()))
    accsum.append(arr[-1])
    if i > 0: accsum[-1] += accsum[-2]
arr.append(10**10)
for i in range(n+1):
    if len(stack) == 0: 
        stack.append([i,arr[i]])
        continue

    if stack[-1][1] > arr[i]:
        stack.append([i,arr[i]])
        continue
    
    while len(stack) > 0 and stack[-1][1] <= arr[i]:
        idx, val = stack.pop()
        # print('between,',idx+1,',',i+1)
        answer += i - idx -1
    stack.append([i,arr[i]])
# print(stack)
print(answer)