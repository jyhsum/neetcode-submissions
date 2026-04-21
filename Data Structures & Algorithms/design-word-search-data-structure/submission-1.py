class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True
        
    def search(self, word: str) -> bool:  # BFS
        nodes = [self.root]
        for c in word:
            next_nodes = []
            for node in nodes:
                if c == '.':
                    next_nodes += node.children.values()
                elif c in node.children:
                    next_nodes.append(node.children[c])
                
            if not next_nodes:
                return False
            nodes = next_nodes
        return any(n.word for n in nodes)

