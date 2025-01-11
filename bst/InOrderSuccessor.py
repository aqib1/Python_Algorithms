from typing import Optional
from bst.TreeNode import TreeNode


class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        return self.successor(root, p, None)

    # time complexity OLog(n) or O(h)
    # space complexity OLog(n) or O(h)
    def successor(self, node: TreeNode, p: TreeNode, successor: Optional[TreeNode]) -> Optional[TreeNode]:
        if not node:
            return successor
        if p.val >= node.val:
            return self.successor(node.right, p, successor)
        return self.successor(node.left, p, node)

