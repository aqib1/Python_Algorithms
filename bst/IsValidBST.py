from typing import Optional
from bst.TreeNode import TreeNode


class IsValidBst:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.is_valid_bst_recur(root, float("-inf"), float("inf"))

    def is_valid_bst_recur(self, root: TreeNode, low: float, high: float) -> bool:
        if not root:
            return True

        if low >= root.val or high <= root.val:
            return False

        return self.is_valid_bst_recur(
            root.left, low, root.val
        ) and self.is_valid_bst_recur(root.right, root.val, high)