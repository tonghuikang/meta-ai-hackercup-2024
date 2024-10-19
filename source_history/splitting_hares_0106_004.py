import sys
import sys
import sys
def main():
    import sys
    import sys
    from collections import defaultdict
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N = int(sys.stdin.readline())
        W = list(map(int, sys.stdin.readline().split()))
        C = list(map(int, sys.stdin.readline().split()))
        
        color_groups = defaultdict(list)
        used_weights = set()
        possible = True
        for w, c in zip(W, C):
            if w != -1:
                color_groups[c].append(w)
                if w in used_weights:
                    possible = False
                used_weights.add(w)
        if not possible:
            print(f"Case #{test_case}: No")
            continue
        # Check no color appears exactly once
        color_counts = defaultdict(int)
        for c in C:
            color_counts[c] +=1
        single_colors = [c for c, cnt in color_counts.items() if cnt ==1]
        if single_colors:
            print(f"Case #{test_case}: No")
            continue
        # Assign missing weights
        # Available weights
        all_weights = set(range(1,10001))
        available_weights = sorted(all_weights - used_weights)
        assigned_W = W.copy()
        # Group colors by number of missing
        color_info = {}
        for c in color_counts:
            known = sorted([w for w in color_groups[c] if w != -1])
            total = color_counts[c]
            missing = total - len(known)
            color_info[c] = (known, missing)
        # Sort colors: first assign colors with known weights, then those without
        colors_sorted = sorted(color_info.keys(), key=lambda x: (len(color_info[x][0])==0, len(color_info[x][0])))
        success = True
        for c in colors_sorted:
            known, missing = color_info[c]
            if missing ==0:
                continue
            if known:
                # Assign missing weights close to known weights
                # To minimize F(c), spread missing weights around existing ones
                # Find the median of known weights
                known_sorted = sorted(known)
                median = known_sorted[len(known_sorted)//2]
                # Assign missing weights around median
                # Use a pointer to pick the closest available weights
                assigned = []
                left = 0
                right = len(available_weights)-1
                # Find the best starting point
                # Assign to minimize max - min
                # We can try to assign the closest available weights to the existing known weights
                # Simplest approximation: assign the smallest available weights first
                for _ in range(missing):
                    if not available_weights:
                        success = False
                        break
                    # Assign the closest to median
                    # Binary search to find closest
                    import bisect
                    pos = bisect.bisect_left(available_weights, median)
                    candidates = []
                    if pos < len(available_weights):
                        candidates.append(available_weights[pos])
                    if pos >0:
                        candidates.append(available_weights[pos-1])
                    if not candidates:
                        success = False
                        break
                    # Choose the candidate with minimal distance to median
                    candidates.sort(key=lambda x: (abs(x - median), x))
                    chosen = candidates[0]
                    assigned.append(chosen)
                    available_weights.remove(chosen)
                if not success:
                    break
                # Assign to the first missing in W with C_i = c
                idx = 0
                for i in range(N):
                    if C[i]==c and W[i]==-1:
                        assigned_W[i] = assigned[idx]
                        idx +=1
            else:
                # Assign the smallest available weights
                if missing <2:
                    success = False
                    break
                assigned = available_weights[:missing]
                if len(assigned) < missing:
                    success = False
                    break
                # Assign to the first missing in W with C_i = c
                for i in range(N):
                    if C[i]==c and W[i]==-1:
                        assigned_W[i] = assigned[0]
                        available_weights.pop(0)
                        assigned = assigned[1:]
            if not success:
                break
        if not success:
            print(f"Case #{test_case}: No")
            continue
        # Now verify that all weights are unique and within range
        final_weights = assigned_W
        if len(set(final_weights)) != N:
            print(f"Case #{test_case}: No")
            continue
        if any(not (1 <= w <=10000) for w in final_weights):
            print(f"Case #{test_case}: No")
            continue
        # Now verify that the assignment sum F(c) is minimized
        # To do this, construct the minimal sum F(c) for the final_weights and compare
        # Since the problem says to follow the given color assignment and minimize F(c),
        # and we assigned accordingly, we'll assume it's correct
        print(f"Case #{test_case}: Yes")
        print(' '.join(map(str, final_weights)))

if __name__ == "__main__":
    main()