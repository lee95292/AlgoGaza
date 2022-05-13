from itertools import permutations

expression ="100-200*300-500+20"
expression ="50*6-3*2"
expression ="200-300-500-600*40+500+500"

debug = True
exps = []
s=''
for idx,i in enumerate(expression):
    if 48 <= ord(i) <58:
        s = s + i
    else:
        exps.append(s)
        exps.append(i)
        s=''
    if idx == len(expression)-1:
        exps.append(s)

# * + -
maxV = 0

prior = permutations(['0','1','2'],3)

for pr in prior :
    ops_pr = {'*':pr[0], '+': pr[1], '-':pr[2]}
    stack = []
    res_exp =[]

    for u in exps:
        if u.isnumeric():
            res_exp.append(u)
        else:
            # 연산자인 경우
            while stack and ops_pr[u] < ops_pr[stack[-1]]: #스택에서 현재 값보다 우선순위 높은것들 빼내기
                res_exp.append(stack.pop())
            stack.append(u)
    while stack:
        res_exp.append(stack.pop())
    
    stack = []
    if debug:
        print(pr)
        print(res_exp)
    for idx,ex in enumerate(res_exp):
        tmp = []
        while idx+1 < len(res_exp) and not ex.isnumeric() and res_exp[idx] == res_exp[idx+1] and stack:
            tmp.append(stack.pop())
        if ex.isnumeric():
            stack.append(int(ex))
        elif ex == '*':
            stack.append(int(stack.pop()) * int(stack.pop()))
        elif ex == '+':
            stack.append(int(stack.pop()) + int(stack.pop()))
        elif ex == '-':
            a1 = int(stack.pop())
            a2 = int(stack.pop())
            stack.append(a2-a1)
        while tmp:
            stack.append(tmp.pop())
        if debug:
            print('stack',stack)

    maxV= max(abs(int(stack[0])),maxV)

print(maxV)
