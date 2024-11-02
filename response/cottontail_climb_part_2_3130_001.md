To solve this problem, we will generate all possible mountain numbers up to 19 digits and then, for each test case, count how many of these numbers are within the given range \([A, B]\) and are divisible by \(M\).

**Key Findings:**

- **Definition of Mountain Numbers:** Mountain numbers have specific properties: they have an odd length \(L = 2k + 1\), their digits increase up to the middle digit (which is unique) and then decrease, none of the digits are zero, and the first \(k+1\) digits are monotonically non-decreasing while the last \(k+1\) digits are monotonically non-increasing.
  
- **Generation of Mountain Numbers:**
  - We define a recursive function to generate mountain numbers for each possible odd length up to 19.
  - We ensure that the middle digit does not appear elsewhere in the number.
  - We enforce the monotonicity constraints on the digits.

- **Counting in the Range and Divisibility:**
  - After generating all possible mountain numbers, we sort them for efficient range queries.
  - For each test case, we iterate over the mountain numbers within the range \([A, B]\) and check for divisibility by \(M\).

- **Efficiency:**
  - The total number of mountain numbers generated is manageable and allows for precomputing and storing.
  - Sorting the list of mountain numbers aids in efficient searching for numbers within the specified range.

```python
def read_int():
    return int(input())

def read_ints():
    return map(int, input().split())

def generate_mountain_numbers():
    mountain_numbers = []

    def dfs(pos, length, is_left_half, prev_digit, used_digits_set, number_so_far):
        if pos == length:
            number = int(''.join(map(str, number_so_far)))
            mountain_numbers.append(number)
            return
        k = (length - 1) // 2
        if pos <= k:
            # Left half including middle digit
            start_digit = prev_digit if pos > 0 else 1
            for d in range(start_digit, 10):
                if pos == k:
                    # Middle digit must be unique
                    if d in used_digits_set:
                        continue
                    # For the middle digit
                    used_digits_set.add(d)
                    number_so_far.append(d)
                    dfs(pos + 1, length, False, d, used_digits_set, number_so_far)
                    number_so_far.pop()
                    used_digits_set.remove(d)
                else:
                    if d in used_digits_set:
                        continue
                    used_digits_set.add(d)
                    number_so_far.append(d)
                    dfs(pos + 1, length, True, d, used_digits_set, number_so_far)
                    number_so_far.pop()
                    used_digits_set.remove(d)
        else:
            # Right half
            prev_middle_digit = number_so_far[(length - 1) // 2]
            start_digit = 1
            end_digit = prev_digit
            for d in range(start_digit, end_digit + 1):
                if d == prev_middle_digit:
                    continue  # Middle digit must be unique
                number_so_far.append(d)
                dfs(pos + 1, length, False, d, used_digits_set, number_so_far)
                number_so_far.pop()

    for length in range(1, 20, 2):  # Lengths from 1 to 19, step 2
        dfs(0, length, True, 0, set(), [])
    return sorted(mountain_numbers)

def count_mountain_numbers_in_range(mountain_numbers, A, B, M):
    from bisect import bisect_left, bisect_right
    left = bisect_left(mountain_numbers, A)
    right = bisect_right(mountain_numbers, B)
    count = 0
    for num in mountain_numbers[left:right]:
        if num % M == 0:
            count += 1
    return count

def main():
    T = read_int()
    mountain_numbers = generate_mountain_numbers()
    for case_num in range(1, T + 1):
        A_str, B_str, M_str = input().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        count = count_mountain_numbers_in_range(mountain_numbers, A, B, M)
        print(f"Case #{case_num}: {count}")

if __name__ == "__main__":
    main()
```