# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None

        #curr is at head

        #curr.next is at the value .next

        #[none, 0, 1,2,3]
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt





        return prev