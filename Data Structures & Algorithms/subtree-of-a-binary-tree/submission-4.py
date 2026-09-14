# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val==q.val and check(p.left,q.left) and check(p.right,q.right)
        def search(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if p.val==q.val and check(p,q):
                return True
            else:
                return search(p.left,q) or search(p.right,q)
        if not subRoot:
            return True
        return search(root, subRoot)