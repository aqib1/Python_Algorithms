from bst.TreeNode import TreeNode
from typing import Optional, List


class PostOrderTraversal:

    ## Time complexity O(n)
    ## Space complexity O(n)
    def postorder(self, root: Optional[TreeNode]) -> List[int]:
        data = []
        self.prepare(root, data)
        return data

    def prepare(self, root: Optional[TreeNode], data: List[int]):
        if not root:
            return

        self.prepare(root.left, data)
        self.prepare(root.right, data)

        data.append(root.val)
