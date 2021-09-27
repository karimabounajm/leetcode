# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # nested helper function for going through a linked
        # list and adding all its nodes to the array of vals
        def iterate_list(cur_node: ListNode):
            while cur_node:
                vals.append(cur_node)
                cur_node = cur_node.next
        # checking the base case of the values
        if not lists:
            return None
        # creating an array to hold the node objects
        vals = []
        # add all nodes into an array, sort the array 
        # by the val, and from link nodes sequentially
        for i in range(len(lists)):
            iterate_list(lists[i])
        if not vals:
            return None
        # sorting the vals array
        vals.sort(key=lambda x: x.val)
        # going through the array connecting nodes
        for i in range(len(vals)-1):
            vals[i].next = vals[i+1]
        return vals[0]