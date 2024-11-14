import sys
import sys
import sys
from sys import stdin
import sys
import sys

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353
    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx])
    idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx])
        idx +=1
        patterns = data[idx:idx+N]
        idx +=N
        # Initialize trie
        nodes = [[-1]*26]
        node_count = 1
        stack = []
        for pattern in patterns:
            stack = [(0, 0)]
            while stack:
                node, pos = stack.pop()
                if pos == len(pattern):
                    continue
                c = pattern[pos]
                if c == '?':
                    for ci in range(26):
                        if nodes[node][ci] == -1:
                            nodes[node][ci] = node_count
                            nodes.append([-1]*26)
                            node_count +=1
                        stack.append((nodes[node][ci], pos +1))
                else:
                    ci = ord(c) - ord('A')
                    if nodes[node][ci] == -1:
                        nodes[node][ci] = node_count
                        nodes.append([-1]*26)
                        node_count +=1
                    stack.append((nodes[node][ci], pos +1))
        print(f"Case #{test_case}: {node_count % MOD}")

if __name__ == "__main__":
    main()