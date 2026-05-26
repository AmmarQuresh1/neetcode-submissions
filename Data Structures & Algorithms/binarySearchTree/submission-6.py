class TreeNode:
    def __init__(self, key: int = 0, val: int = 0, left = None, right=None):
        self.left = left
        self.right = right
        self.key = key
        self.val = val

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode
            return
        
        cur = self.root
        while True:
            if key < cur.key:
                if not cur.left:
                    cur.left = newNode
                    return
                cur = cur.left
            elif key > cur.key:
                if not cur.right:
                    cur.right = newNode
                    return 
                cur = cur.right
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
        if not self.root:
            return -1 

        cur = self.root

        while cur.left:
            cur = cur.left
        
        return cur.val

    def getMax(self) -> int:
        if not self.root:
            return -1 

        cur = self.root

        while cur.right:
            cur = cur.right
        
        return cur.val

    def findMin(self, node):
        while node and node.left:
            node = node.left
        return node

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)
    
    def removeHelper(self, cur, key):
        if not cur:
            return None
        
        if key > cur.key:
            cur.right = self.removeHelper(cur.right, key)
        elif key < cur.key:
            cur.left = self.removeHelper(cur.left, key)
        else:
            if not cur.left:
                return cur.right
            elif not cur.right:
                return cur.left
            else:
                minNode = self.findMin(cur.right)
                cur.key = minNode.key
                cur.val = minNode.val
                cur.right = self.removeHelper(cur.right, minNode.key)
        return cur


    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, root, result):
        if root:
            self.inorderTraversal(root.left, result)
            result.append(root.key)
            self.inorderTraversal(root.right, result)
