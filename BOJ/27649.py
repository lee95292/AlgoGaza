line = input()

splitter = {
    '<':True,
    '>':True,
    '&&':True,
    '||':True,
    '(':True,
    ')':True,
    ' ':True,
}
st = ''
ctnFlag= False
tokens = []
for i in range(len(line)):
    if ctnFlag: 
        ctnFlag= False
        continue
    if splitter.get(line[i]):
        if len(st)> 0: tokens.append(st)
        if line[i]!=' ':tokens.append(line[i])
        st=''
    elif i+2< len(line) and splitter.get(line[i:i+2]):
        if len(st)> 0: tokens.append(st)
        tokens.append(line[i:i+2])
        ctnFlag=True
        st=''
    else:
        st += line[i]
if len(st)> 0: tokens.append(st)

answer=''

for i,t in enumerate(tokens):
    if t != ' ':
        if i < len(tokens)-1:
            print(t,end=' ')
        else: print(t,end='')
