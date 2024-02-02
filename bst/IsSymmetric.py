from typing import Optional
from bst.TreeNode import TreeNode

class Solution:
    ## Time complexity O(N) & Space O(N)
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSymmetricRecur(root, root)

    def isSymmetricRecur(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        if not left and not right:
            return True
        if not left or not right:
            return False

        return (left.val == right.val
                and self.isSymmetricRecur(left.left, right.right)
                and self.isSymmetricRecur(left.right, right.left))
