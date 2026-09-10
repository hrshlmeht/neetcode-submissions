class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            # returns (height, diameter)
            if not node:
                return 0, 0
            lh, ld = dfs(node.left)
            rh, rd = dfs(node.right)
            height = 1 + max(lh, rh)
            diameter = max(ld, rd, lh + rh)
            return height, diameter

        return dfs(root)[1]