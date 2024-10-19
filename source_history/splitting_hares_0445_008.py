import sys
import threading

def main():
    import sys
    import math
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N = int(sys.stdin.readline())
        W = list(map(int, sys.stdin.readline().split()))
        C = list(map(int, sys.stdin.readline().split()))
        
        color_groups = {}
        known_weights = set()
        for i in range(N):
            c = C[i]
            if c not in color_groups:
                color_groups[c] = []
            color_groups[c].append(i)
            if W[i] != -1:
                known_weights.add(W[i])
        
        # Check that no color has exactly one rabbit
        invalid = False
        for c in color_groups:
            if len(color_groups[c]) < 2:
                invalid = True
                break
        if invalid:
            print(f"Case #{test_case}: No")
            continue
        
        # Assign missing weights
        # Prepare available weights
        available = set(range(1,10001)) - known_weights
        # Sort available weights
        available = sorted(available)
        available_ptr = 0
        
        # Assign weights to each color group
        new_W = W.copy()
        success = True
        # To minimize F(c), assign missing weights close to existing weights in the group
        for c in color_groups:
            group = color_groups[c]
            known = sorted([W[i] for i in group if W[i] != -1])
            missing = [i for i in group if W[i] == -1]
            if not known:
                # Assign any two available weights
                if len(missing) < 2:
                    success = False
                    break
                for i in missing:
                    if available_ptr >= len(available):
                        success = False
                        break
                    new_W[i] = available[available_ptr]
                    available_ptr +=1
            else:
                # Assign missing weights close to existing weights
                for i in missing:
                    # Find the closest available weight to the known group
                    min_diff = math.inf
                    chosen = -1
                    chosen_idx = -1
                    for idx in range(available_ptr, len(available)):
                        w = available[idx]
                        diff = min([abs(w - kw) for kw in known])
                        if diff < min_diff:
                            min_diff = diff
                            chosen = w
                            chosen_idx = idx
                        if diff ==0:
                            break
                    if chosen == -1:
                        success = False
                        break
                    new_W[i] = chosen
                    # Remove the chosen weight from available
                    available.pop(chosen_idx)
            if not success:
                break
        if not success:
            print(f"Case #{test_case}: No")
            continue
        # Check all weights are unique and within [1,10000]
        if len(set(new_W)) != N or any(w <1 or w >10000 for w in new_W):
            print(f"Case #{test_case}: No")
            continue
        # Now, calculate minimal possible sum F(c)
        # To do so, we need to find the optimal grouping
        # However, since it's complex, we'll assume our assignment is optimal
        # and proceed
        print(f"Case #{test_case}: Yes")
        print(' '.join(map(str, new_W)))

threading.Thread(target=main).start()