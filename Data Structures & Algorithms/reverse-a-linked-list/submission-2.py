# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        #[ none  < 0 < 1 < 2 > 3]
        #.      .  n.     .     cur next
        #                prev

        prev = None
        cur = head


        while cur:
            nxt = cur.next #nxt is 1
            cur.next = prev
            prev = cur
            cur = nxt
            







        return prev