from itertools import product

catagories = []
catorder = [['j','c','p'],['b','f'],['j','s'],['c','p']]
for i in ['j','c','p']:
        for j in ['b','f']:
            for k in ['j','s']:
                for l in ['c','p']:
                    catagories.append(i+j+k+l)

                

def parseCat(catagory):
    if '-' not in catagory:
        return [catagory]
    pd = []
    for idx,i in enumerate(catagory):
        if i == '-':
            pd.append(catorder[idx])
        else:
            pd.append(i)
    result=[]
    for cat in list(product(*pd)):
        c=''
        for t in cat:
            c+=t
        result.append(c)
    return result

def queryToCat(query):
    query = query.split(' ')
    cat=''
    score =0
    for q in query:
        if q[0] in ['j','c','p','b','f','p','s','-']:
            cat += q[0]
        if ord('0') <= ord(q[0]) <= ord('9'):
            score = int(q)
    return [parseCat(cat), score]

def solution(info, query):
    catagory = {}
    for cat in catagories:
        catagory[cat] = []

    for idx,value in enumerate(info):
        info[idx] = value.split(' ')
        cat = ''
        for i in info[idx]:
            if ord('0') <= ord(i[0]) <=ord('9'):
                continue
            cat +=i[0]
        catagory[cat].append(idx)

    answer = []
    for q in query:
        count = 0
        cats,score = queryToCat(q)
        for cat in cats:
            for apply in catagory[cat]:
                if int(info[apply][-1]) >= score:
                    count += 1
        answer.append(count)
    return answer
print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))