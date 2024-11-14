import sys

import threading
def main():
    T = int(sys.stdin.readline())
    for case_num in range(1, T+1):
        N = int(sys.stdin.readline())
        low = 0.0
        high = float('inf')
        for i in range(1, N+1):
            Ai_str, Bi_str = sys.stdin.readline().split()
            Ai = int(Ai_str)
            Bi = int(Bi_str)
            Ai_div_i = Ai / i
            Bi_div_i = Bi / i
            if Ai_div_i > Bi_div_i:
                # This interval is invalid; no need to proceed further.
                low = 1.0
                high = 0.0
                break
            low = max(low, Ai_div_i)
            high = min(high, Bi_div_i)
        if low > high or high <= 0.0:
            print(f"Case #{case_num}: -1")
        else:
            v = 1.0 / high
            # Ensure we have enough precision
            print(f"Case #{case_num}: {v:.10f}")
threading.Thread(target=main).start()