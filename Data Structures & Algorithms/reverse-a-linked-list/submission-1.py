# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = head
        if head is not None:
            second = head.next
            if second is None:
                return head
        else:
            return None
        head.next = None
        while second != None:
            prev = second
            second = second.next
            prev.next = first
            first = prev
        
        return prev