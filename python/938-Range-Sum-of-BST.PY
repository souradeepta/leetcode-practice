# 938. Range Sum of BST


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        # empty tree
        if not root:
            return None
        
        # BFS
        queue =collections.deque()
        queue.append(root)
        sum = 0
        while queue:
            node = queue.popleft()
            # optimize for BST property
            if( L <= node.val <= R):
                sum+= node.val
                print(node.val)
            
            if(node.right is not None and node.val <=R):
                queue.append(node.right)
            
            if(node.left is not None and node.val >=L):
                queue.append(node.left)
                
        return sum
