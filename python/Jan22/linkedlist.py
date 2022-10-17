class Node():
    def __init__(self, value, next=None):
        self.val = value
        self.next = next

class LinkedList():
    def __init__(self, input: list):
        self.head = head

    def createlist(self, input:list):
        sentinel = Node(-1, None)
        for ele in list:
            sentinel = Node(ele, sentinel)