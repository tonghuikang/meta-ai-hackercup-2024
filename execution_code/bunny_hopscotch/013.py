import sys
import bisect

def main():
    import sys
    import threading

    def solve():
        import sys

        T = int(sys.stdin.readline())
        for test_case in range(1, T +1):
            R, C, K = map(int, sys.stdin.readline().split())
            B = []
            owner_to_positions = {}
            for i in range(1, R +1):
                row = list(map(int, sys.stdin.readline().split()))
                for j in range(1, C +1):
                    owner = row[j -1]
                    if owner not in owner_to_positions:
                        owner_to_positions[owner] = []
                    owner_to_positions[owner].append( (i, j) )
            # Function to compute total_hops_s
            def total_hops(s):
                # Compute sum_k_i
                if s >= R -1:
                    sum_k_i = R * R
                else:
                    sum_k_i = R*(2*s +1) - s*(s +1)
                # Compute sum_k_j
                if s >= C -1:
                    sum_k_j = C * C
                else:
                    sum_k_j = C*(2*s +1) - s*(s +1)
                return sum_k_i * sum_k_j

            # Function to compute invalid_hops_s
            def invalid_hops(s):
                total_invalid =0
                for positions in owner_to_positions.values():
                    n = len(positions)
                    if n <2:
                        continue
                    # Sort positions by row, then column
                    positions_sorted = sorted(positions)
                    # Use sliding window
                    window = []
                    cols = []
                    count =0
                    left =0
                    sorted_cols = []
                    for pos in positions_sorted:
                        i, j = pos
                        # Remove positions with row < i -s
                        while left < len(positions_sorted) and positions_sorted[left][0] < i - s:
                            # Remove their j from sorted_cols
                            old_j = positions_sorted[left][1]
                            idx = bisect.bisect_left(sorted_cols, old_j)
                            if idx < len(sorted_cols) and sorted_cols[idx] == old_j:
                                sorted_cols.pop(idx)
                            left +=1
                        # Now, sorted_cols contains j of burrows with row >= i -s
                        # Find number of j in [j -s, j +s]
                        low_j = j - s
                        high_j = j + s
                        left_idx = bisect.bisect_left(sorted_cols, low_j)
                        right_idx = bisect.bisect_right(sorted_cols, high_j)
                        cnt = right_idx - left_idx
                        count += cnt
                        # Insert current j into sorted_cols
                        bisect.insort(sorted_cols, j)
                    # Each unordered pair is counted once, multiply by 2 for ordered pairs
                    total_invalid += 2 * count
                return total_invalid

            # Binary search
            low =0
            high = max(R, C)
            answer = high
            while low <= high:
                mid = (low + high) //2
                th = total_hops(mid)
                ih = invalid_hops(mid)
                vh = th - ih
                if vh >= K:
                    answer = mid
                    high = mid -1
                else:
                    low = mid +1
            print(f"Case #{test_case}: {answer}")

    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()