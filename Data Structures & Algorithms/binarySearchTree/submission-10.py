class TreeMap:
    class _Node:
        def __init__(self, key, val, left=None, right=None):
            self.key = key
            self.val = val
            self.left = left
            self.right = right

    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = self._Node(key, val)
        if not self.root:
            self.root = newNode
            return
        
        cur = self.root
        while cur:
            if key < cur.key:
                if cur.left: 
                    cur = cur.left
                else:
                    cur.left = newNode
                    return
            elif key > cur.key:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = newNode
                    return
            else:
                cur.val = val
                return
            

    def get(self, key: int) -> int:
        cur = self.root
        while cur:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val
        
        return -1

    def getMin(self) -> int:
        cur = self.root
        while cur and cur.left:
            cur = cur.left
        
        return cur.val if cur.val is not None else -1

    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right:
            cur = cur.right
        
        return cur.val if cur.val is not None else -1

    def getMinNode(self, cur):
        while cur and cur.left:
            cur = cur.left
        
        return cur 

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def removeHelper(self, cur, key):
        if cur is None:
            return None 

        if key < cur.key:
            cur.left = self.removeHelper(cur.left, key)
        elif key > cur.key:
            cur.right = self.removeHelper(cur.right, key)
        else:
            if cur.right is None:
                return cur.left
            elif cur.left is None:
                return cur.right
            else:
                minNode = self.getMinNode(cur.right)
                cur.key, cur.val = minNode.key, minNode.val
                cur.right = self.removeHelper(cur.right, minNode.key)
        return cur

    def getInorderKeys(self) -> List[int]:
        res = []
        def _dfs(root):
            if not root: return
            _dfs(root.left)
            res.append(root.key)
            _dfs(root.right)

        _dfs(self.root)
        return res
