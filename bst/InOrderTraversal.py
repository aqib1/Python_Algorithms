from bst.TreeNode import TreeNode
from typing import Optional, List


class InOrderTraversal:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        data = []
        self.inorder_insert(root, data)
        return data

    def inorder_insert(self, root, data):
        if not root:
            return
        self.inorder_insert(root.left, data)
        data.append(root.val)
        self.inorder_insert(root.right, data)
