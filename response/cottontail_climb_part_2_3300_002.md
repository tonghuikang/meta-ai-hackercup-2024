When solving this problem, the key steps and considerations are as follows:

1. **Understanding Mountain Numbers**: 
   - A mountain number has an odd number of digits \(2k + 1\).
   - All digits are non-zero.
   - The first \(k+1\) digits are non-decreasing.
   - The last \(k+1\) digits are non-increasing.
   - The middle digit is strictly greater than its immediate neighbors, ensuring it is a unique peak.

2. **Generating Mountain Numbers**:
   - Iterate through all possible odd lengths from 1 to 17 digits.
   - For each length, generate all possible middle digits (from 2 to 9).
   - For each middle digit, generate all non-decreasing sequences for the first half and all non-increasing sequences for the second half.
   - Combine these parts to form full mountain numbers and store them in a sorted list.

3. **Counting Valid Mountains**:
   - For each test case, use binary search to find the range of mountain numbers that fall within \([A, B]\).
   - Iterate through this range and count how many numbers are divisible by \(M\).

4. **Optimization**:
   - Precompute all mountain numbers once and reuse them across test cases.
   - Utilize efficient sequence generation methods to handle large numbers within the constraints.

Here's the Python implementation incorporating these steps:

```python
import sys
import itertools
import bisect

def generate_non_decreasing_sequences(k, max_digit):
    if k == 0:
        return [()]
    # digits from 1 to max_digit
    return list(itertools.combinations_with_replacement(range(1, max_digit +1), k))

def generate_non_increasing_sequences(k, max_digit):
    if k ==0:
        return [()]
    # Generate non-decreasing sequences and reverse them
    sequences = itertools.combinations_with_replacement(range(1, max_digit +1), k)
    return [seq[::-1] for seq in list(sequences)]

def generate_mountain_numbers():
    mountains = []
    # odd lengths from1 to17
    for l in range(1, 19, 2):
        k = (l -1)//2
        if l ==1:
            # single-digit mountains:1-9
            mountains.extend(range(1,10))
            continue
        # for l>=3
        for middle_digit in range(2,10):
            first_max = middle_digit -1
            if first_max <1:
                continue
            # generate all non-decreasing sequences of length k with digits 1 to first_max
            first_sequences = generate_non_decreasing_sequences(k, first_max)
            # generate all non-increasing sequences of length k with digits 1 to first_max
            last_sequences = generate_non_increasing_sequences(k, first_max)
            for first in first_sequences:
                for last in last_sequences:
                    # Construct the number
                    # Convert sequences to digits
                    number_digits = list(first) + [middle_digit] + list(last)
                    # Convert to integer
                    number = 0
                    for d in number_digits:
                        number = number *10 + d
                    mountains.append(number)
    mountains.sort()
    return mountains

def main():
    import sys
    import threading
    def run():
        mountains = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for test_case in range(1, T+1):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            A_str, B_str, M_str = line.strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find left and right indices
            left = bisect.bisect_left(mountains, A)
            right = bisect.bisect_right(mountains, B)
            count =0
            if M ==1:
                count = right - left
            else:
                # Iterate through mountains[left:right] and count divisible by M
                # To optimize, iterate and check divisibility
                for num in mountains[left:right]:
                    if num % M ==0:
                        count +=1
            print(f"Case #{test_case}: {count}")
    threading.Thread(target=run,).start()

if __name__ == "__main__":
    main()
```