def solution(people, limit):
    people.sort()
    people.reverse()

    rescueBoat ={x:limit for x in range(0, len(people))}
    pivot = people[len(people)-1]
    answer = 0
    for weight in people:
        boatLen=len(rescueBoat)-1
        newBoat=0
        for i in range(newBoat,len(rescueBoat)):
            
            flag=False
            for j in range(newBoat,0,-1):
                if(rescueBoat[j]-weight >= 0):
                    rescueBoat[j] -= weight
                    flag=True
                    break
                    if(rescueBoat[j] < pivot):
                        rescueBoat.pop(boatLen-i)
                        answer += 1 
            
            if(flag):
                break
        # for i in range(0, len(rescueBoat)):
        #     if rescueBoat[i]-weight >= 0:
        #         rescueBoat[i] -= weight
        #         break
    for i in rescueBoat:
        if(rescueBoat[i] != limit):
            answer += 1
    return answer

print(solution([70, 50, 80, 50,30],100))