T = int(input())
for case_num in range(1, T + 1):
    N = int(input())
    S_list = [input() for _ in range(N)]

    # Build the pattern trie
    class Node:
        def __init__(self):
            self.children = {}
            self.indices = []  # List of tuples (S_i_index, position in S_i)
            self.dp = None  # Memoization for the total number of nodes

    root = Node()
    for idx, S in enumerate(S_list):
        node = root
        node.indices.append((idx, 0))  # (string index, position)
        for pos in range(len(S)):
            c = S[pos]
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
            node.indices.append((idx, pos + 1))  # Next position in S_i

    MOD = 998244353

    from sys import setrecursionlimit
    setrecursionlimit(1 << 25)

    def dfs(node):
        if node.dp is not None:
            return node.dp
        total = 1  # For the current node
        letters = set()
        # Collect possible letters at this node
        for idx, pos in node.indices:
            S = S_list[idx]
            if pos == len(S):
                continue  # End of S_i
            c = S[pos]
            if c == '?':
                letters.update(chr(ord('A') + i) for i in range(26))
            else:
                letters.add(c)
        # For each possible letter, proceed to child node
        for c in letters:
            if c in node.children:
                child = node.children[c]
            else:
                # Create new child node
                child = Node()
                node.children[c] = child
                # Update indices for the new child node
                for idx, pos in node.indices:
                    S = S_list[idx]
                    if pos == len(S):
                        continue
                    if S[pos] == c or S[pos] == '?':
                        child.indices.append((idx, pos + 1))
            total = (total + dfs(node.children[c])) % MOD
        node.dp = total
        return total

    result = dfs(root)
    print(f"Case #{case_num}: {result}")