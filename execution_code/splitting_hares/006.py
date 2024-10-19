import sys
import sys
import sys
from collections import defaultdict
import bisect

def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        W = list(map(int, data[idx:idx+N])); idx +=N
        C = list(map(int, data[idx:idx+N])); idx +=N
        
        # Group rabbits by color
        groups = defaultdict(list)
        for i in range(N):
            groups[C[i]].append(i)
        
        # Collect known weights
        known_weights = set()
        for w in W:
            if w != -1:
                known_weights.add(w)
        
        # Available weights
        # All numbers from 1 to 10000 not in known_weights
        # To optimize, we can keep them sorted
        available = []
        max_weight = 10000
        # To make it efficient, we can iterate once and collect all available
        # For speed, precompute once
        # Since N is small (300), and T is large, we should precompute available as needed
        # But per test case, N is small, so this should be manageable

        # To speed up, we can represent available as a list
        # from 1 to 10000, excluding known_weights
        # Since W can have up to N=300 known weights, it's feasible
        # For better performance, let's iterate and collect available
        available = []
        w_min = 1
        for w in range(1, max_weight+1):
            if w not in known_weights:
                available.append(w)
        # We'll use a list and keep it sorted

        # Assign missing weights per group
        success = True
        assigned = W.copy()
        # To keep track of assigned weights to prevent duplicates
        used = set(known_weights)
        
        # To assign missing weights, process groups
        # To minimize F(c), process groups with more constraints first
        # Groups with known weights first
        # Sort groups: those with known weights first, then those without
        groups_with_known = []
        groups_without_known = []
        for c, indices in groups.items():
            has_known = any(W[i] != -1 for i in indices)
            if has_known:
                groups_with_known.append((c, indices))
            else:
                groups_without_known.append((c, indices))
        
        # Function to assign missing weights in a group with known weights
        def assign_known_group(indices):
            nonlocal available, used, success
            known = sorted([W[i] for i in indices if W[i] != -1])
            missing = [i for i in indices if W[i] == -1]
            if not known:
                return False
            current_min = known[0]
            current_max = known[-1]
            needed = len(missing)
            # Assign as close as possible to existing weights
            # Find available weights within [current_min, current_max]
            assignable = [w for w in available if current_min <= w <= current_max]
            if len(assignable) >= needed:
                # Assign the smallest possible
                for i in range(needed):
                    w = assignable[i]
                    assigned[missing[i]] = w
                    used.add(w)
                    available.remove(w)
            else:
                # Assign all possible within [current_min, current_max]
                for w in assignable:
                    if len(missing) ==0:
                        break
                    i = len(used)  # dummy
                    # Assign to first missing
                    i = missing.pop(0)
                    assigned[i] = w
                    used.add(w)
                    available.remove(w)
                # Now, assign the rest outside
                remaining = needed - len(assignable)
                if remaining >0:
                    # Assign next available weights outside
                    # Prefer extending the range minimally
                    # Try to assign above current_max
                    extra_assign = [w for w in available if w > current_max]
                    if len(extra_assign) >= remaining:
                        for i in range(remaining):
                            w = extra_assign[i]
                            idx_missing = missing.pop(0)
                            assigned[idx_missing] = w
                            used.add(w)
                            available.remove(w)
                    else:
                        success = False
                        return
            return
        
        # Function to assign missing weights in a group without known weights
        def assign_unknown_group(indices):
            nonlocal available, used, success
            missing = indices
            needed = len(missing)
            if needed <2:
                success = False
                return
            # Assign the smallest possible consecutive weights
            # to minimize F(c)
            for start in range(len(available)-needed+1):
                # Assign available[start] to available[start+needed-1]
                candidate = available[start:start+needed]
                # Check if they are consecutive or as close as possible
                # To minimize F(c), choose the minimal range
                # So pick the first possible
                assign_weights = candidate
                # Assign them
                for i in range(needed):
                    idx = missing[i]
                    w = assign_weights[i]
                    assigned[idx] = w
                    used.add(w)
                # Remove them from available
                del available[start:start+needed]
                return
            # If not enough available
            success = False
            return
        
        # Assign groups with known weights first
        for c, indices in groups_with_known:
            assign_known_group(indices)
            if not success:
                break
        if success:
            # Assign groups without known weights
            for c, indices in groups_without_known:
                assign_unknown_group(indices)
                if not success:
                    break
        # After assignment, verify all weights are unique and within range
        if success:
            # Verify uniqueness
            final_weights = set()
            for w in assigned:
                if w <1 or w >10000:
                    success = False
                    break
                if w in final_weights:
                    success = False
                    break
                final_weights.add(w)
        if success:
            print(f"Case #{test_case}: Yes")
            print(' '.join(map(str, assigned)))
        else:
            print(f"Case #{test_case}: No")

if __name__ == "__main__":
    main()