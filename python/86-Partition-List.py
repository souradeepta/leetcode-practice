# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l1 = []
        l2 = []
        curr = head
        while curr:
            if curr.val <= x:
                l1.append(curr.val)
            else:
                l2.append(curr.val)
            curr = curr.next

        dummy = ListNode(-1)
        new_head = dummy
        for i in range(len(l1)):
            node = ListNode(l1[i])
            new_head.next = node
            new_head = new_head.next

        for i in range(len(l2)):
            node = ListNode(l2[i])
            new_head.next = node
            new_head = new_head.next

        return dummy.next
