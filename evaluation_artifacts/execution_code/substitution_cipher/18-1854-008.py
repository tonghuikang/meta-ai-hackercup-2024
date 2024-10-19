import sys

def main():
    import sys
    import threading

    def solve():
        import sys

        sys.setrecursionlimit(1 << 25)
        T = int(sys.stdin.readline())
        MOD = 998244353
        for test_case in range(1, T +1):
            line = sys.stdin.readline()
            if not line:
                line = sys.stdin.readline()
            E_K = line.strip().split()
            E = E_K[0]
            K = int(E_K[1])
            n = len(E)
            s = list(E)
            suff_question = [0]*(n +1)
            for i in range(n-1, -1, -1):
                suff_question[i] = suff_question[i+1] + (1 if s[i] == '?' else 0)
            # Precompute pow2 up to suff_question[i]
            # Since K <=1,000,000, 2^20=1,048,576 >=1e6
            max_pow = 1000001
            pow2 = [1]*(n+1)
            for i in range(1, n+1):
                if pow2[i-1] < max_pow:
                    pow2[i] = pow2[i-1]*2
                    if pow2[i] > max_pow:
                        pow2[i] = max_pow
                else:
                    pow2[i] = max_pow
            # Assign '2' or '1' to '?'
            res = s.copy()
            for i in range(n):
                if s[i] == '?':
                    rem = suff_question[i+1]
                    current_pow = pow2[rem]
                    if current_pow >= K:
                        res[i] = '2'
                    else:
                        res[i] = '1'
                        K -= current_pow
            # Now, compute f[n]
            f_prev_prev =1
            if res[0] != '0':
                f_prev =1
            else:
                f_prev =0
            for i in range(1, n):
                f_curr =0
                if res[i] != '0':
                    f_curr += f_prev
                two_digit = res[i-1] + res[i]
                if '10' <= two_digit <= '26':
                    f_curr += f_prev_prev
                f_curr %= MOD
                f_prev_prev, f_prev = f_prev, f_curr
            f_n = f_prev
            res_str = ''.join(res)
            print(f"Case #{test_case}: {res_str} {f_n}")
    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()

import sys

def main():
    import sys
    import threading

    def solve():
        import sys

        sys.setrecursionlimit(1 << 25)
        T = int(sys.stdin.readline())
        MOD = 998244353
        for test_case in range(1, T +1):
            line = sys.stdin.readline()
            if not line:
                line = sys.stdin.readline()
            E_K = line.strip().split()
            E = E_K[0]
            K = int(E_K[1])
            n = len(E)
            s = list(E)
            suff_question = [0]*(n +1)
            for i in range(n-1, -1, -1):
                suff_question[i] = suff_question[i+1] + (1 if s[i] == '?' else 0)
            # Precompute pow2 up to suff_question[i]
            # Since K <=1,000,000, 2^20=1,048,576 >=1e6
            max_pow = 1000001
            pow2 = [1]*(n+1)
            for i in range(1, n+1):
                if pow2[i-1] < max_pow:
                    pow2[i] = pow2[i-1]*2
                    if pow2[i] > max_pow:
                        pow2[i] = max_pow
                else:
                    pow2[i] = max_pow
            # Assign '2' or '1' to '?'
            res = s.copy()
            for i in range(n):
                if s[i] == '?':
                    rem = suff_question[i+1]
                    current_pow = pow2[rem]
                    if current_pow >= K:
                        res[i] = '2'
                    else:
                        res[i] = '1'
                        K -= current_pow
            # Now, compute f[n]
            f_prev_prev =1
            if res[0] != '0':
                f_prev =1
            else:
                f_prev =0
            for i in range(1, n):
                f_curr =0
                if res[i] != '0':
                    f_curr += f_prev
                two_digit = res[i-1] + res[i]
                if '10' <= two_digit <= '26':
                    f_curr += f_prev_prev
                f_curr %= MOD
                f_prev_prev, f_prev = f_prev, f_curr
            f_n = f_prev
            res_str = ''.join(res)
            print(f"Case #{test_case}: {res_str} {f_n}")
    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()