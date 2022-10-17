1  # Definition for a binary tree node.

# class TreeNode:

#     def __init__(self, val=0, left=None, right=None):

#         self.val = val

#         self.left = left

#         self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, left, right):
        if left and right:
            return left.val == right.val and self.dfs(left.left, right.right) and self.dfs(
                left.right, right.left
            )
        return left == right
    def isSymmetric_iterative(self, root):
        if not root:
            return True
        stack = [(root.left, root.right)]

        while stack:
            l, r = stack.pop()
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            stack.append((l.left, r.right))
            stack.append((l.right, r.left))

        return True