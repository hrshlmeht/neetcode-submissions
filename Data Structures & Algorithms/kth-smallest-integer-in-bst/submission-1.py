# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self, root:Optional[TreeNode], k:int)->None:
        if root is None:
            return
        
        self.dfs(root.left, k)

        self.node_counter += 1
        
        if self.node_counter == k:
            self.k_node_found = True
            self.answer = root.val
            return

        if self.k_node_found:
            return
        
        self.dfs(root.right, k)
        
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.node_counter = 0
        self.answer = -1
        self.k_node_found = False
        
        self.dfs(root, k)

        return self.answer