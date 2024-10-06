import sys
import threading

def main():
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    MOD = 998244353
    for case_num in range(1, T + 1):
        N = int(sys.stdin.readline())
        S = [sys.stdin.readline().strip() for _ in range(N)]
        max_len = max(len(s) for s in S)
        N_s = len(S)
        memo = {}
        trie_size = 0

        from collections import defaultdict

        def dfs(pos_list):
            nonlocal trie_size
            state_key = tuple(pos_list)
            if state_key in memo:
                return
            memo[state_key] = True
            trie_size += 1

            # Determine possible letters at current positions
            possible_letters = set()
            for i in range(N_s):
                if pos_list[i] < len(S[i]):
                    c = S[i][pos_list[i]]
                    if c == '?':
                        possible_letters.update(chr(ord('A') + k) for k in range(26))
                    else:
                        possible_letters.add(c)

            # For each possible letter, advance positions and recurse
            for c in possible_letters:
                next_pos_list = []
                valid = False
                for i in range(N_s):
                    if pos_list[i] < len(S[i]):
                        s_char = S[i][pos_list[i]]
                        if s_char == '?' or s_char == c:
                            next_pos_list.append(pos_list[i] + 1)
                            valid = True
                        else:
                            next_pos_list.append(pos_list[i])
                    else:
                        next_pos_list.append(pos_list[i])
                if valid:
                    dfs(tuple(next_pos_list))

        # Initialize positions
        initial_pos_list = tuple([0] * N_s)
        dfs(initial_pos_list)

        print(f'Case #{case_num}: {trie_size % MOD}')

if __name__ == '__main__':
    threading.Thread(target=main).start()