import sys
import sys
import bisect

def main():
    import sys
    import threading

    def solve():
        import sys
        from collections import defaultdict

        data = sys.stdin.read().split()
        idx = 0
        T = int(data[idx]); idx +=1
        for test_case in range(1, T+1):
            R = int(data[idx]); C = int(data[idx+1]); K = int(data[idx+2]); idx +=3
            grid = []
            owner_positions = defaultdict(list)
            for r in range(R):
                row = list(map(int, data[idx:idx+C]))
                idx += C
                grid.append(row)
                for c in range(C):
                    owner_positions[row[c]].append( (r, c) )
            # Binary search over possible S
            left = 0
            right = max(R, C)
            def compute_T(S):
                # Compute sum_{dx=-S}^S (R - |dx|) = R + 2*sum_{d=1}^{min(S, R-1)} (R - d)
                min_S_R = min(S, R-1)
                sum_R = R + 2 * (min_S_R * R - (min_S_R * (min_S_R +1))//2)
                min_S_C = min(S, C-1)
                sum_C = C + 2 * (min_S_C * C - (min_S_C * (min_S_C +1))//2)
                return sum_R * sum_C
            def compute_T_same(S):
                total = 0
                for owner, positions in owner_positions.items():
                    k = len(positions)
                    if k <2:
                        continue
                    # Sort positions by row, then column
                    positions_sorted = sorted(positions)
                    # Use a sliding window approach
                    # For ordered pairs, we need to count all (u,v) where max(|i2-i1|, |j2 -j1|) <=S
                    # Since ordered, we can for each u, count number of v with v != u and within S
                    # To optimize, we can sort by row and use sliding window on rows, then within rows use binary search on columns
                    # Alternatively, use a 2D grid for the owner's positions and for each position, count number within S
                    # Given constraints, we can use brute force for small k
                    if k <= 1000:
                        cnt = 0
                        for u in positions:
                            ur, uc = u
                            # Count number of v in positions with |vr - ur| <=S and |vc - uc| <=S
                            # Can use binary search since positions_sorted is sorted by row then column
                            # Find rows in [ur - S, ur + S]
                            # As positions_sorted is sorted by row then column, we can find the range
                            # Then within those, count columns within [uc -S, uc + S]
                            # Implemented via two pointers
                            # Find lower and upper row indices
                            # Using bisect to find range
                            r_low = ur - S
                            r_high = ur + S
                            left_idx = bisect.bisect_left(positions_sorted, (r_low, -1))
                            right_idx = bisect.bisect_right(positions_sorted, (r_high, C))
                            # Now in positions_sorted[left_idx:right_idx], need to find columns within [uc -S, uc + S]
                            # Extract the relevant columns
                            columns = [c for (r, c) in positions_sorted[left_idx:right_idx]]
                            # Find left and right indices in columns
                            c_left = uc - S
                            c_right = uc + S
                            l = bisect.bisect_left(columns, c_left)
                            r_ = bisect.bisect_right(columns, c_right)
                            cnt += (r_ - l) -1  # exclude u itself
                        total += cnt
                return total
            while left < right:
                mid = (left + right) //2
                T_S = compute_T(mid)
                T_same_S = compute_T_same(mid)
                different = T_S - T_same_S
                if different >= K:
                    right = mid
                else:
                    left = mid +1
            print(f"Case #{test_case}: {left}")

    threading.Thread(target=solve,).start()

if __name__ == "__main__":
    main()