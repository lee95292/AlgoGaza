"""
https://leetcode.com/problems/validate-stack-sequences/submissions/
"""

class Solution:
    def validateStackSequences(self, pushed: list[int], popped: list[int]) -> bool:
        st = []
        pidx = 0 
        for i in range(len(pushed)):
            st.append(pushed[i])
            print(st)
            while len(st) > 0 and len(popped) > 0 and st[-1] == popped[pidx]:
                st.pop()
                pidx+=1
                print(st)
        return len(st) == 0


if __name__ == '__main__':
    s = Solution()
    print(s.validateStackSequences(pushed=[1,2,3,4,5], popped = [4,5,3,2,1]))
    print(s.validateStackSequences([1,0,2], [2,1,0]))
