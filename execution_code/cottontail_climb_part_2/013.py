import sys
import itertools
import bisect

def generate_mountain_numbers():
    mountains = set()
    # Handle k=0 separately: single-digit numbers from 1 to 9
    for m in range(1, 10):
        mountains.add(m)
    # For k=1 to 9 (length=3 to 19)
    for k in range(1, 10):
        length = 2 * k +1
        for m in range(1, 10):
            if m ==1 and k >=1:
                # For m=1 and k>=1, first k digits from 1 to m-1=0, which is invalid
                continue
            # Generate all possible first k digits: non-decreasing, digits from 1 to m-1
            if m-1 <1 and k>=1:
                # No valid digits for first k digits
                continue
            if k ==0:
                first_parts = [()]
            else:
                # Non-decreasing sequences: combinations with replacement
                first_parts = itertools.combinations_with_replacement(range(1, m), k)
            # Similarly, generate all possible last k digits: non-increasing, digits from 1 to m-1
            if m-1 <1 and k>=1:
                # No valid digits for last k digits
                continue
            if k ==0:
                last_parts = [()]
            else:
                last_parts = itertools.combinations_with_replacement(range(1, m), k)
                # To make non-increasing, we need to sort each combination in reverse
                last_parts = [tuple(reversed(part)) for part in last_parts]
            # Combine first_parts and last_parts
            if k ==0:
                # Only the middle digit
                mountains.add(m)
            else:
                for first in first_parts:
                    # Ensure first is non-decreasing
                    # Already ensured by combinations_with_replacement
                    for last in last_parts:
                        # Ensure last is non-increasing
                        # Already ensured by reversed combinations
                        # Now, assemble the number
                        num_digits = list(first) + [m] + list(last)
                        # Now, check if middle digit m is unique
                        # Since first k digits are <m and last k digits are <=m-1 <m, m appears only once
                        # So no need for additional check
                        # Now, convert to integer
                        num = 0
                        for d in num_digits:
                            num = num *10 + d
                        mountains.add(num)
    # Return the sorted list
    return sorted(mountains)

def readints():
    import sys
    return list(map(int, sys.stdin.read().split()))

def main():
    mountains = generate_mountain_numbers()
    # Read input
    data = readints()
    T = data[0]
    idx =1
    for ti in range(1, T+1):
        A = data[idx]
        B = data[idx+1]
        M = data[idx+2]
        idx +=3
        # Find the range in mountains
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count =0
        subset = mountains[left:right]
        if M ==0:
            # If M=0, avoid division
            cnt =0
        else:
            for num in subset:
                if num % M ==0:
                    count +=1
        print(f"Case #{ti}: {count}")

if __name__ == "__main__":
    main()