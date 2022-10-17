# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        l = self.depth(root.left)
        r = self.depth(root.right)
        return (
            (abs(l - r) < 2)
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )

    def depth(self, node):
        if node == None:
            return 0
        return max(self.depth(node.left), self.depth(node.right)) + 1
