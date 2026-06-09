# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        head = ListNode()
        curr = head



        #empty node (head here)

       #                  v  l1
        #list 1 =   [1,2,4]


        #               l2 
        #list 2 =  [1,3,5]


        #[1,1,2,3,4,5]        
        while list1 and list2: #while both still have nodes

            if list1.val < list2.val: #current will point to the smaller value
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            
            curr = curr.next
        
        curr.next = list1 or list2

        return head.next

