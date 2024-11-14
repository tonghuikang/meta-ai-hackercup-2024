import sys

def main():
    import sys
    import math

    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N_line = ''
        while N_line.strip() == '':
            N_line = sys.stdin.readline()
        N = int(N_line)
        max_v_min = 0.0
        v_max_candidates = []
        impossible = False
        for i in range(1, N+1):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            A_i, B_i = map(int, line.strip().split())
            if B_i == 0:
                # B_i is zero, delivery time must be zero, which implies v = inf unless i=0
                if i !=0:
                    impossible = True
                    continue
            # v >= i / B_i
            if B_i == 0:
                # If B_i is 0, only possible if i ==0
                if i !=0:
                    impossible = True
            else:
                v_min = i / B_i
                if v_min > max_v_min:
                    max_v_min = v_min
            if A_i > 0:
                v_max = i / A_i
                v_max_candidates.append(v_max)
        if impossible:
            print(f"Case #{test_case}: -1")
            continue
        if v_max_candidates:
            min_v_max = min(v_max_candidates)
            if max_v_min > min_v_max + 1e-12:
                print(f"Case #{test_case}: -1")
                continue
        # Now, need to ensure that max_v_min <= min_v_max (if any)
        # The minimal speed that satisfies all is max_v_min
        print(f"Case #{test_case}: {max_v_min if not v_max_candidates or max_v_min <= min(v_max_candidates) else -1}")
        
if __name__ == "__main__":
    main()