s = input()
bombstr = input()
bomblen = len(bombstr)
stack = []
for i in range(len(s)):
    stack.append(s[i])
    if i+1>= bomblen and ''.join(stack[-bomblen:]) == bombstr:
        for _ in range(bomblen):
            stack.pop()
        # stack = stack[:len(stack)-bomblen]
    
if stack: print(''.join(stack))
else: print("FRULA")
# 11111111111111111111111111111111111111111111111111111234234234234234234234234234234234234
# 12312312312312312312312312312312312312312312312312312344444444444444444444444444444444444444444444444444444444444444444444
# 11234234