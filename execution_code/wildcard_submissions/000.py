import sys
import threading

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    MOD = 998244353
    T_and_rest = sys.stdin.read().split('\n')
    idx = 0
    T = int(T_and_rest[idx])
    idx +=1
    for test_case in range(1, T+1):
        if idx >= len(T_and_rest):
            N = 0
            strings = []
        else:
            N_line = T_and_rest[idx]
            while N_line.strip() == '':
                idx +=1
                N_line = T_and_rest[idx]
            N = int(N_line)
            idx +=1
            strings = []
            for _ in range(N):
                if idx >= len(T_and_rest):
                    s = ''
                else:
                    s = T_and_rest[idx].strip()
                    idx +=1
                strings.append(s)
        # Initialize trie
        trie = [-1]  # root node has index 0
        children = [[]]  # list of lists, each sublist will have 26 elements
        children[0] = [-1]*26
        node_count =1
        stack = []
        for S in strings:
            stack = [(0,0)]
            # Use a stack to perform DFS
            while stack:
                node, pos = stack.pop()
                if pos == len(S):
                    continue
                c_set = []
                c_char = S[pos]
                if c_char == '?':
                    c_set = range(26)
                else:
                    c_set = [ord(c_char) - ord('A')]
                for c in c_set:
                    if children[node][c] == -1:
                        children[node][c] = node_count
                        children.append([-1]*26)
                        node_count +=1
                    stack.append( (children[node][c], pos +1) )
        print(f"Case #{test_case}: {node_count % MOD}")

threading.Thread(target=main).start()