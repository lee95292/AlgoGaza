# Definition for a binary tree node.
# https://leetcode.com/problems/range-sum-of-bst/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.answer=0
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def travel(node):
            if node.left == None and node.right == None:
                return
            
            if low <= node.val <= high:
                self.answer += node.val
            if node.left: 
                travel(node.left)
            if node.right:
                travel(node.right)
        return self.answer

if __name__ == '__main__':
    s = Solution()
    s.rangeSumBST([10,5,15,3,7,13,18,1,None,6],6,10)