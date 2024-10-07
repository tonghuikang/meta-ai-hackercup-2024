import sys
import sys
import sys
import sys
sys.setrecursionlimit(10000)

MOD = 998244353

def main():
    import sys
    import sys
    from collections import defaultdict

    input = sys.stdin.read().splitlines()
    ptr = 0
    T = int(input[ptr]); ptr +=1

    for test_case in range(1, T+1):
        N = int(input[ptr]); ptr +=1
        patterns = []
        for _ in range(N):
            patterns.append(input[ptr]); ptr +=1
        # Build trie
        # Each node will be a dict mapping character to node id
        # We use a list of dicts to represent nodes
        trie = [{}]
        for pattern in patterns:
            # recursive insert with wildcards
            def insert(node_id, pos):
                if pos == len(pattern):
                    return
                char = pattern[pos]
                if char == '?':
                    options = [chr(ord('A') + i) for i in range(26)]
                else:
                    options = [char]
                for c in options:
                    if c not in trie[node_id]:
                        trie[node_id][c] = len(trie)
                        trie.append({})
                    insert(trie[node_id][c], pos+1)
            insert(0, 0)
        total_nodes = len(trie) % MOD
        print(f"Case #{test_case}: {total_nodes}")

if __name__ == "__main__":
    main()