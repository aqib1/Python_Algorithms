from typing import Optional
from collections import deque
from bst import Node


class ConnectBst:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if not root:
            return None

        bfs = deque([root])

        while bfs:
            size = len(bfs)
            for i in range(size):
                current = bfs.popleft()
                if i != size - 1:
                    current.next = bfs[0]  # Peek at the next element in the queue

                if current.left:
                    bfs.append(current.left)

                if current.right:
                    bfs.append(current.right)

        return root