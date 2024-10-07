import sys

def main():
    import sys

    MOD = 998244353
    LETTERS = [chr(i) for i in range(65, 91)]  # 'A' to 'Z'

    data = sys.stdin.read().splitlines()
    T = int(data[0])
    ptr = 1
    for test_case in range(1, T +1):
        N = int(data[ptr])
        ptr +=1
        strings = data[ptr: ptr + N]
        ptr += N

        # Initialize trie
        trie = [ [None]*26 ]  # root node at index 0
        node_count =1

        for s in strings:
            current_nodes = [0]
            for c in s:
                if c == '?':
                    possible_indices = list(range(26))
                else:
                    possible_indices = [ord(c) - 65]
                next_nodes = []
                for node_id in current_nodes:
                    for idx in possible_indices:
                        if trie[node_id][idx] is None:
                            trie[node_id][idx] = node_count
                            trie.append( [None]*26 )
                            node_count +=1
                        next_nodes.append(trie[node_id][idx])
                current_nodes = next_nodes
        print(f"Case #{test_case}: {node_count % MOD}")

if __name__ == "__main__":
    main()