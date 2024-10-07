import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    MOD = 998244353

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        patterns = [sys.stdin.readline().strip() for _ in range(N)]
        
        # Trie node represented as a dict: {char: node}
        # To optimize, use list of size 26 for children
        # Each node will have a list of 26 elements, initialized to -1
        # and a list to store nodes
        nodes = []
        children = []
        nodes.append(0)  # root node
        children.append([-1] * 26)
        node_count = 1

        for pattern in patterns:
            stack = [(0, 0)]  # (current node index, position in pattern)
            memo = {}
            while stack:
                current_node, pos = stack.pop()
                if pos == len(pattern):
                    continue
                key = (current_node, pos)
                if key in memo:
                    continue
                memo[key] = True
                char = pattern[pos]
                if char == '?':
                    for c in range(26):
                        if children[current_node][c] == -1:
                            children[current_node][c] = node_count
                            children.append([-1] * 26)
                            node_count += 1
                        stack.append((children[current_node][c], pos + 1))
                else:
                    c = ord(char) - ord('A')
                    if children[current_node][c] == -1:
                        children[current_node][c] = node_count
                        children.append([-1] * 26)
                        node_count += 1
                    stack.append((children[current_node][c], pos + 1))
        print(f"Case #{test_case}: {node_count % MOD}")

if __name__ == "__main__":
    threading.Thread(target=main).start()