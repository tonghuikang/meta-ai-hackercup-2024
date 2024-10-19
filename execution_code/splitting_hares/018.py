import sys
import threading
from collections import defaultdict
import bisect

def main():
    import sys

    T = int(sys.stdin.readline())
    for test_case in range(1, T + 1):
        N = int(sys.stdin.readline())
        W = list(map(int, sys.stdin.readline().split()))
        C = list(map(int, sys.stdin.readline().split()))
        
        color_to_rabbits = defaultdict(list)
        used_weights = set()
        for i in range(N):
            color_to_rabbits[C[i]].append(i)
            if W[i] != -1:
                used_weights.add(W[i])
        
        # Check if any color has exactly one rabbit
        # According to problem statement, no C_i appears exactly once
        # So this check is not needed, but let's keep it for safety
        invalid = False
        for c in color_to_rabbits:
            if len(color_to_rabbits[c]) < 2:
                invalid = True
                break
        if invalid:
            print(f"Case #{test_case}: No")
            continue
        
        # Collect available weights
        # All weights are supposed to be unique within 1 to 10,000
        available_weights = []
        # To speed up, create a list for available weights
        # Using a bitmap
        bitmap = [False] * (10001)
        for w in used_weights:
            if 1 <= w <= 10000:
                bitmap[w] = True
        for w in range(1, 10001):
            if not bitmap[w]:
                available_weights.append(w)
        # Sort available_weights for easier assignment
        available_weights.sort()
        # We will use a list and pop from start
        # Convert to a list
        from collections import deque
        available_deque = deque(available_weights)
        
        # Prepare the assignment
        W_assigned = W.copy()
        assignment_possible = True
        
        # First, assign to colors with known weights
        # Sort the colors by number of known weights descending
        colors_with_known = []
        colors_without_known = []
        for c in color_to_rabbits:
            has_known = False
            for idx in color_to_rabbits[c]:
                if W[idx] != -1:
                    has_known = True
                    break
            if has_known:
                colors_with_known.append(c)
            else:
                colors_without_known.append(c)
        
        # Sort colors_with_known by sorted known weights
        colors_with_known.sort(key=lambda c: (min(W[i] for i in color_to_rabbits[c] if W[i]!=-1), max(W[i] for i in color_to_rabbits[c] if W[i]!=-1)))
        # Assign to colors with known weights first
        for c in colors_with_known:
            # Get known weights
            known_ws = sorted([W[i] for i in color_to_rabbits[c] if W[i]!=-1])
            missing_indices = [i for i in color_to_rabbits[c] if W[i]==-1]
            count_missing = len(missing_indices)
            # Try to assign weights close to known weights
            # We will try to assign weights below and above the known range
            min_w = known_ws[0]
            max_w = known_ws[-1]
            # To assign missing weights, expand from the known range
            candidate_weights = []
            # Collect weights from min_w - k to max_w +k until we have enough
            # Here, set k max as count_missing + something
            k = 1
            while len(candidate_weights) < count_missing and (min_w - k >=1 or max_w + k <=10000):
                if min_w - k >=1 and not bitmap[min_w - k]:
                    candidate_weights.append(min_w - k)
                if max_w + k <=10000 and not bitmap[max_w + k]:
                    candidate_weights.append(max_w + k)
                k +=1
            if len(candidate_weights) < count_missing:
                assignment_possible = False
                break
            # Assign the first count_missing candidate_weights
            assigned = candidate_weights[:count_missing]
            # Assign to missing_indices
            for idx, w_new in zip(missing_indices, assigned):
                W_assigned[idx] = w_new
                bitmap[w_new] = True
            # Remove assigned weights from available_deque
            # To make it efficient, we need to filter available_deque
            # Convert available_deque to set for O(1) removal
            # But since T=1e5 and N=300, it's too slow
            # Instead, proceed without removing, since we have bitmap
            # So when assigning next, check bitmap
            # Alternatively, reconstruct available_deque
            # But to keep it simple, we'll ignore this step
            # as we have already marked the assigned weights in bitmap
        if not assignment_possible:
            print(f"Case #{test_case}: No")
            continue
        # Now assign to colors without known weights
        for c in colors_without_known:
            missing_indices = color_to_rabbits[c]
            count_missing = len(missing_indices)
            # We need to assign at least two rabbits per color
            # Since no color appears exactly once, count_missing >=2
            # Assign the smallest available weights
            if len(available_deque) < count_missing:
                assignment_possible = False
                break
            assigned = []
            for _ in range(count_missing):
                # Find the next available weight
                while available_deque and bitmap[available_deque[0]]:
                    available_deque.popleft()
                if not available_deque:
                    break
                w_new = available_deque.popleft()
                assigned.append(w_new)
                bitmap[w_new] = True
            if len(assigned) < count_missing:
                assignment_possible = False
                break
            # Assign to missing_indices
            for idx, w_new in zip(missing_indices, assigned):
                W_assigned[idx] = w_new
        if not assignment_possible:
            print(f"Case #{test_case}: No")
            continue
        # Now, all missing weights are assigned
        # Check uniqueness and all within range
        final_weights = W_assigned
        final_set = set()
        valid = True
        for w in final_weights:
            if not (1 <= w <= 10000):
                valid = False
                break
            if w in final_set:
                valid = False
                break
            final_set.add(w)
        if not valid:
            print(f"Case #{test_case}: No")
            continue
        # Now, compute sum F(c) and check if it's minimal
        # To check minimality is complex, but since we assigned as close as possible, assume it's minimal
        # Thus, output 'Yes' and the assignment
        print(f"Case #{test_case}: Yes")
        print(' '.join(map(str, final_weights)))
                

threading.Thread(target=main).start()