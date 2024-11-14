import sys
import sys
import sys
import sys
sys.setrecursionlimit(1000000)

def main():
    import sys
    from collections import defaultdict
    T = int(sys.stdin.readline())
    MOD = 998244353
    for test_case in range(1, T+1):
        N = int(sys.stdin.readline())
        strings = [sys.stdin.readline().strip() for _ in range(N)]
        # Build the trie
        trie = {}
        count = 1  # Start with root
        for s in strings:
            stack = [(trie, 0)]
            stack = [(trie, 0, s)]
            # Implement iterative insertion with wildcards
            nodes = [(trie, 0)]
            while nodes:
                current_node, pos = nodes.pop()
                if pos == len(s):
                    continue
                c = s[pos]
                if c == '?':
                    options = [chr(ord('A') + i) for i in range(26)]
                else:
                    options = [c]
                for ch in options:
                    if ch not in current_node:
                        current_node[ch] = {}
                        count = (count +1) % MOD
                    nodes.append((current_node[ch], pos+1))
        print(f"Case #{test_case}: {count % MOD}")

if __name__ == "__main__":
    main()