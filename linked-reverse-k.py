
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
# common algorithm/loop for reversing a linked list in place,
# with a for loop reversing n nodes if it is done in 
next_node = ptr.next
ptr.next = new_head
new_head = ptr
ptr = next_node

class Solution:
    # helper function for reversing a subset of the linked list, with
    # it reversing k nodes in the given linked list starting at the 
    # pointer to the current position in the linked list recursively
    def reverseLinkedList(self, head, k):
        # initializing the new header node, which will obviously change
        # given that the linked list is being reversed, so the head of 
        # this subsection of the list will be what was the kth of the 
        # subset passed by reference
        new_head, ptr = None, head
        # reversing k nodes within the linked list
        for i in range(k):
            # saving the next node in the linked list
            next_node = ptr.next
            # setting the next node of the current head to the
            # head of the linked list reversed so far
            ptr.next = new_head
            # setting the head of the current linked list, which 
            # has had its next replaced by the head of the previous 
            # reversed linked list so far, as the new head of the 
            # linked list
            new_head = ptr
            # setting the pointer to the new head of the remaining 
            # previous linked list, which was saved in the beginning of
            # the iteration from the next node of the previous head
            ptr = next_node
        # returning the new head, which is formed ultimately by setting
        # its next constantly to a reversed linked list of iteratively
        # increasing length that is reversed
        return new_head
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # initializing the head value by the pointer to the node in
        # the linked list the process is currently reversing
        count, ptr = 0, head
        # counting the number of nodes left in the linked list given
        # the current position
        for i in range(k):
            if not ptr:
                break
            ptr = ptr.next
            count += 1            
        # checking if there are k nodes left, if not then there is no 
        # need to reverse that subsection of the linked list
        if count == k: 
            # the reversed head is the new head
            reversedHead = self.reverseLinkedList(head, k)
            # the old head is the new tail of the sub list
            head.next = self.reverseKGroup(ptr, k)
            # returning the new head of the sub list created by this
            # recursive call of reverseKGroup, which will allow for 
            # the linking the the tail of the previous calling
            return reversedHead
        # modifying head as it is passed by reference, the head that
        # is returned at the end of every recursive calling will 
        # essentially chain the entire reversing of the linked list
        return head
    ''' new method, not part of the question '''
    # note, if wanted to also reverse the last version sub list of 
    # the original list, even if it is not of length k, then we 
    # could simply change the reverseKGroup code to this
    def reverseAllK(self, head:ListNode, k:int) -> ListNode:
        # checking if the head is None, which would mean that all
        # of the substrings have been reversed
        if not head:
            return head
        # initializing head value and count, which will be pointer
        # to the head of the current sub list and how long it is, 
        # so that the helper reversing function can know how much 
        count, ptr = 0, head
        # checking the length of the sub list that we will reverse
        # which is min(length of remining list, k)
        for i in range(k):
            if not ptr:
                break
            ptr = ptr.next
            count += 1
        # creating a pointer to the new head, which is the tail 
        # of the sub list that is about to be reversed
        new_head = self.reverseLinkedList(head, count)
        # setting the head of the current call of this recursive
        # function as the next of the next calling of the function
        # which will return the head of the next, reversed, sublist
        head.next = self.reverseAllK(ptr, k)
        return new_head