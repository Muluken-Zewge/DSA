class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.freq = 1
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.size = 0

    def add_to_tail(self, node):
        prev = self.tail.prev
        
        prev.next = node
        node.prev = prev
        
        node.next = self.tail
        self.tail.prev = node
        
        self.size += 1

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        
        prev.next = nxt
        nxt.prev = prev
        
        self.size -= 1

    def pop_head(self):
        if self.size == 0:
            return None
        
        node = self.head.next
        self.remove(node)
        return node

    def is_empty(self):
        return self.size == 0


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.minFreq = 0
        
        self.key_to_node = {}
        self.freq_to_list = defaultdict(DoublyLinkedList)


    def update_freq(self, node):
        freq = node.freq
        self.freq_to_list[freq].remove(node)

        if freq == self.minFreq and self.freq_to_list[freq].is_empty():
            self.minFreq += 1

        node.freq += 1
        self.freq_to_list[node.freq].add_to_tail(node)


    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]
        self.update_freq(node)
        
        return node.val


    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value
            self.update_freq(node)
            return
        
        if len(self.key_to_node) == self.capacity:
            lfu_list = self.freq_to_list[self.minFreq]
            node_to_remove = lfu_list.pop_head()
            
            del self.key_to_node[node_to_remove.key]

        new_node = Node(key, value)
        self.key_to_node[key] = new_node
        
        self.freq_to_list[1].add_to_tail(new_node)
        self.minFreq = 1