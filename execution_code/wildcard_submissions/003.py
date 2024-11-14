import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353

    T_and_rest = sys.stdin.read().splitlines()
    idx = 0
    T = int(T_and_rest[idx]); idx +=1

    for test_case in range(1, T+1):
        N = int(T_and_rest[idx]); idx +=1
        S = [T_and_rest[idx + i] for i in range(N)]
        idx +=N

        # Implement a trie with counting nodes
        class TrieNode:
            __slots__ = ['children']
            def __init__(self):
                self.children = {}

        root = TrieNode()
        count =1  # root is already counted

        for s in S:
            def insert(node, pos):
                nonlocal count
                if pos == len(s):
                    return
                c = s[pos]
                if c == '?':
                    for ch in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        if ch not in node.children:
                            node.children[ch] = TrieNode()
                            count = (count +1) % MOD
                        insert(node.children[ch], pos+1)
                else:
                    if c not in node.children:
                        node.children[c] = TrieNode()
                        count = (count +1) % MOD
                    insert(node.children[c], pos+1)
            insert(root, 0)
        print(f"Case #{test_case}: {count % MOD}")

threading.Thread(target=main).start()