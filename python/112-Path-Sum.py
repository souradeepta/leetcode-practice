# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return None
        rem = 0
        node = root
        # while node:
        rem = sum-node.val
        while node:
            if node.left is not None or node.right is not None:
                return self.hasPathSum(node.left , rem) or self.hasPathSum(node.right, rem)
            elif rem == 0 and node.left is None and node.right is None:
                return True
            else:
                return False
            
        
#         if not root:
#         return False

#         sum -= root.val
#         if not root.left and not root.right:  # if reach a leaf
#             return sum == 0
#         return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
            
        