# Validate binary search tree
# Complexity:: Time:O(n), Space:O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
    
        upper = float('inf')
        lower = float('-inf')
        
        def helper(node, lower, upper):
            if not node:
                return True
            
            value = node.val

            if  lower >= value or value >= upper:
                return True
            
            if not helper(node.left, lower, value):
                return False
            
            if not helper(node.right, value, upper):
                return False
            
            return True
        
        return helper(root, lower, upper)
            
            