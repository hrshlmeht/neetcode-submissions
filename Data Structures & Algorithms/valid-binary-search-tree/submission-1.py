# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root: Optional[TreeNode], minimum: float, maximum: float) -> bool:
            if not root:
                return True

            if not (minimum < root.val and maximum > root.val):
                return False
             
            #check left if there invalid left value
            left = dfs(root.left, minimum, root.val)
            #check right if there invalid right value
            right = dfs(root.right, root.val, maximum)


            return left and right

        return dfs(root, float("-inf"), float("inf"))
        