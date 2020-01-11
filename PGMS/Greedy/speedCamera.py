def solution(routes):
    answer = 0
    routesOut = sorted(routes, key=lambda route: route[1])

    lenRout = len(routesOut)
    while lenRout > 0:
        pivot = routesOut[0][1]
        rm = []
        for route in routesOut:
            if(pivot >= route[0]):
                rm.append(route)
        for r in rm:
            routesOut.remove(r)
        answer += 1
        lenRout = len(routesOut)

    return answer


print(solution([[-20, 15], [-14, -5], [-18, -13], [-5, -3]]))

# 1 Out point 기준으로 route 정렬하기 (O nlogn)
# 2 routeOut은 빨리 나가는 차 순서로 정렬됨
# 3 첫 번째 나가는 차를 체크하기 위해 카메라 설치
# 4 카메라에 감지된 차는 리스트에서 제거
# 5 3번으로 돌아가 반복
