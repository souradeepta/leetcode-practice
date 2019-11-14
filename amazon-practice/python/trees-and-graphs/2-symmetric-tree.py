#  Symmetric Tree
# Complexity:: Time:O(n), Space:O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isMirror(root, root)    

    def isMirror(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        elif t1 is None or t2 is None:
            return False
        
        return (t1.val == t2.val) and self.isMirror(t1.left, t2.right) \
            and self.isMirror(t2.left, t1.right)

    # iterative solution
    def isSymmetric2(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        stack = [[root.left, root.right]]

        while stack:
            left, right = stack.pop()

            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False

            return True

        
