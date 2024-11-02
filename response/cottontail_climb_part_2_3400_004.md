**Key Findings:**

1. **Mountain Number Characteristics:**
   - Mountain numbers must have an odd number of digits (`2k + 1`) with no zeros.
   - The first `k+1` digits are non-decreasing, and the last `k+1` digits are non-increasing.
   - The middle digit must be strictly greater than its immediate neighbors.

2. **Generation of Mountain Numbers:**
   - For each possible length (`1, 3, 5, ..., 17`), iterate through possible middle digits (`2` to `9`).
   - Generate all possible non-decreasing sequences for the left half and non-increasing sequences for the right half using combinations with replacement.
   - Combine left sequences, the middle digit, and right sequences to form valid mountain numbers.

3. **Efficiency Considerations:**
   - Precompute and store all possible mountain numbers up to `10^18` since their total count is manageable.
   - Sort the list of mountain numbers to enable efficient range queries using binary search.
   - For each test case, perform binary searches to find mountain numbers within the range `[A, B]` and count those divisible by `M`.

4. **Handling Multiple Test Cases:**
   - Precompute the mountain numbers once and reuse the sorted list for all test cases.
   - Utilize Python's `bisect` module for efficient range queries.

**Python Code:**

```python
import sys
import bisect
from itertools import combinations_with_replacement

def generate_mountain_numbers():
    mountain_numbers = set()

    # Single-digit mountain numbers
    for d in range(1, 10):
        mountain_numbers.add(d)

    # Generate mountain numbers with length >=3
    for k in range(1, 9):  # k from 1 to8, L=2k+1 up to 17
        L = 2 * k + 1
        for D in range(2, 10):  # Middle digit from 2 to9
            # Generate all non-decreasing left sequences of length k with digits from 1 to D-1
            left_seqs = combinations_with_replacement(range(1, D), k)
            left_seqs = list(left_seqs)
            if not left_seqs:
                continue
            # Generate all non-increasing right sequences of length k with digits from 1 to D-1
            # To generate non-increasing, generate non-decreasing and reverse
            right_seqs = combinations_with_replacement(range(1, D), k)
            right_seqs = [seq[::-1] for seq in right_seqs]
            if not right_seqs:
                continue
            # Combine left and right sequences with middle digit D
            for left in left_seqs:
                left_part = ''.join(str(d) for d in left)
                for right in right_seqs:
                    right_part = ''.join(str(d) for d in right)
                    number_str = left_part + str(D) + right_part
                    number = int(number_str)
                    mountain_numbers.add(number)

    # Return sorted list of mountain numbers
    return sorted(mountain_numbers)

def main():
    mountain_numbers = generate_mountain_numbers()

    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        A_str, B_str, M_str = sys.stdin.readline().strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)

        # Find the indices of mountain numbers within [A, B]
        left_idx = bisect.bisect_left(mountain_numbers, A)
        right_idx = bisect.bisect_right(mountain_numbers, B)

        count = 0
        # Iterate through the relevant subset and count divisible by M
        for num in mountain_numbers[left_idx:right_idx]:
            if num % M == 0:
                count += 1

        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()
```