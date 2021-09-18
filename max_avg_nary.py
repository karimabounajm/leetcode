class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Solution:
    def maxAverage(self, root):
        if not root or not root.children:
            return None

        # self.res = [max average, tree node of the max average]
        self.res = [float('-inf'), root)]
        self.dfs(root)

        return self.res[1]

    def dfs(self, root):
        # if this is a leaf node, return its value and 1, which indicates
        # that is has no children, so only one node is returned/counted
        if not root.children:
            return [root.val, 1]
        # setting the value to the value of the node, and count to 1
        cur_val, cur_count = root.val, 1
        # finding the sum values and count of the children recurisively,
        # and then adding the values to values and total count
        for node in root.children:
            child_val, child_count = self.dfs(node)
            cur_val += child_val
            cur_count += child_count
        # finding the average by dividing the sum total of the values of 
        # the children of the root node by its total count
        cur_average = cur_val / float(cur_count)
        # updating the current best average and the node at which it is
        # calculated if a new best is achieved
        if cur_average > self.res[0]:
            self.res = [cur_average, root]
        # returning the sum values of the root node and all its childre,
        # as well as count, to continue to recursive nature of function
        return [cur_val, cur_count]

