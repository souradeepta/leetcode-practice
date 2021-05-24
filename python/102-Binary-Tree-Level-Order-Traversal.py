from typing import List
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []

        if not root:
            return levels

        def helper(node, level):
            if not node:
                return

            if level > len(levels):
                levels.append([node.val])
            else:
                levels[level-1].extend([node.val])

            helper(node.left, level+1)
            helper(node.right, level+1)

        helper(root, 1)

        return levels
