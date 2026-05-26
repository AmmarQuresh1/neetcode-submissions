class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k
        for n in nums:
            self.push(n)
            if len(self.heap) - 1 > self.k:
                self.pop()

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]:
            tmp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = tmp
            i = i // 2
        
    def pop(self):
        if len(self.heap) == 1:
            return None
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]
        self.heap[1] = self.heap.pop()
        i = 1
        while i * 2 < len(self.heap):
            # if the right exists, is smaller than left and cur > right child
            if (i * 2 + 1 < len(self.heap) and
            self.heap[i * 2 + 1] < self.heap[i * 2] and
            self.heap[i] > self.heap[i * 2 + 1]):
                tmp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = tmp
                i = i * 2 + 1
            # we know left exists from while condition
            # swap if left is min 
            elif self.heap[i] > self.heap[i * 2]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[i*2]
                self.heap[i*2] = tmp
                i = i * 2
            else:
                break
        
        return res

    def add(self, val: int) -> int:
        self.push(val)
        if len(self.heap) - 1 > self.k:
            self.pop()
        return self.heap[1]
