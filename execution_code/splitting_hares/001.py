#!/usr/bin/env python3
import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        N = int(sys.stdin.readline())
        W_line = sys.stdin.readline().split()
        C_line = sys.stdin.readline().split()
        W = []
        C = []
        known_weights = set()
        weight_indices = {}
        missing_indices = []
        for i in range(N):
            w = W_line[i]
            if w == '-1':
                W.append(-1)
                missing_indices.append(i)
            else:
                w = int(w)
                W.append(w)
                known_weights.add(w)
                weight_indices[i] = w
        C = [int(c) for c in C_line]
        # We need to assign missing weights
        # Collect the rabbits per color
        color_rabbits = {}
        for i in range(N):
            c = C[i]
            if c not in color_rabbits:
                color_rabbits[c] = []
            color_rabbits[c].append(i)
        # Check that no color is assigned to exactly one rabbit
        impossible = False
        for c in color_rabbits:
            if len(color_rabbits[c]) == 1:
                impossible = True
                break
        if impossible:
            print('Case #{}: No'.format(test_case))
            continue
        # Assign missing weights
        W_assigned = W.copy()
        used_weights = set(known_weights)
        weight_c = {}  # weights per color
        for c in color_rabbits:
            indices = color_rabbits[c]
            weights_c = []
            for idx in indices:
                if W_assigned[idx] != -1:
                    weights_c.append(W_assigned[idx])
            # Assign missing weights
            u_c = len(indices) - len(weights_c)
            if u_c == 0:
                weight_c[c] = sorted(weights_c)
                continue
            else:
                # Need to assign weights
                positions = []
                if weights_c:
                    min_c = min(weights_c)
                    max_c = max(weights_c)
                    # Try to assign missing weights between min_c and max_c
                    for w in range(min_c+1, max_c):
                        if w not in used_weights:
                            positions.append(w)
                            used_weights.add(w)
                            if len(positions) == u_c:
                                break
                    # If not enough positions, assign weights adjacent to min and max
                    w_down = min_c -1
                    w_up = max_c +1
                    while len(positions) < u_c:
                        assigned = False
                        if w_down >=1 and w_down not in used_weights:
                            positions.append(w_down)
                            used_weights.add(w_down)
                            w_down -=1
                            assigned = True
                        if len(positions) == u_c:
                            break
                        if w_up <=10000 and w_up not in used_weights:
                            positions.append(w_up)
                            used_weights.add(w_up)
                            w_up +=1
                            assigned = True
                        if not assigned:
                            break
                    if len(positions) < u_c:
                        impossible = True
                        break
                else:
                    # No known weights in color c
                    # Assign arbitrary weights
                    positions = []
                    w = 1
                    while len(positions) < u_c:
                        if w not in used_weights:
                            positions.append(w)
                            used_weights.add(w)
                        w +=1
                    weights_c = positions.copy()
                # Assign positions to missing rabbits in c
                pos_idx = 0
                for idx in indices:
                    if W_assigned[idx] == -1:
                        W_assigned[idx] = positions[pos_idx]
                        pos_idx +=1
                weights_c.extend(positions)
                weight_c[c] = sorted(weights_c)
        if impossible:
            print('Case #{}: No'.format(test_case))
            continue
        # Now, W_assigned is complete
        # Compute total sum F(c) for given shirt colors
        sum_Fc_assigned = 0
        for c in color_rabbits:
            weights = []
            for idx in color_rabbits[c]:
                weights.append(W_assigned[idx])
            F_c = max(weights) - min(weights)
            sum_Fc_assigned += F_c
        # Compute minimal total sum F(c) via DP
        W_full = W_assigned.copy()
        W_full.sort()
        N = len(W_full)
        INF = float('inf')
        dp = [INF]*(N+1)
        dp[0]=0
        dp[1]=INF  # Cannot have group of size 1
        for i in range(2, N+1):
            # Form group of size 2
            dp[i]=dp[i-2]+W_full[i-1]-W_full[i-2]
            # If possible, form group of size 3
            if i>=3:
                dp[i]=min(dp[i], dp[i-3]+W_full[i-1]-W_full[i-3])
        total_min_Fc = dp[N]
        if sum_Fc_assigned == total_min_Fc:
            print('Case #{}: Yes'.format(test_case))
            print(' '.join(map(str, W_assigned)))
        else:
            print('Case #{}: No'.format(test_case))

# threading.Thread(target=main).start()
threading.Thread(target=main).start()