st = input()
k = ''
number = []
ops = []
for i in st:
    if i != '+' and i != '-':
        k+=i
    else:
        ops.append(i)
        number.append(int(k))
        k=''
number.append(int(k))

# print(number,ops)
mi = 0
mit = False
answer = number[0]
for i in range(len(ops)):
    if ops[i] == '-':
        mit = True
        mi += number[i+1]
    if ops[i] == '+':
        if mit: mi += number[i+1]
        else: answer += number[i+1]
print(answer-mi)