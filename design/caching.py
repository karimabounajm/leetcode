class DLinkedNode(): 
    def __init__(self, key=0, value=0):
        # intitializing a node with constructor
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
            
class LRUCache():
    def _add_node(self, node):
        # new nodes are added right after the head
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        # passing node by reference and removing its link
        # to its previous and next node, severing from ll
        prev = node.prev
        new = node.next
        # setting the next of the previous to next and prev
        # of next to prev, linking the two nodes, disconnect
        prev.next = new
        new.prev = prev

    def _push_up_node(self, node):
        # removing node from current position and putting it 
        # right next to the head, where a new node would go
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        # finding the tail node by going to the prev of the 
        # tail pointer/object
        res = self.tail.prev
        self._remove_node(res)
        return res

    def __init__(self, capacity):
        # initializing cache with dictionary, which will contain nodes
        self.cache = {}
        # varaibles to measure size and capacity, to keep it from overflowing
        self.size = 0
        self.capacity = capacity
        # initializing head and tail pointer nodes
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        # linking the head and the tail nodes
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        # getting the node through the get method, using the key
        node = self.cache.get(key, None)
        # adding mechanism
        if not node:
            return -1

        # move the accessed node to the head, cache functionality
        self._push_up_node(node)
        return node.value

    def put(self, key, value):
        # getting the node through the get method, using the key
        node = self.cache.get(key)
        # if the node is not in the cache, add it
        if not node: 
            newNode = DLinkedNode(key, value)
            # adding it to the dictionary cache and the linked list
            self.cache[key] = newNode
            self._add_node(newNode)
            # incrementing size, and checking to make room if necessary
            self.size += 1
            if self.size > self.capacity:
                # popping the tail if cache is full, removing oldest
                # piece of memory in the cache;
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            # if the key is associated with an existing node update the 
            # value of that node, and move it to the head
            node.value = value
            self._push_up_node(node)