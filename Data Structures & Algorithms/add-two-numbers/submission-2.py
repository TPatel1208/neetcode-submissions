# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        curr = head
        carry = 0
        while True:

            if l1 is None:
                break
            if l2 is None:
                break
            s = l1.val + l2.val + carry
            if s > 9:
                carry = 1
                s = s%10
            else:
                carry=0
            l1 = l1.next
            l2 = l2.next
            n = ListNode(s)
            curr.next = n
            curr = n
        if l1 is not None:
            while True:
                if l1 is None:
                    break
                s = l1.val+carry
                if s > 9:
                    carry = 1
                    s = s%10
                else:
                    carry=0
                l1 = l1.next
                n = ListNode(s)
                curr.next = n
                curr = n
        if l2 is not None:
            while True:
                if l2 is None:
                    break
                s = l2.val+carry
                if s > 9:
                    carry = 1
                    s = s%10
                else:
                    carry=0
                l2 = l2.next
                n = ListNode(s)
                curr.next = n
                curr = n
               
        if carry:
            n = ListNode(1)
            curr.next = n
            curr = n
        return head.next
            
            