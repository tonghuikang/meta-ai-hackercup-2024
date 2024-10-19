import sys
import sys
def main():
    import sys
    import sys
    from collections import defaultdict

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        W = list(map(int, sys.stdin.readline().split()))
        C = list(map(int, sys.stdin.readline().split()))
        
        color_groups = defaultdict(list)
        known_weights = set()
        unknown_indices = []
        for idx in range(N):
            color = C[idx]
            weight = W[idx]
            if weight != -1:
                color_groups[color].append(weight)
                known_weights.add(weight)
            else:
                color_groups[color].append(-1)
                unknown_indices.append(idx)
        
        # Check if any color has only one rabbit
        invalid = False
        for color, weights in color_groups.items():
            if len(weights) == 1:
                invalid = True
                break
        if invalid:
            print(f"Case #{test_case}: No")
            continue
        
        # Available weights
        available = set(range(1, 10001)) - known_weights
        available = sorted(available)
        
        # Assign weights to unknowns
        # Strategy: for each color with missing weights, assign the smallest available weights
        # to make the group as tight as possible
        assignment = {}
        possible = True
        # Sort colors by number of unknowns descending
        colors_sorted = sorted(color_groups.keys(), key=lambda c: color_groups[c].count(-1), reverse=True)
        for color in colors_sorted:
            group = color_groups[color]
            missing = [i for i, w in enumerate(group) if w == -1]
            if not missing:
                continue
            if len(available) < len(missing):
                possible = False
                break
            # Assign the smallest available weights
            for idx in missing:
                W_idx = unknown_indices.pop(0)
                W[W_idx] = available.pop(0)
        
        # After assignment, check all weights are unique and within range
        assigned_weights = set()
        for w in W:
            if w < 1 or w > 10000 or w in assigned_weights:
                possible = False
                break
            assigned_weights.add(w)
        
        if possible:
            print(f"Case #{test_case}: Yes")
            print(' '.join(map(str, W)))
        else:
            print(f"Case #{test_case}: No")

if __name__ == "__main__":
    main()