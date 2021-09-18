

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        # using breadth first search
        q, max_width = [], 0
        q.append((root,0))
        while q:
            # finding the new max width, with the difference in 
            # the indices of the rightmost and leftmost values in
            # the queue, or the most recent and the first inserted, 
            # forming the width of the current level, as the queue
            # itself contains all the nodes of a level
            max_width = max(max_width,q[-1][1]-q[0][1]+1)
            # finding the length to itereate over, so that all the 
            # child nodes of the nodes in the current level, which 
            # are stored in the array, are appended to the queue
            length = len(q)
            for i in range(length):
                # extracting the pointer to the current node and its 
                # position from the queue, as is stored
                (current,pos) = q.pop(0)
                # appendin the left and right children nodes, if they
                # exist, into the queue, while also calculating their 
                # indices using formula that the index of a child node 
                # is double the index of its parent node (+1 for right)
                if current.left:
                    q.append((current.left,2*pos))
                if current.right:
                    q.append((current.right,2*pos+1))
        return max_width