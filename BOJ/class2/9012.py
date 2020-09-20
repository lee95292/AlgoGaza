tc = int(input())

for i in range(tc):
    braket = input()
    flag = True
    stack = []
    for i in braket:
        if(i == '('):
            stack.append(i)
        elif(i == ')'):
            if(len(stack) == 0 or stack.pop() != '('):
                flag = False
                break
    if(len(stack) != 0 or flag == False):
        print('NO')
    else:
        print('YES')
