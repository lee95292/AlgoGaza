from itertools import combinations
class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        answer = 0
        maxOr = 0
        for v in nums:
            maxOr |= v
        for i in range(len(nums)+1):
            numsComb = combinations(range(len(nums)), i)
            
            for combi in numsComb:
                subsetOr = 0
                for idx in combi:
                    subsetOr |= nums[idx]
                # print(combi,subsetOr)
                if maxOr == subsetOr:
                    answer+=1
        return answer




if __name__ == '__main__':
    s = Solution()
    print(s.countMaxOrSubsets([3,1,2,5]))
        