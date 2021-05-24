# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def _inorderRecurr(node, result):
            if node:
                _inorderRecurr(node.left, result)
                result.append(node.val)
                _inorderRecurr(node.right, result)

        _inorderRecurr(root, result)
        return result
