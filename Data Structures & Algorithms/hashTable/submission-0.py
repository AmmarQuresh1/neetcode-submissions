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
        self.map = []
        for i in range(capacity):
            self.map.append(None)

    def insert(self, key: int, value: int) -> None:
        hashed_key = key % self.cap # mod key by capacity to get hashed key
        self.map[hashed_key] = (key, value) # insert key, value at index 
        self.size += 1
        # check for resize
        if self.size >= self.cap/2:
            self.resize()

    def get(self, key: int) -> int:
        hashed_key = key % self.cap
        slot = self.map[hashed_key]
        if slot is not None and slot[0] == key:
            return slot[1]
        return -1

    def remove(self, key: int) -> bool:
        hashed_key = key % self.cap
        slot = self.map[hashed_key]
        if slot is not None and slot[0] == key:
            self.map[hashed_key] = None
            self.size -= 1
            return True
        return False

    def getSize(self) -> int:
        return self.size        

    def getCapacity(self) -> int:
        return self.cap

    def resize(self) -> None:
        self.cap *= 2
        # new map at size capacity 
        newMap = []
        for i in range(self.cap):
            newMap.append(None)
        # save old map
        oldMap = self.map
        # set new map to current map and update by rehashing keys
        self.map = newMap
        for slot in oldMap:
            if slot is not None:
                key, value = slot
                hashed_key = key % self.cap
                self.map[hashed_key] = (key, value)
