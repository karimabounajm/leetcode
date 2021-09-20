"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
      # default dict is used because it auotmatically generates
      # a new element whenever a key is not found; the lambda
      # below essentially has the default dict create a new 
      # node whenever a key that does not exist is accessed, noting
      # that keys are themselves nodes, pointers and unique
      dic = collections.defaultdict(lambda: Node(0))
      dic[None] = None
      cur_point = head
      while cur_point:
          dic[cur_point].val = cur_point.val
          dic[cur_point].next = dic[cur_point.next]
          dic[cur_point].random = dic[cur_point.random]
          cur_point = cur_point.next
      return dic[head]
    def copyRandomList(self, head):
      # initializing a hash table in python, with keys being nodes
      # of the original linked list and their correpsonding elements
      # being nodes of the new linked list
      dic = dict()
      # initializing two pointers to the head of the old linked
      m = n = head
      # creating all of the nodes of the new linked list, with their 
      # values initialized however their pointers left void
      while m:
        dic[m] = RandomListNode(m.label)
        m = m.next
      # setting up the next and random pointers of nodes in new linked
      # list, which can now be done as the nodes are already created
      while n:
        # note, get is used because the the key is a node of the original
        # list, so getting n.next with n being of the original list gets
        # the copy of the next value within the dictionary
        dic[n].next = dic.get(n.next)
        dic[n].random = dic.get(n.random)
        n = n.next
      # returning the pointer that the old head points to, which is the
      # new head of the new linked list 
      return dic.get(head)

nums = [0,2,1,1,1,1,3]
# nums = [0, 4, 2, 1, 5]
sol = Solution()
print(sol.firstMissingPositive(nums))
print(nums)