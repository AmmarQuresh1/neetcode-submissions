class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = {}

class PrefixTree:

    def __init__(self):
        self.root = Node("")

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.next:
                cur.next[c] = Node(c)
            cur = cur.next[c]
        cur.next['\0'] = Node('\0')

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.next:
                return False
            cur = cur.next[c]
        
        if '\0' in cur.next:
            return True
        
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.next:
                return False
            cur = cur.next[c]
        
        return True
        