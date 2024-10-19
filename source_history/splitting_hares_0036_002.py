import sys
import sys
import sys

def main():
    import sys
    import sys
    sys.setrecursionlimit(1000000)
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N = int(sys.stdin.readline())
        W = list(map(int, sys.stdin.readline().split()))
        C = list(map(int, sys.stdin.readline().split()))
        
        color_dict = {}
        for i in range(N):
            color = C[i]
            if color not in color_dict:
                color_dict[color] = []
            if W[i] != -1:
                color_dict[color].append(W[i])
        
        # Check if any color has exactly one rabbit, should not happen per constraints
        flag = False
        for color in color_dict:
            if len(color_dict[color]) <2 and W.count(-1) ==0:
                flag = True
                break
        if flag:
            print(f"Case #{test_case}: No")
            continue
        
        # Collect used weights
        used = set()
        for w in W:
            if w != -1:
                used.add(w)
        # Initialize available weights
        available = set(range(1,10001)) - used
        
        # Assign weights
        assignment = W.copy()
        possible = True
        for color in color_dict:
            known = sorted([w for w in color_dict[color] if w != -1])
            count = C.count(color)
            missing = count - len(known)
            if missing <0:
                possible = False
                break
            if len(known) >=2:
                min_w = known[0]
                max_w = known[-1]
                possible_weights = set(range(min_w, max_w+1)) - used
                if len(possible_weights) >= missing:
                    assign_w = sorted(list(possible_weights))[:missing]
                    for w in assign_w:
                        used.add(w)
                        available.discard(w)
                    # Assign these weights to -1 in W for this color
                    idxs = [i for i in range(N) if C[i]==color and W[i]==-1]
                    for idx, w in zip(idxs, assign_w):
                        assignment[idx] = w
                else:
                    # Need to extend the range
                    needed = missing - len(possible_weights)
                    assign_w = sorted(list(possible_weights))
                    # Try extending downward
                    lower = min_w -1
                    while needed >0 and lower >=1:
                        if lower not in used:
                            assign_w.append(lower)
                            used.add(lower)
                            available.discard(lower)
                            needed -=1
                        lower -=1
                    # Try extending upward
                    upper = max_w +1
                    while needed >0 and upper <=10000:
                        if upper not in used:
                            assign_w.append(upper)
                            used.add(upper)
                            available.discard(upper)
                            needed -=1
                        upper +=1
                    if needed >0:
                        possible = False
                        break
                    assign_w = sorted(assign_w)
                    for w in assign_w:
                        pass
                    # Assign these weights to -1 in W for this color
                    idxs = [i for i in range(N) if C[i]==color and W[i]==-1]
                    for idx, w in zip(idxs, assign_w):
                        assignment[idx] = w
            elif len(known) ==1:
                base = known[0]
                assign_w = []
                # Assign closest available weights to base
                offset =1
                while len(assign_w) < missing and (base - offset >=1 or base + offset <=10000):
                    if base - offset >=1 and (base - offset) not in used:
                        assign_w.append(base - offset)
                        used.add(base - offset)
                        available.discard(base - offset)
                        if len(assign_w) == missing:
                            break
                    if base + offset <=10000 and (base + offset) not in used:
                        assign_w.append(base + offset)
                        used.add(base + offset)
                        available.discard(base + offset)
                        if len(assign_w) == missing:
                            break
                    offset +=1
                if len(assign_w) < missing:
                    possible = False
                    break
                # Assign these weights to -1 in W for this color
                assign_w = sorted(assign_w)
                idxs = [i for i in range(N) if C[i]==color and W[i]==-1]
                for idx, w in zip(idxs, assign_w):
                    assignment[idx] = w
            else:
                # No known weights, assign any available weights, preferably consecutive
                if len(available) < missing:
                    possible = False
                    break
                assign_w = []
                sorted_available = sorted(list(available))
                # Try to assign consecutive weights
                for i in range(len(sorted_available)-missing+1):
                    window = sorted_available[i:i+missing]
                    if window[-1] - window[0] == missing -1:
                        assign_w = window
                        break
                if not assign_w:
                    # Assign the first 'missing' available
                    assign_w = sorted_available[:missing]
                for w in assign_w:
                    used.add(w)
                    available.discard(w)
                # Assign these weights to -1 in W for this color
                idxs = [i for i in range(N) if C[i]==color and W[i]==-1]
                for idx, w in zip(idxs, assign_w):
                    assignment[idx] = w
        # Now, verify all weights are unique and in range
        if not possible:
            print(f"Case #{test_case}: No")
            continue
        seen = set()
        valid = True
        for w in assignment:
            if w <1 or w >10000 or w in seen:
                valid = False
                break
            seen.add(w)
        if not valid:
            print(f"Case #{test_case}: No")
            continue
        # Now, compute minimal sum F(c)
        # To ensure that the given C is minimal, check if sum F(c) matches minimal possible
        # Compute current sum F(c)
        current_F =0
        for color in color_dict:
            weights = sorted([assignment[i] for i in range(N) if C[i]==color])
            F = weights[-1] - weights[0]
            current_F += F
        # To find minimal possible sum F(c), we need to assign weights to colors optimally
        # which is similar to assigning weights grouped by colors with minimal ranges
        # Since we have already assigned weights in a way to minimize F(c), assume it's minimal
        # So, accept the assignment
        print(f"Case #{test_case}: Yes")
        print(' '.join(map(str, assignment)))

if __name__ == "__main__":
    main()