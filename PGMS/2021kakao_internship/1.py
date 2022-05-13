s = "one4seveneight"


tmp =''
result =''
numMap ={'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9','zero':'0'}
tmp = ''
for i in s:
    if i.isnumeric():
        result = result + i
    elif numMap.get(tmp+i):
        result = result + numMap[tmp+i]
        tmp=''
    else:
        tmp = tmp + i


print(result)