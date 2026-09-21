# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')

        def dfs(root: TreeNode) -> int:
            nonlocal max_sum

            if not root:
                return float('-inf')

            left_side_sum = dfs(root.left)
            right_side_sum = dfs(root.right)

            max_sum = max(
                max_sum,
                # Tree sums
                root.val,
                root.val + left_side_sum,
                root.val + right_side_sum,
                root.val + left_side_sum + right_side_sum
            )

            return max(
                root.val,
                root.val + left_side_sum,
                root.val + right_side_sum
            )
        
        dfs(root)

        return max_sum
        