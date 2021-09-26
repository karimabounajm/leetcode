# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def RecursiveisValidBST(self, root: TreeNode) -> bool:
        def recursive_search(node: TreeNode, maxi, mini):
            if not node:
                return True
            if node.val >= maxi or node.val <= mini:
                return False
            return recursive_search(node.left, node.val, mini) and recursive_search(node.right, maxi, node.val)
        return recursive_search(root, math.inf, -math.inf)
    # depth first implementation of the previous solution, uses a stack instead of a queue, 
    # and does not have a recursive component to it
    def DFSisValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, lower, upper = stack.pop()
            if not root:
                continue
            val = root.val
            if val <= lower or val >= upper:
                return False
            stack.append((root.right, val, upper))
            stack.append((root.left, lower, val))
        return True
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(node: TreeNode, curr_sum) -> None:
            nonlocal count
            if not node:
                return 
            curr_sum += node.val
            if curr_sum == k:
                count += 1
            count += h[curr_sum - k]
            hdic[curr_sum] += 1
            preorder(node.right, curr_sum)
            preorder(node.left, curr_sum)
            hdic[curr_sum] -= 1
            
        count, k = 0, sum
        hdic = defaultdict(int)
        preorder(root, 0)
        return count