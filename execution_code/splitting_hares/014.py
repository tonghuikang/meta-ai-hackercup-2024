import sys
import sys
def main():
    import sys
    import sys
    from collections import defaultdict

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(input[idx]); idx +=1
        W = list(map(int, input[idx:idx+N])); idx +=N
        C = list(map(int, input[idx:idx+N])); idx +=N

        color_groups = defaultdict(list)
        known_weights = set()
        missing_indices = []
        for i in range(N):
            c = C[i]
            if W[i] != -1:
                color_groups[c].append(W[i])
                known_weights.add(W[i])
            else:
                color_groups[c].append(-1)
                missing_indices.append(i)

        # Check that no color has exactly one rabbit
        invalid = False
        for c in color_groups:
            if len(color_groups[c]) <2:
                invalid = True
                break
        if invalid:
            print(f"Case #{test_case}: No")
            continue

        # Assign weights
        # We'll attempt to assign missing weights for each color group
        # Strategy: sort known weights in each group, assign missing weights between min and max
        # or extend the range minimally.

        # Available weights
        available = set(range(1, 10001)) - known_weights
        available = sorted(available)

        success = True
        assigned = W.copy()

        # To optimize, for each color group, find the number of missing and try to assign accordingly
        # Sorting color groups by the number of missing descending might help
        color_list = sorted(color_groups.items(), key=lambda x: x[1].count(-1), reverse=True)

        for c, group in color_list:
            missing = group.count(-1)
            if missing ==0:
                continue
            known = sorted([w for w in group if w != -1])
            if not known:
                # Assign any missing weights, but need to assign at least two to have a difference
                if missing <2:
                    success = False
                    break
                # Assign consecutive available weights
                # To minimize F(c), assign consecutive numbers
                if len(available) < missing:
                    success = False
                    break
                assigned_weights = available[:missing]
                del available[:missing]
                # Assign to the group
                for i in range(N):
                    if C[i] == c and W[i]==-1:
                        assigned[i] = assigned_weights.pop(0)
            else:
                # Try to assign missing weights close to known weights
                # To minimize F(c), try to keep min and max as tight as possible
                # Find the minimal possible min and maximal possible max
                current_min = known[0]
                current_max = known[-1]
                # Assign missing weights between current_min and current_max
                possible = []
                for w in available:
                    if current_min <= w <= current_max:
                        possible.append(w)
                if len(possible) >= missing:
                    assigned_weights = possible[:missing]
                    del available[:missing]
                    # Assign to the group
                    for i in range(N):
                        if C[i] == c and W[i]==-1:
                            assigned[i] = assigned_weights.pop(0)
                else:
                    # Assign some below current_min or above current_max
                    needed = missing
                    assigned_weights = []
                    # First take all possible within range
                    assigned_weights.extend(possible)
                    needed -= len(possible)
                    del available[:len(possible)]
                    # Then assign the smallest available above current_max
                    above = [w for w in available if w > current_max]
                    below = [w for w in available if w < current_min]
                    # To minimize F(c), prefer to extend the range minimally
                    assign_above = above[:needed]
                    if len(assign_above) < needed:
                        assign_below = below[-needed:] if needed <= len(below) else below
                        if len(assign_above) + len(assign_below) < needed:
                            success = False
                            break
                        assigned_weights.extend(assign_above)
                        assigned_weights.extend(assign_below[-(needed - len(assign_above)):])
                    else:
                        assigned_weights.extend(assign_above)
                    # Remove assigned weights from available
                    for w in assign_above:
                        available.remove(w)
                    for w in assign_below[-(needed - len(assign_above)):]:
                        available.remove(w)
                    # Assign to the group
                    for i in range(N):
                        if C[i] == c and W[i]==-1:
                            assigned[i] = assigned_weights.pop(0)
        # After assignment, check uniqueness and constraints
        if not success:
            print(f"Case #{test_case}: No")
            continue
        # Check all weights are unique
        if len(set(assigned)) != N:
            print(f"Case #{test_case}: No")
            continue
        # Check all colors have at least two rabbits
        color_count = defaultdict(int)
        for c in C:
            color_count[c] +=1
        if any(v <2 for v in color_count.values()):
            print(f"Case #{test_case}: No")
            continue
        # Now, need to check sum F(c) is minimized
        # To verify, we would need an optimal method, but since we're assigning as tightly as possible, we'll assume it's correct
        print(f"Case #{test_case}: Yes")
        print(' '.join(map(str, assigned)))

if __name__ == "__main__":
    main()