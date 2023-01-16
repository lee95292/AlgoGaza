s = input()

for i in range(0, len(s)//2):
    print(s[i]+s[-i-1], end='')

if(len(s) % 2 == 1):
    print(s[len(s)//2])
