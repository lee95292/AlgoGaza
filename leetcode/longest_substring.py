"""
Given a string s, find the length of the longest substring without repeating characters.

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)  < 2 :
            return len(s)
        st, ed,answer = 0,0,0
        ordDict = {}
        ordDict[s[st]] = st
        while ed < len(s)-1:
            ed+=1
            passOrd = ordDict.get(s[ed])
            
            ordDict[s[ed]] = ed
            if passOrd != None and passOrd >= st:
                st = passOrd+1
                ordDict[s[st]] = st

            answer = max(ed-st+1, answer)
        return answer
        


if __name__ =='__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(" "))
