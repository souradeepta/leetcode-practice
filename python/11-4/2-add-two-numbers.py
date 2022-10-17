l1 = [2,4,3]
l2 = [5,6,4]
output = [7,0,8]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and l2:
            return None
        if not l1 and l2:
            return l2
        if l1 and not l2:
            return l1

    sentinel = ListNode(-1)
    head = l1
    carry = 0
    while l1 or l2:
        
