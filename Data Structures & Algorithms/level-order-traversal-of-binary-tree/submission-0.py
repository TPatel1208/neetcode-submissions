from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        if not root:
            return []
        queue.append([root,0])
        results = []
        level = 0
        while queue:
            l = []
            while queue:
                node = queue[0][0]
                curr = queue[0][1]
                if curr == level and node:
                    l.append(node.val)
                    queue.popleft()
                    if node.left:
                        queue.append([node.left,level+1])
                    if node.right:
                        queue.append([node.right,level+1])
                else:
                    break
            results.append(l)
            level+=1
        
        return results
                    
