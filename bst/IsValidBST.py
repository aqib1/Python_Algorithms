import sys
from typing import Optional
from bst.TreeNode import TreeNode


class IsValidBst:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def solve(root, low, high) -> bool:
            if root is None:
                return True
            if low >= root.val or high <= root.val:
                return False

            return solve(root.left, low, root.val) and solve(root.right, root.val, high)

        return solve(root, float('-inf'), float('inf'))