from collections import deque
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        if not root:
          return []
        answer = []
        stack = [(root,0)]
        while stack:
          node, level = stack.pop()
          if level >= len(answer):
            answer.append(deque())
          if level & 1: #odd?
            answer[level].appendleft(node.val)
          else:
            answer[level].append(node.val)
          for child in [node.right, node.left]:
            if not child:
              continue
            else:
              stack.append([child,level+1])
        return answer 

grid = [3,9,20,0,0,15,7]
sol = Solution()
print(sol.zigzagLevelOrder(grid))