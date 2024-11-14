import sys
import sys
import sys
import sys
sys.setrecursionlimit(1000000)

MOD = 998244353

def readints():
    return list(map(int, sys.stdin.readline().split()))

class TrieNode:
    __slots__ = ['children']
    def __init__(self):
        self.children = {}

def solve():
    import sys
    from collections import deque
    T_and_rest = sys.stdin.read().splitlines()
    T = int(T_and_rest[0])
    idx = 1
    for test_case in range(1, T+1):
        N = int(T_and_rest[idx])
        idx +=1
        strings = []
        for _ in range(N):
            strings.append(T_and_rest[idx])
            idx +=1
        root = TrieNode()
        total_nodes = 1
        for s in strings:
            stack = [(root, 0)]
            while stack:
                node, pos = stack.pop()
                if pos == len(s):
                    continue
                c = s[pos]
                if c == '?':
                    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        if letter not in node.children:
                            node.children[letter] = TrieNode()
                            total_nodes = (total_nodes +1) % MOD
                        stack.append( (node.children[letter], pos+1))
                else:
                    if c not in node.children:
                        node.children[c] = TrieNode()
                        total_nodes = (total_nodes +1) % MOD
                    stack.append( (node.children[c], pos+1))
        print(f"Case #{test_case}: {total_nodes % MOD}")

import sys
import sys
import sys
import sys
sys.setrecursionlimit(1000000)

MOD = 998244353

def readints():
    return list(map(int, sys.stdin.readline().split()))

class TrieNode:
    __slots__ = ['children']
    def __init__(self):
        self.children = {}

def solve():
    import sys
    from collections import deque
    T_and_rest = sys.stdin.read().splitlines()
    T = int(T_and_rest[0])
    idx = 1
    for test_case in range(1, T+1):
        N = int(T_and_rest[idx])
        idx +=1
        strings = []
        for _ in range(N):
            strings.append(T_and_rest[idx])
            idx +=1
        root = TrieNode()
        total_nodes = 1
        for s in strings:
            stack = [(root, 0)]
            while stack:
                node, pos = stack.pop()
                if pos == len(s):
                    continue
                c = s[pos]
                if c == '?':
                    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                        if letter not in node.children:
                            node.children[letter] = TrieNode()
                            total_nodes = (total_nodes +1) % MOD
                        stack.append( (node.children[letter], pos+1))
                else:
                    if c not in node.children:
                        node.children[c] = TrieNode()
                        total_nodes = (total_nodes +1) % MOD
                    stack.append( (node.children[c], pos+1))
        print(f"Case #{test_case}: {total_nodes % MOD}")

if __name__ == "__main__":
    solve()