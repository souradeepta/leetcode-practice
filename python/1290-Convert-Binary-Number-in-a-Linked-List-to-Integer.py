# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        decimal = 0
        digits = []
        curr = head
        while curr:
            digits.append(curr.val)
            curr = curr.next

        msb = len(digits) - 1
        for digit in digits:
            decimal += digit*2**msb
            msb -= 1
        print(decimal)
        return decimal


s = Solution()

a = ListNode(1)
b = ListNode(0)
c = ListNode(1)
a.next = b
b.next = c

assert 5 == s.getDecimalValue(a), "incorrect output"
