import sys
import threading

def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353
    for test_case in range(1, T+1):
        N = int(sys.stdin.readline())
        patterns = [sys.stdin.readline().strip() for _ in range(N)]
        trie = [ [-1]*26 ]
        node_count =1
        for S in patterns:
            stack = [ (0, 0) ]
            while stack:
                node, pos = stack.pop()
                if pos == len(S):
                    continue
                c = S[pos]
                if c == '?':
                    for ch in range(26):
                        if trie[node][ch] == -1:
                            trie[node][ch] = node_count
                            trie.append( [-1]*26 )
                            node_count +=1
                        child = trie[node][ch]
                        stack.append( (child, pos+1) )
                else:
                    ch = ord(c) - ord('A')
                    if trie[node][ch] == -1:
                        trie[node][ch] = node_count
                        trie.append( [-1]*26 )
                        node_count +=1
                    child = trie[node][ch]
                    stack.append( (child, pos+1) )
        print(f"Case #{test_case}: {node_count % MOD}")

threading.Thread(target=main,).start()