import sys
import threading

def main():
    import sys
    import heapq
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T+1):
        N = int(sys.stdin.readline())
        W = list(map(int, sys.stdin.readline().split()))
        C = list(map(int, sys.stdin.readline().split()))
        W_taken = set()
        color_rabbits = {}
        known_weights = {}
        total_missing = 0
        max_weight = 10000
        conflict = False
        for i in range(N):
            ci = C[i]
            wi = W[i]
            if ci not in color_rabbits:
                color_rabbits[ci] = []
                known_weights[ci] = []
            color_rabbits[ci].append(i)
            if wi != -1:
                if wi in W_taken:
                    conflict = True
                    break
                known_weights[ci].append(wi)
                W_taken.add(wi)
        if conflict:
            print(f'Case #{case_num}: No')
            continue
        colors = list(color_rabbits.keys())
        min_c = {}
        max_c = {}
        W_assign = [wi if wi != -1 else None for wi in W]
        W_indices_per_color = {}
        for c in colors:
            W_indices_per_color[c] = []
            known_w = known_weights[c]
            if known_w:
                min_c[c] = min(known_w)
                max_c[c] = max(known_w)
            else:
                # No known weights, start with some value between 1 and max_weight
                min_c[c] = max_weight // 2
                max_c[c] = max_weight // 2
            for idx in color_rabbits[c]:
                if W[idx] == -1:
                    W_indices_per_color[c].append(idx)
        possible = True
        assigned_weights = set(W_taken)
        for c in colors:
            idxs = W_indices_per_color[c]
            remaining = len(idxs)
            min_w = min_c[c]
            max_w = max_c[c]
            assigned = []
            candidates = []
            # Start from min_c and max_c and expand outward
            lptr = min_w
            rptr = max_w
            while remaining > 0:
                lptr -= 1
                rptr += 1
                candidates = []
                if lptr >= 1 and lptr not in assigned_weights:
                    candidates.append(lptr)
                if rptr <= max_weight and rptr not in assigned_weights:
                    candidates.append(rptr)
                # Try to assign weights as close as possible to min_c and max_c
                if not candidates:
                    continue
                for w in candidates:
                    assigned_weights.add(w)
                    assigned.append(w)
                    if w < min_c[c]:
                        min_c[c] = w
                    if w > max_c[c]:
                        max_c[c] = w
                    remaining -=1
                    if remaining ==0:
                        break
                if (lptr < 1 and rptr > max_weight) or (lptr < 1 and rptr in assigned_weights) and (rptr > max_weight and lptr in assigned_weights):
                    # No more weights to assign
                    possible = False
                    break
            if remaining > 0:
                possible = False
                break
            # Assign weights to indices
            for idx, w in zip(W_indices_per_color[c], assigned):
                W_assign[idx] = w
        if not possible:
            print(f'Case #{case_num}: No')
        else:
            # All missing weights assigned
            print(f'Case #{case_num}: Yes')
            print(' '.join(map(str, W_assign)))
    
threading.Thread(target=main).start()