import sys
import bisect
from itertools import combinations_with_replacement, product

def generate_prefixes(k, max_digit):
    if k == 0:
        return ['']
    prefixes = []

    def backtrack(current, last):
        if len(current) == k:
            prefixes.append(''.join(map(str, current)))
            return
        for d in range(last, max_digit +1):
            current.append(d)
            backtrack(current, d)
            current.pop()

    for last_digit in range(1, max_digit):
        backtrack([last_digit], last_digit)
    return prefixes

def generate_suffixes(k, max_digit):
    if k == 0:
        return ['']
    suffixes = []

    def backtrack(current, last):
        if len(current) == k:
            suffixes.append(''.join(map(str, current)))
            return
        for d in range(last, max_digit +1):
            current.append(d)
            backtrack(current, d)
            current.pop()

    for first_digit in range(1, max_digit):
        backtrack([first_digit], first_digit)
    return suffixes

def generate_mountain_numbers():
    mountain_numbers = set()
    for length in range(1, 20, 2):
        k = (length -1)//2
        if k ==0:
            # Single-digit numbers
            for d in range(1,10):
                mountain_numbers.add(d)
            continue
        for d in range(1,10):
            # Generate prefixes: non-decreasing of length k, last digit < d
            prefixes = []

            def backtrack_prefix(position, current, last):
                if position == k:
                    prefixes.append(''.join(map(str, current)))
                    return
                for next_d in range(last, d):
                    current.append(next_d)
                    backtrack_prefix(position +1, current, next_d)
                    current.pop()

            backtrack_prefix(0, [], 1)

            # Generate suffixes: non-increasing of length k, first digit < d
            suffixes = []

            def backtrack_suffix(position, current, last):
                if position == k:
                    suffixes.append(''.join(map(str, current)))
                    return
                for next_d in range(1, last +1):
                    current.append(next_d)
                    backtrack_suffix(position +1, current, next_d)
                    current.pop()

            backtrack_suffix(0, [], d -1)

            # Combine prefixes, d, suffixes
            for prefix in prefixes:
                for suffix in suffixes:
                    num_str = prefix + str(d) + suffix
                    num = int(num_str)
                    mountain_numbers.add(num)
    sorted_mountain = sorted(mountain_numbers)
    return sorted_mountain

def main():
    import sys
    import threading

    def run():
        sorted_mountain = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for test_case in range(1, T+1):
            A, B, M = map(int, sys.stdin.readline().split())
            left = bisect.bisect_left(sorted_mountain, A)
            right = bisect.bisect_right(sorted_mountain, B)
            count = 0
            if M ==1:
                count = right - left
            else:
                # Iterate through the relevant range and count multiples
                for num in sorted_mountain[left:right]:
                    if num % M ==0:
                        count +=1
            print(f"Case #{test_case}: {count}")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()