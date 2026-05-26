class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    # Size of a hashmap is the keys 
    # capacity is the number of indexes 
    # when size = capacity/2, capacity is doubled, keys are rehashed
    # this is checked after every insert
    # In the case of collisions here just overwrite
    # when key is inserted it is hashed then modded by the capacity of the hasmap and inserted at the relevant index

    def __init__(self, capacity: int):
        self.size = 0
        self.cap = capacity
        self.map = [None] * capacity

    # mod key by capacity to get hashed key
    def hash_function(self, key):
        return key % self.cap

    def insert(self, key: int, value: int) -> None:
        index = self.hash_function(key)
        head = self.map[index]
        # if head is falsy then this runs as not(falsy) = true
        if not head:
            self.map[index] = Node(key, value) # insert key, value at index 
        else:
            prev = None
            while head:
                if head.key == key:
                    head.value = value
                    return 
                prev, head = head, head.next
            prev.next = Node(key, value)
        self.size += 1
        # check for resize
        if self.size * 2 >= self.cap:
            self.resize()

    def get(self, key: int) -> int:
        index = self.hash_function(key)
        node = self.map[index]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> bool:
        index = self.hash_function(key)
        dummy = Node(None, None)
        node = self.map[index]
        dummy.next = node
        prev = dummy
        while node:
            if node.key == key:
                prev.next = node.next
                self.size -= 1
                self.map[index] = dummy.next
                return True
            prev, node = node, node.next
        return False

    def getSize(self) -> int:
        return self.size        

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        self.cap *= 2
        # new map at size capacity 
        newMap = [None] * self.cap
        # save old map # set new map to current map and update by rehashing keys
        oldMap, self.map = self.map, newMap
        for node in oldMap:
            while node:
                index = self.hash_function(node.key)
                if not self.map[index]:
                    self.map[index] = Node(node.key, node.value)
                else:
                    new_node = self.map[index]
                    while new_node.next:
                        new_node = new_node.next
                    new_node.next = Node(node.key, node.value)
                node = node.next
