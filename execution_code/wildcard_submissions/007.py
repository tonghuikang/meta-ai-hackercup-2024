import sys
import sys
import sys
from collections import defaultdict

import sys
sys.setrecursionlimit(1000000)

MOD = 998244353
ALPHABET_SIZE = 26
ALPHABET = [chr(ord('A') + i) for i in range(ALPHABET_SIZE)]

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    ptr = 0
    T = int(data[ptr])
    ptr +=1
    for test_case in range(1, T+1):
        N = int(data[ptr])
        ptr +=1
        strings = data[ptr:ptr+N]
        ptr +=N
        root = {}
        count = 1  # root node
        for s in strings:
            nodes = [root]
            for c in s:
                next_nodes = []
                if c == '?':
                    for node in nodes:
                        for letter in ALPHABET:
                            if letter not in node:
                                node[letter] = {}
                                count = (count +1) % MOD
                            next_nodes.append(node[letter])
                else:
                    for node in nodes:
                        if c not in node:
                            node[c] = {}
                            count = (count +1) % MOD
                        next_nodes.append(node[c])
                nodes = next_nodes
            # No need to mark end of word
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()