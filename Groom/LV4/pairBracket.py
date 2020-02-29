bracket = input()

flag = True
bracketCase = {'(': 1, '{': 2, '[': 3, ')': 4, '}': 5, ']': 6}
stack = []
for i in bracket:
    if(bracketCase[i] < 4):
        stack.append(bracketCase[i])
    elif(stack.pop() != bracketCase[i]-3):
        flag = False
print(flag)
