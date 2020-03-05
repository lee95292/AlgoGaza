s = input()
while(s != '0'):

    flag = True
    for i in range(len(s)//2):
        if(s[i] != s[-i-1]):
            flag = False
            break

    if(flag):
        print('yes')
    else:
        print('no')
    s = input()
