# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #none [0,1,2,3]
        #^      ^ ^nextnode
        curr = head
        prev = None

        while curr:

            #make curr point to none
            #then we move prev up to curr
            #move curr to the nect

            nextnode = curr.next
            curr.next = prev
            prev = curr
            curr = nextnode



        return prev



