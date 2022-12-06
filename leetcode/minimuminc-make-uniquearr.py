"""
https://leetcode.com/problems/minimum-increment-to-make-array-unique/
"""

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()
        now = nums[0]
        # print(nums)
        move = 0
        for idx, num in enumerate(nums):
            if idx == 0:
                continue
            if now >= num:
                now = now+1
                move += now - num
                nums[idx] = now
            else:
                now = num
        # print(nums)
        return move
        


if __name__ =='__main__':
    s = Solution()
    print(s.minIncrementForUnique([3,2,1,2,1,7]))
    print(s.minIncrementForUnique([3,2,1,2,1,7,7,7,8]))

