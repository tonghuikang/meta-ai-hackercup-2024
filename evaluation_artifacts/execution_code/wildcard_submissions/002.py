import sys
import sys
import sys

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read().splitlines()
    T = int(input[0])
    MOD = 998244353
    ptr = 1
    output = []
    for test_case in range(1, T + 1):
        N = int(input[ptr])
        ptr += 1
        strings = input[ptr:ptr+N]
        ptr += N
        # Initialize trie
        children = [[-1] * 26]
        node_count = 1
        for s in strings:
            current_nodes = [0]
            for c in s:
                if c == '?':
                    possible = range(26)
                else:
                    possible = [ord(c) - ord('A')]
                next_nodes = []
                for node in current_nodes:
                    for ch in possible:
                        if children[node][ch] == -1:
                            children[node][ch] = node_count
                            children.append([-1] * 26)
                            node_count += 1
                        next_nodes.append(children[node][ch])
                current_nodes = next_nodes
        output.append(f"Case #{test_case}: {node_count % MOD}")
    print('\n'.join(output))

if __name__ == "__main__":
    main()