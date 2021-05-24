# 235. Lowest Common Ancestor of a Binary Search Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # tree is empty
        if root is None:
            return None
        
        # DFS
        if root.val > q.val and root.val > p.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < q.val and root.val <p.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        # # DFS        
        # while root:
        #     if root.val > q.val and root.val > p.val:
        #         root = root.left
        #     elif root.val <q.val and root.val <p.val:
        #         root = root.right   
        #     else:
        #         return root
