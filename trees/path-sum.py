# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            root, cur_sum = stack.pop()
            if not root.left and not root.right:
                print(cur_sum)
                if cur_sum == targetSum:
                    return True
                else:
                    continue
            if root.left:
                stack.append((root.left, cur_sum+root.left.val))
            if root.right:
                stack.append((root.right, cur_sum+root.right.val))
        return False
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, root.val, [root.val])]
        ans = []
        while stack:
            root, cur_sum, path = stack.pop()
            if not root.left and not root.right:
                if cur_sum == targetSum:
                    ans.append(path)
                continue
            if root.left:
                stack.append((root.left, cur_sum+root.left.val, path+[root.left.val]))
            if root.right:
                stack.append((root.right, cur_sum+root.right.val, path+[root.right.val]))
        return ans