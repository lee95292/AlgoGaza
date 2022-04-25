"""
kakao 2019 인턴십 코테 #3 불량 사용자 easy~medium
시간복잡도 제약조건이 없어서 O(N^2) DFS로 편하게 풀었다.
유저 아이디 길이가 최대 8인것을 이용하면 더 빠르게 풀 수 있을듯 한데..
"""
user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]
# banMap = user id > banned id 매칭, 
# banMap

ban_match = []

def isMatch(u,b):
    lu = len(u)
    if lu != len(b):
        return False

    for i in range(lu):
        if b[i] == '*':
            continue
        if b[i] != u[i]:
            return False
    return True


def user_ban_match ():
    for b in banned_id:
        regban = []
        for idx,u in enumerate(user_id):
            if isMatch(u,b):
                regban.append(idx)
        ban_match.append(regban)

user_ban_match()

ans= []
# get은 리스트에 들어간 밴아이디 리스트, k는 ban_match의 인덱스
def dfs(get,k): 
    if k==len(ban_match):
        if set(get) not in ans:
           ans.append(set(get))
        return get
    for idx in ban_match[k]:
        if idx not in get:
            get_ = get.copy()
            get_.append(idx)
            dfs(get_,k+1)
dfs([],0)
print(len(ans))