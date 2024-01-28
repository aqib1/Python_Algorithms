from bst.TreeNode import TreeNode
from typing import Optional
from typing import List

class LevelOrder:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        data = [[]]
        self.preorder(root, data, 0)
        return data


    def preorder(self, root: Optional[TreeNode], data: List[List[int]], height: int):
        if not root:
            return
        if len(data) == height:
            data.append([])

        data[height].append(root.val)

        self.preorder(root.left, data, height + 1)
        self.preorder(root.right, data, height + 1)