import sys
import bisect

def readints():
    return list(map(int, sys.stdin.read().split()))

def compute_total_pairs(R, C, s):
    total = 0
    for dx in range(0, s + 1):
        x_count = R - dx
        for dy in range(0, s + 1):
            y_count = C - dy
            if dx == 0 and dy == 0:
                total += x_count * y_count
            elif dx == 0 or dy == 0:
                total += 2 * x_count * y_count
            else:
                total += 4 * x_count * y_count
    return total

def compute_same_owner_pairs(R, C, s, owners):
    total = 0
    for owner, pos_list in owners.items():
        t = len(pos_list)
        if t < 2:
            continue
        # Sort positions by row, then by column
        pos_sorted = sorted(pos_list, key=lambda x: (x[0], x[1]))
        n = len(pos_sorted)
        for k in range(n):
            ai, aj = pos_sorted[k]
            # Find the lower bound for row
            l = k
            while l > 0 and pos_sorted[l-1][0] >= ai - s:
                l -=1
            # Find the upper bound for row
            r = k
            while r < n-1 and pos_sorted[r+1][0] <= ai + s:
                r +=1
            # Extract the candidate columns
            candidates = [pos_sorted[m][1] for m in range(l, r+1)]
            # Find number of columns within [aj - s, aj + s]
            left = bisect.bisect_left(candidates, aj - s)
            right = bisect.bisect_right(candidates, aj + s)
            cnt = right - left
            # Exclude the current position
            if aj - s <= aj <= aj + s:
                cnt -=1
            total += cnt
    return total

def main():
    data = readints()
    ptr = 0
    T = data[ptr]
    ptr +=1
    for test_case in range(1, T+1):
        R = data[ptr]
        C = data[ptr+1]
        K = data[ptr+2]
        ptr +=3
        owners = {}
        for i in range(1, R+1):
            for j in range(1, C+1):
                b = data[ptr]
                ptr +=1
                if b not in owners:
                    owners[b] = []
                owners[b].append((i,j))
        # Binary search over possible scores
        left = 0
        right = max(R, C)
        while left < right:
            mid = (left + right) //2
            total_pairs = compute_total_pairs(R, C, mid)
            same_pairs = compute_same_owner_pairs(R, C, mid, owners)
            diff_pairs = total_pairs - same_pairs
            if diff_pairs >= K:
                right = mid
            else:
                left = mid +1
        print(f"Case #{test_case}: {left}")

if __name__ == "__main__":
    main()