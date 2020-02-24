import math

a = input()
a = int(a)
flag = True
for i in range(2, int(math.sqrt(a))+1):
    if(a % i == 0):
        flag = False

if(flag):
    print('True')
else:
    print('False')
