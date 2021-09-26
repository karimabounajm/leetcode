# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# strategy: level order traversal, with the maintaining of heights 
# being used as a manner of deciding when to reverse subsets of the
# array of values returned; create an object that contains the value
# of each node, and its height; after creating an array through level
# order traversal, modify that array by reversing all of its sublists 
# that contain elements with an even height. note, this can't be messed
# up by having consecutive layers that should be reversed being reversed
# together because there has to be at least one node connecting two 
# layers that are a level apart

from typing import List
from collections import deque



class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base case, check if the root exists
        if root is None:
            return
        # create a deque to store nodes and allow for O(1) popping of  
        # left side of the linked list array
        queue, ans = deque([root]), []
        level = 1
        # running a level order traversal, using a queue with O(1) popping
        while queue:
            # finding the current length of the queue, which represents all
            # of the nodes in the current level, and create an array to 
            # store their values
            level_vals, length = [], len(queue)
            # iterating through the queue and dequeuing the number of nodes 
            # that were determined to be part of the current level by the
            # length of the queue recorded at the beginning of the iteration
            for _ in range(length):
                node = queue.popleft()
                level_vals.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if level % 2 == 0:
                ans.append(level_vals[::-1])
            else:
                ans.append(level_vals)
            level += 1
        return ans
    def origZigzag(self, root: Optional[TreeNode]) -> List[List[int]]:
        # base case, check if the root exists
        if root is None:
            return
        # create a deque to store nodes and allow for O(1) popping of  
        # left side of the linked list array
        queue = deque([[root, 1]])
        ans, buf = [], []
        cur_level = 1
        # running a level order traversal
        while queue:
            # dequeue a node and its level, add the value of the node and 
            # its level to the answer array
            node, level = queue.popleft()
            if level <= cur_level:
                buf.append(node.val)
            else:
                # updating the current height
                cur_level = level
                # adding the values of the current level into the answer 
                if level % 2 == 1:
                    # add in reverse if the current level is odd, which 
                    # means that the values in buf are of an even level
                    ans.append(buf[::-1])
                else:
                    ans.append(buf)
                # resetting the buffer with elements from the new level
                buf = [node.val]
            # print(ans)
            # enqueuing the children with incremented level to the parents
            if node.left is not None:
                queue.append([node.left, level + 1])
            if node.right is not None:
                queue.append([node.right, level + 1])
        if buf:
            if cur_level % 2 == 0:
                ans.append(buf[::-1])
            else:
                ans.append(buf)
        return ans