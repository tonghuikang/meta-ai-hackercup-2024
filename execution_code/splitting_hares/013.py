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
        for i in range(N):
            color_groups[C[i]].append(i)
            if W[i] != -1:
                known_weights.add(W[i])
            else:
                unknown_indices.append(i)
        
        # Check no color appears exactly once
        invalid = False
        for c in color_groups:
            if len(color_groups[c]) < 2:
                invalid = True
                break
        if invalid:
            print(f"Case #{test_case}: No")
            continue
        
        # Assign weights
        # Strategy:
        # - For each color group with known weights, assign unknowns within the min and max
        # - For color groups without known weights, assign new unique weights
        # - Ensure all weights are unique and within 1 to 10000
        # - If impossible, mark as invalid

        assigned = W.copy()
        used_weights = set(known_weights)
        possible = True
        # Collect color groups with known weights first
        groups_with_known = []
        groups_without_known = []
        for c in color_groups:
            group = color_groups[c]
            current_known = [assigned[i] for i in group if assigned[i] != -1]
            current_unknown = [i for i in group if assigned[i] == -1]
            if current_known:
                groups_with_known.append((c, group, current_known, current_unknown))
            else:
                groups_without_known.append((c, group, [], group))
        
        # Assign to groups with known weights
        for c, group, current_known, current_unknown in groups_with_known:
            if not current_known:
                continue
            min_w = min(current_known)
            max_w = max(current_known)
            # We want to assign unknowns between min_w and max_w as much as possible
            # To minimize F(c), assign closest to min and max
            available = list(range(min_w, max_w + 1))
            # Remove used weights
            available = [w for w in available if w not in used_weights]
            if len(available) < len(current_unknown):
                # Not enough weights within range, try to expand
                # Assign as close as possible to existing min and max
                # Assign below min_w or above max_w
                # First assign within range
                to_assign = []
                for w in available:
                    to_assign.append(w)
                    used_weights.add(w)
                    if len(to_assign) == len(current_unknown):
                        break
                remaining = len(current_unknown) - len(to_assign)
                if remaining > 0:
                    # Assign above max_w
                    next_w = max_w + 1
                    while remaining > 0 and next_w <= 10000:
                        if next_w not in used_weights:
                            to_assign.append(next_w)
                            used_weights.add(next_w)
                            remaining -= 1
                        next_w += 1
                if remaining > 0:
                    # Assign below min_w
                    next_w = min_w - 1
                    while remaining > 0 and next_w >= 1:
                        if next_w not in used_weights:
                            to_assign.append(next_w)
                            used_weights.add(next_w)
                            remaining -= 1
                        next_w -= 1
                if remaining > 0:
                    possible = False
                    break
                # Assign to unknowns
                for idx, w in zip(current_unknown, to_assign):
                    assigned[idx] = w
            else:
                # Assign any available weights within range
                to_assign = available[:len(current_unknown)]
                for idx, w in zip(current_unknown, to_assign):
                    assigned[idx] = w
                    used_weights.add(w)
        
        if not possible:
            print(f"Case #{test_case}: No")
            continue
        
        # Assign to groups without known weights
        # Assign unique weights, trying to minimize overall F(c)
        # For simplicity, assign consecutive available weights
        current_available = set(range(1, 10001)) - used_weights
        current_available = sorted(current_available)
        ptr = 0
        for c, group, _, current_unknown in groups_without_known:
            k = len(current_unknown)
            if ptr + k > len(current_available):
                possible = False
                break
            assigned_weights = current_available[ptr:ptr + k]
            ptr += k
            for idx, w in zip(current_unknown, assigned_weights):
                assigned[idx] = w
                used_weights.add(w)
        
        if not possible:
            print(f"Case #{test_case}: No")
            continue
        
        # Now check all constraints
        # All weights unique and within range
        if len(set(assigned)) != N:
            possible = False
        if not all(1 <= w <= 10000 for w in assigned):
            possible = False
        if not possible:
            print(f"Case #{test_case}: No")
            continue
        
        # Recalculate sum F(c) to check minimality
        # Not required as per problem, since we are to find any assignment satisfying constraints

        # All checks passed
        print(f"Case #{test_case}: Yes")
        print(' '.join(map(str, assigned)))

if __name__ == "__main__":
    main()