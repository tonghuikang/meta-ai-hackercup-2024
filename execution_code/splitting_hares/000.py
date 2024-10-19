import sys
import sys
from collections import defaultdict

def solve():
    import sys
    import sys
    def input():
        return sys.stdin.read()

    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        W = list(map(int, data[idx:idx+N])); idx +=N
        C = list(map(int, data[idx:idx+N])); idx +=N

        color_map = defaultdict(list)
        known_weights = {}
        used_weights = set()
        missing = []
        for i in range(N):
            c = C[i]
            if W[i] != -1:
                if W[i] in used_weights:
                    # Duplicate known weight
                    color_map = None
                    break
                used_weights.add(W[i])
                known_weights[i] = W[i]
            else:
                missing.append(i)
            color_map[c].append(i)
        if color_map is None:
            print(f"Case #{test_case}: No")
            continue
        # Check that no color appears exactly once
        invalid = False
        for c, lst in color_map.items():
            if len(lst) <2:
                invalid = True
                break
        if invalid:
            print(f"Case #{test_case}: No")
            continue
        # Now, assign weights to missing
        # Strategy:
        # Assign the missing weights to colors in a way that minimizes F(c)
        # To minimize F(c), within each color, the weights should be as close as possible
        # We can sort the colors by the number of known weights
        # and try to assign missing weights adjacent to known weights
        # If no known weights in color, assign any available unique weights
        # Start by sorting all possible weights
        # Collect gaps between known weights to assign missing weights
        # For simplicity, we'll assign the smallest available weights first
        # ensuring no duplication
        # Assign weights starting from 1 to 10000, skipping used_weights
        available = set(range(1,10001)) - used_weights
        available = sorted(list(available))
        assign = {}
        success = True
        # First, sort colors by number of known weights descending
        sorted_colors = sorted(color_map.items(), key=lambda x: -len([i for i in x[1] if W[i]!=-1]))
        for c, lst in sorted_colors:
            known = sorted([W[i] for i in lst if W[i]!=-1])
            missing_in_c = [i for i in lst if W[i]==-1]
            k = len(known)
            m = len(missing_in_c)
            if k ==0:
                # Assign m missing weights
                if len(available) < m:
                    success = False
                    break
                for i in missing_in_c:
                    assign[i] = available.pop(0)
            else:
                # Assign missing weights as close as possible to known weights
                # To minimize F(c), assign missing weights between min and max of known
                min_known = known[0]
                max_known = known[-1]
                possible = []
                # Collect possible available weights between min_known and max_known
                between = [w for w in available if min_known < w < max_known]
                needed = m
                if len(between) < needed:
                    # Assign some below min_known or above max_known
                    needed_remaining = needed - len(between)
                    # Assign as close as possible to min_known and max_known
                    lower = [w for w in available if w < min_known]
                    upper = [w for w in available if w > max_known]
                    assign_between = between[:len(between)]
                    assign_lower = lower[-needed_remaining:] if needed_remaining <= len(lower) else lower
                    if len(assign_between) + len(assign_lower) < needed:
                        # Not enough weights
                        success = False
                        break
                    for i in missing_in_c:
                        if assign_between:
                            assign[i] = assign_between.pop(0)
                        else:
                            if assign_lower:
                                assign[i] = assign_lower.pop()
                            else:
                                success = False
                                break
                    # Remove assigned from available
                    for val in assign_between:
                        available.remove(val)
                    for val in assign_lower:
                        available.remove(val)
                else:
                    # Enough between min and max
                    for i in missing_in_c:
                        assign[i] = between.pop(0)
                # Now remove assigned
                for val in assign.values():
                    if val in available:
                        available.remove(val)
        if not success:
            print(f"Case #{test_case}: No")
            continue
        # Now assign the weights
        final_W = W.copy()
        for i in assign:
            final_W[i] = assign[i]
        # Check all weights are unique
        if len(set(final_W)) != N:
            print(f"Case #{test_case}: No")
            continue
        # Now, calculate sum F(c) for the given assignment
        # and check if it's minimal for some assignment.
        # However, the problem statement does not require us to verify minimality,
        # only to ensure that the given color assignment is possible with some weight assignment.
        print(f"Case #{test_case}: Yes")
        print(' '.join(map(str, final_W)))