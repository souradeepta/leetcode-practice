# 144. Binary Tree Preorder Traversal
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        def _preorderTraversalRecursive(node, result):
            if node:
                result.append(node.val)
                _preorderTraversalRecursive(node.left, result)
                _preorderTraversalRecursive(node.right, result)

        _preorderTraversalRecursive(root, result)
        return result

    def preorderTraversalIterative(self, root: TreeNode) -> List[int]:
        result = []
        if not root:
            return result

        stack = [root, ]

        while stack:
            node = stack.pop()
            if root:
                result.append(root.val)
                if root.right:
                    stack.append(root.right)
                if root.left:
                    stack.append(root.left)

        return result