# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        #make base cases


        #what if both are Null: return true
        if not p and not q:
            return True

        #what if one is Null but other is not: return False

        if not p or not q:
            return False

        if p.val != q.val: #3what if their values are different
            return False

        return  self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

      

        







        
        