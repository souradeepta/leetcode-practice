#   Binary Tree Level Order Traversal
# Complexity:: Time:O(n), Space:O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        def helper(self, node, level):
            # start the current level
            if len(levels) == level:
                levels.append([])

            # append the current node value
            levels[level].append(node.val)

            # process child nodes for the next level
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)

            helper(root, 0 )
            return levels

    
    def levelOrder2(self, root: TreeNode) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        
        level = 0        
        queue = collections.deque([root, ])

        while queue:
            # start the current level
            levels.append([])

            #number of elements in the current level
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()

                #fulfill the current level
                levels[level].append(node.val)

                #add child nodes of the current level
                # in the queue for the next level

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            #go to next level
            level = level + 1
        return levels

