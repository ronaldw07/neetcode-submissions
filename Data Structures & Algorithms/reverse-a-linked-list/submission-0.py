# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        cur = head
        prev = None



        #[none, 0, 1,2,3]
        #prev cur t
        while cur: #while cur not null
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
        
        return prev