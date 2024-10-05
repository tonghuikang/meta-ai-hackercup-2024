import sys
import sys
import sys
def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353
    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        strings = [sys.stdin.readline().strip() for _ in range(N)]
        node_list = [ [-1] * 26 ]
        node_count = 1
        for S in strings:
            current_nodes = [0]
            for ch in S:
                if ch == '?':
                    letters = list(range(26))
                else:
                    letters = [ord(ch) - ord('A')]
                next_nodes = []
                for node in current_nodes:
                    for l in letters:
                        child = node_list[node][l]
                        if child == -1:
                            node_list.append([ -1 ] * 26)
                            node_list[node][l] = node_count
                            child = node_count
                            node_count +=1
                        next_nodes.append(child)
                # Remove duplicates by converting to set and back to list
                current_nodes = list(set(next_nodes))
        print(f"Case #{test_case}: {node_count % MOD}")

if __name__ == "__main__":
    main()