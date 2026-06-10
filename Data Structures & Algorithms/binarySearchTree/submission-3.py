class TreeNode:
    def __init__(self, key=None, val=None, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        newNode = TreeNode(key, val)
        if not self.root:
            self.root = newNode
            return

        cur = self.root

        while cur:
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
        cur = self.root
        if not cur:
            return -1
        while cur.left:
            cur = cur.left
        return cur.val

    def getMax(self) -> int:
        cur = self.root
        if not cur:
            return -1
        while cur.right:
            cur = cur.right
        return cur.val

    def getMinNode(self, root):
        while root.left:
            root = root.left
        return root

    def removeHelper(self, root, key) -> TreeNode:
        if not root:
            return None

        if key < root.key:
            root.left = self.removeHelper(root.left, key)
        elif key > root.key:
            root.right = self.removeHelper(root.right, key)
        else:
            if not root.right:
                return root.left
            if not root.left:
                return root.right
            else:
                minNode = self.getMinNode(root.right)
                root.val = minNode.val
                root.right = self.removeHelper(root.right, minNode)
        
        return root

    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    def getInorderKeys(self) -> List[int]:
        inorder = []
        def dfs(root):
            if not root:
                return None
            
            dfs(root.left)
            inorder.append(root.key)
            dfs(root.right)
        
        dfs(self.root)
        return inorder
