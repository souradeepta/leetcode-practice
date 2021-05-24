# 669. Trim a Binary Search Tree
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self, node, L , R):
        if not node:
            return None
        if  node.val > R:
            # node = node.right
            return self.helper(node.left, L, R)
        elif node.val < L:
            # node = node.left
            return self.helper(node.right, L, R)
        else:
            node.left = self.helper(node.left, L,R)
            node.right = self.helper(node.right, L,R )
            return node
            
            
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        else:
            return self.helper(root, L,R )   
