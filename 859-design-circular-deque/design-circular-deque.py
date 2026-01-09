class Node:
    def __init__(self,val=0):
        self.value = val
        self.prev = None
        self.next = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.dummy_head = Node # dummy head node
        self.dummy_tail = Node # dummy tail node
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.capacity = k
        self.size = 0
        
    def insertFront(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        new_node = Node(value)
        first = self.dummy_head.next

        new_node.next = first
        new_node.prev = self.dummy_head
        self.dummy_head.next = new_node
        first.prev = new_node
        self.size += 1
        curr = self.dummy_head

        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.capacity:
            return False
        new_node = Node(value)
        last = self.dummy_tail.prev
        new_node.next = self.dummy_tail
        new_node.prev = last
        last.next = new_node
        self.dummy_tail.prev = new_node
        self.size += 1

        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
        first = self.dummy_head.next
        self.dummy_head.next = first.next
        first.next.prev = self.dummy_head
        self.size -= 1

        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        last = self.dummy_tail.prev
        last.prev.next = self.dummy_tail
        self.dummy_tail.prev = last.prev
        self.size -= 1

        return True

    def getFront(self) -> int:
        if self.size == 0:
            return -1
        first = self.dummy_head.next
        return first.value

    def getRear(self) -> int:
        
        if self.size == 0:
            return -1
        last = self.dummy_tail.prev
        return last.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(capacity)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()