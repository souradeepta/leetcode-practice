# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        serialized = []

        def preorder(node):
            if not node:
                return None
            else:
                serialized.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return serialized

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def preorder(node):
            value = next(data)
            if not data:
                return None

            node = TreeNode(value)
            node.left = preorder()
            node.right = preorder()
            return node

        return preorder()


# Your Codec object will be instantiated and called as such:
ser = Codec()
deser = Codec()
root = [1, 2, 3, None, None, 4, 5]
ans = deser.deserialize(ser.serialize(root))
