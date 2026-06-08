class Node:
    def __init__(self, val, is_end=False):
        self.val = val
        self.next = {}
        self.is_end = is_end

class WordDictionary:

    def __init__(self):
        self.prefix_root = Node("")

    def addWord(self, word: str) -> None:
        i = 0
        cur = self.prefix_root
        while i < (len(word)):
            if word[i] not in cur.next:
                cur.next[word[i]] = Node(word[i])
            cur = cur.next[word[i]]
            i += 1
        cur.is_end = True 

    def search(self, word: str) -> bool:
        def dfs(cur_prefix, word):
            if len(word) == 0:
                return cur_prefix.is_end

            if word[0] == '.':
                for child in cur_prefix.next.values():
                    if dfs(child, word[1:]):
                        return True

            if word[0] in cur_prefix.next:
                return dfs(cur_prefix.next[word[0]], word[1:])
        
            return False

        cur_prefix = self.prefix_root
        return dfs(cur_prefix, word)
