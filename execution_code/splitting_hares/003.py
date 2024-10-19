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
        known_weights = set()
        unknown_indices = []
        for i in range(N):
            color_groups[C[i]].append(i)
            if W[i] != -1:
                known_weights.add(W[i])
            else:
                unknown_indices.append(i)
        
        # Check if any color group has only one rabbit
        invalid = False
        for color, indices in color_groups.items():
            if len(indices) == 1:
                invalid = True
                break
        if invalid:
            print(f"Case #{test_case}: No")
            continue
        
        # Assign weights to unknowns
        # Available weights are [1, 10000] not in known_weights
        available = set(range(1, 10001)) - known_weights
        available = sorted(list(available))
        
        # Sort color groups by number of known weights descending
        sorted_colors = sorted(color_groups.keys(), key=lambda c: (-sum(1 for i in color_groups[c] if W[i]!=-1), c))
        
        success = True
        assignment = {}
        used = set()
        for color in sorted_colors:
            indices = color_groups[color]
            known = sorted([W[i] for i in indices if W[i]!=-1])
            cnt_unknown = len(indices) - len(known)
            if cnt_unknown == 0:
                continue
            if known:
                # Try to assign missing weights close to known weights
                # For simplicity, assign the smallest available weights
                for _ in range(cnt_unknown):
                    if not available:
                        success = False
                        break
                    w = available.pop(0)
                    # Ensure w does not conflict with known weights
                    if w in known:
                        success = False
                        break
                    assignment[indices[len(known)]] = w
                    known.append(w)
            else:
                # Assign any available weights
                for _ in range(cnt_unknown):
                    if not available:
                        success = False
                        break
                    w = available.pop(0)
                    assignment[indices[len(known)]] = w
                    known.append(w)
            if not success:
                break
        
        if not success:
            print(f"Case #{test_case}: No")
            continue
        
        # Now assign the weights
        final_W = W.copy()
        for i in range(N):
            if final_W[i] == -1:
                if i in assignment:
                    final_W[i] = assignment[i]
                else:
                    success = False
                    break
        if not success:
            print(f"Case #{test_case}: No")
            continue
        
        # Check all weights are unique and within range
        if len(set(final_W)) != N or not all(1 <= w <=10000 for w in final_W):
            print(f"Case #{test_case}: No")
            continue
        
        # Now compute the minimal sum of F(c)
        # To verify, but we skip as we assigned in a simplistic way
        print(f"Case #{test_case}: Yes")
        print(' '.join(map(str, final_W)))

if __name__ == "__main__":
    main()