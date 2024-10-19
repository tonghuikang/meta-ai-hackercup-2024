import sys
import bisect
from functools import lru_cache

@lru_cache(maxsize=None)
def generate_non_decreasing(k, max_digit, min_digit=1):
    if k == 0:
        return [tuple()]
    sequences = []
    for digit in range(min_digit, max_digit + 1):
        for seq in generate_non_decreasing(k - 1, max_digit, digit):
            sequences.append((digit,) + seq)
    return sequences

@lru_cache(maxsize=None)
def generate_non_increasing(k, max_digit, min_digit=1):
    if k == 0:
        return [tuple()]
    sequences = []
    for digit in range(min_digit, max_digit + 1):
        for seq in generate_non_increasing(k - 1, digit, min_digit):
            sequences.append((digit,) + seq)
    return sequences

def generate_mountain_numbers():
    mountains = []
    for L in range(1, 20, 2):
        k = (L - 1) // 2
        if L == 1:
            mountains.extend(range(1, 10))
            continue
        for D in range(2, 10):
            if D - 1 < 1:
                continue
            D_left_sequences = generate_non_decreasing(k, D - 1, 1)
            D_right_sequences = generate_non_increasing(k, D - 1, 1)
            for D_left in D_left_sequences:
                for D_right in D_right_sequences:
                    num_str = ''.join(map(str, D_left)) + str(D) + ''.join(map(str, D_right))
                    num = int(num_str)
                    mountains.append(num)
    mountains.sort()
    return mountains

def main():
    mountains = generate_mountain_numbers()
    input = sys.stdin.read().splitlines()
    T = int(input[0])
    test_cases = [tuple(map(int, line.strip().split())) for line in input[1:T+1]]
    for idx, (A, B, M) in enumerate(test_cases, 1):
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        # To speed up, use list slicing and list comprehension
        subset = mountains[left:right]
        if M == 1:
            count = len(subset)
        else:
            count = sum(1 for num in subset if num % M == 0)
        print(f"Case #{idx}: {count}")

if __name__ == "__main__":
    main()