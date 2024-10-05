import sys
import sys
import sys
from collections import defaultdict

MOD = 998244353

def main():
    import sys
    import sys
    sys.setrecursionlimit(1000000)
    input = sys.stdin.read().splitlines()
    ptr = 0
    T = int(input[ptr])
    ptr +=1
    for test_case in range(1, T+1):
        N = int(input[ptr])
        ptr +=1
        patterns = []
        for _ in range(N):
            patterns.append(input[ptr])
            ptr +=1
        # Build trie
        trie = {}
        count = 1  # root node
        for pattern in patterns:
            queue = [(trie, 0)]
            for pos, char in enumerate(pattern):
                next_queue = []
                if char == '?':
                    options = [chr(c) for c in range(ord('A'), ord('Z')+1)]
                else:
                    options = [char]
                for node, depth in queue:
                    for c in options:
                        if c not in node:
                            node[c] = {}
                            count = (count +1) % MOD
                        next_queue.append((node[c], depth+1))
                queue = next_queue
            # No need to handle end of string
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()

import sys
from collections import defaultdict

MOD = 998244353

def main():
    import sys
    import sys
    sys.setrecursionlimit(1000000)
    input = sys.stdin.read().splitlines()
    ptr = 0
    T = int(input[ptr])
    ptr +=1
    for test_case in range(1, T+1):
        N = int(input[ptr])
        ptr +=1
        patterns = []
        for _ in range(N):
            patterns.append(input[ptr])
            ptr +=1
        # Build trie
        trie = {}
        count = 1  # root node
        for pattern in patterns:
            queue = [(trie, 0)]
            for pos, char in enumerate(pattern):
                next_queue = []
                if char == '?':
                    options = [chr(c) for c in range(ord('A'), ord('Z')+1)]
                else:
                    options = [char]
                for node, depth in queue:
                    for c in options:
                        if c not in node:
                            node[c] = {}
                            count = (count +1) % MOD
                        next_queue.append((node[c], depth+1))
                queue = next_queue
            # No need to handle end of string
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()