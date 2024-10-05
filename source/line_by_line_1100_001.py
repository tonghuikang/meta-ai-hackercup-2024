import math

def solve():
    import sys
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        line = sys.stdin.readline()
        while line.strip() == '':
            line = sys.stdin.readline()
        N_str, P_str = line.strip().split()
        N = int(N_str)
        P = float(P_str)
        P_frac = P / 100.0
        # Compute Q = (P_frac)^{(N-1)/N} * 100
        if P_frac == 0.0:
            Q = 0.0
        else:
            exponent = (N - 1) / N
            Q_frac = P_frac ** exponent
            Q = Q_frac * 100.0
        increase = Q - P
        # To handle negative increases (though with P <=99 and N>=2, likely increase >=0)
        print(f"Case #{tc}: {increase:.15f}")

if __name__ == "__main__":
    solve()