from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # We can do a full level view but only ever store the right-most node
        # per level.
        # We need to traverse the full tree because we cannot know in advance whether
        # there are still nodes further to the right on a given level.

        # We do BFS on the tree.
        # We store in a queue the next node to be traversed and its level, where root is
        # at level 0, its children at level 1 and so on.
        # Since we add the left child before the right child, nodes on the same level
        # are processed from left to right.
        # We store one value per level and overwrite it whenever we encounter another
        # node on the same level. The last value stored is therefore the right-most node.

        if not root:
            return []

        queue = deque()
        queue.append((0, root))
        res = []

        while queue:
            level, node = queue.popleft()

            if len(res) <= level:
                res.append(node.val)
            else:
                res[level] = node.val

            if node.left:
                queue.append((level + 1, node.left))
            if node.right:
                queue.append((level + 1, node.right))

        return res