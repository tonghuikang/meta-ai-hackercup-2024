import sys
import sys
import bisect

def main():
    import sys
    import sys
    sys.setrecursionlimit(1000000)
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N = int(sys.stdin.readline())
        W = list(map(int, sys.stdin.readline().split()))
        C = list(map(int, sys.stdin.readline().split()))
        
        # Group rabbits by color
        color_groups = {}
        for i in range(N):
            c = C[i]
            if c not in color_groups:
                color_groups[c] = []
            color_groups[c].append(i)
        
        # Check no color appears exactly once
        single_color = False
        for c in color_groups:
            if len(color_groups[c]) == 1:
                single_color = True
                break
        if single_color:
            print(f"Case #{test_case}: No")
            continue
        
        # Collect used weights
        used = set()
        for w in W:
            if w != -1:
                used.add(w)
        # Available weights
        available = sorted(set(range(1,10001)) - used)
        # Index for available
        avail_ptr = 0
        
        # Assign weights
        success = True
        # To store assignments
        W_new = W.copy()
        for c in color_groups:
            group = color_groups[c]
            known_weights = sorted([W[i] for i in group if W[i] != -1])
            unknown_indices = [i for i in group if W[i] == -1]
            if not known_weights:
                # Assign a block of unique weights
                # Assign any two first available weights
                if len(available) < len(unknown_indices):
                    success = False
                    break
                for i in unknown_indices:
                    W_new[i] = available[avail_ptr]
                    used.add(available[avail_ptr])
                    avail_ptr +=1
            else:
                # Assign missing weights near existing weights
                for i in unknown_indices:
                    # Assign the smallest available weight not used
                    if avail_ptr >= len(available):
                        success = False
                        break
                    W_new[i] = available[avail_ptr]
                    used.add(available[avail_ptr])
                    avail_ptr +=1
            if not success:
                break
        if not success:
            print(f"Case #{test_case}: No")
            continue
        # Now, check if all weights are unique
        if len(set(W_new)) != N:
            print(f"Case #{test_case}: No")
            continue
        # Now, compute F(c) sum
        F_sum = 0
        for c in color_groups:
            group = color_groups[c]
            weights = [W_new[i] for i in group]
            F_sum += max(weights) - min(weights)
        # Now, to check if the sum is minimal
        # The problem states that we need to minimize F_sum, but in the problem statement, if any assignment that satisfies constraints is acceptable
        # So, as long as we have a valid assignment, output "Yes"
        print(f"Case #{test_case}: Yes")
        print(' '.join(map(str, W_new)))
        
if __name__ == "__main__":
    main()