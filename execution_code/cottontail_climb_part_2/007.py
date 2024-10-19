import sys
import itertools
from bisect import bisect_left, bisect_right

def readints():
    return list(map(int, sys.stdin.read().split()))

def generate_non_decreasing(k, max_digit):
    # Generate all non-decreasing sequences of length k with digits from 1 to max_digit
    return itertools.combinations_with_replacement(range(1, max_digit), k)

def generate_non_increasing(k, max_digit):
    # Generate all non-increasing sequences of length k with digits from 1 to max_digit
    return itertools.combinations_with_replacement(range(1, max_digit), k)

def main():
    import sys
    import threading
    def run():
        import sys
        T,*rest = map(int, sys.stdin.read().split())
        test_cases = []
        for i in range(T):
            A, B, M = rest[3*i:3*(i+1)]
            test_cases.append((A, B, M))
        
        # Precompute all mountain numbers
        mountains = []
        for k in range(0, 10):
            for D in range(k+1, 10):
                if k == 0:
                    num = D
                    mountains.append(num)
                else:
                    # Generate all non-decreasing first k digits from 1 to D-1
                    first_seqs = itertools.combinations_with_replacement(range(1, D), k)
                    # Generate all non-increasing last k digits from 1 to D-1
                    last_seqs = itertools.combinations_with_replacement(range(1, D), k)
                    first_seqs = list(first_seqs)
                    last_seqs = list(last_seqs)
                    for first in first_seqs:
                        # Convert first sequence to number
                        first_num = 0
                        for digit in first:
                            first_num = first_num *10 + digit
                        for last in last_seqs:
                            # Convert last sequence to number (non-increasing)
                            last_num = 0
                            for digit in reversed(last):
                                last_num = last_num *10 + digit
                            # Combine to form the full number
                            num = first_num * (10**(k+1)) + D * (10**k) + last_num
                            mountains.append(num)
        
        mountains = sorted(mountains)
        
        # To handle large lists, convert to list once
        mountains = sorted(mountains)
        
        for idx, (A, B, M) in enumerate(test_cases):
            # Find left and right indices
            left = bisect_left(mountains, A)
            right = bisect_right(mountains, B)
            count = 0
            for num in mountains[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{idx+1}: {count}")
    
    threading.Thread(target=run,).start()

import sys
import itertools
from bisect import bisect_left, bisect_right

def readints():
    return list(map(int, sys.stdin.read().split()))

def generate_non_decreasing(k, max_digit):
    # Generate all non-decreasing sequences of length k with digits from 1 to max_digit
    return itertools.combinations_with_replacement(range(1, max_digit), k)

def generate_non_increasing(k, max_digit):
    # Generate all non-increasing sequences of length k with digits from 1 to max_digit
    return itertools.combinations_with_replacement(range(1, max_digit), k)

def main():
    import sys
    import threading
    def run():
        import sys
        T,*rest = map(int, sys.stdin.read().split())
        test_cases = []
        for i in range(T):
            A, B, M = rest[3*i:3*(i+1)]
            test_cases.append((A, B, M))
        
        # Precompute all mountain numbers
        mountains = []
        for k in range(0, 10):
            for D in range(k+1, 10):
                if k == 0:
                    num = D
                    mountains.append(num)
                else:
                    # Generate all non-decreasing first k digits from 1 to D-1
                    first_seqs = itertools.combinations_with_replacement(range(1, D), k)
                    # Generate all non-increasing last k digits from 1 to D-1
                    last_seqs = itertools.combinations_with_replacement(range(1, D), k)
                    first_seqs = list(first_seqs)
                    last_seqs = list(last_seqs)
                    for first in first_seqs:
                        # Convert first sequence to number
                        first_num = 0
                        for digit in first:
                            first_num = first_num *10 + digit
                        for last in last_seqs:
                            # Convert last sequence to number (non-increasing)
                            last_num = 0
                            for digit in reversed(last):
                                last_num = last_num *10 + digit
                            # Combine to form the full number
                            num = first_num * (10**(k+1)) + D * (10**k) + last_num
                            mountains.append(num)
        
        mountains = sorted(mountains)
        
        # To handle large lists, convert to list once
        mountains = sorted(mountains)
        
        for idx, (A, B, M) in enumerate(test_cases):
            # Find left and right indices
            left = bisect_left(mountains, A)
            right = bisect_right(mountains, B)
            count = 0
            for num in mountains[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{idx+1}: {count}")
    
    threading.Thread(target=run,).start()