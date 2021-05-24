from typing import List

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return None

        levels = []

        def helper(node, level):
            if not root:
                return None
            if len(level) < level:
                levels.append([node.val])
            else:
                levels[level].extend([node.val])

        helper(root, 0)

    def createTree(self, input):
        if not input:
            return None
        sentinel = None

        for i in range(len(input)):
            node = TreeNode(input[i])
            node.left = createTree(input[])


s = Solution()
s.createTree([[3, 9, 20, None, 15, 7]])
