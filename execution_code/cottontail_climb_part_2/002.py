import sys
import bisect
from itertools import combinations_with_replacement, combinations
from math import comb

def generate_mountain_numbers():
    mountains = set()
    # Maximum number of digits is 19 (since B <= 1e18)
    for total_digits in range(1, 20, 2):
        k = (total_digits -1) //2
        # Iterate over possible middle digit
        for c in range(1,10):
            # Generate all non-decreasing sequences of length k from 1 to c-1
            if k ==0:
                first_half = ['']
            else:
                # Using combinations_with_replacement
                # Generate all sequences where each digit is >= previous and <=c-1
                # We need to generate all possible tuples
                first_half = []
                def backtrack_first(pos, current):
                    if pos == k:
                        first_half.append(''.join(map(str, current)))
                        return
                    start = 1 if pos ==0 else current[-1]
                    for d in range(start, c):
                        current.append(d)
                        backtrack_first(pos+1, current)
                        current.pop()
                backtrack_first(0, [])
            # Generate all non-increasing sequences of length k from 1 to c-1
            if k ==0:
                second_half = ['']
            else:
                second_half = []
                def backtrack_second(pos, current):
                    if pos ==k:
                        second_half.append(''.join(map(str, current)))
                        return
                    start = c-1 if pos ==0 else current[-1]
                    for d in range(1, start+1):
                        current.append(d)
                        backtrack_second(pos+1, current)
                        current.pop()
                backtrack_second(0, [])
            # Combine first half, middle digit, and second half
            for fh in first_half:
                for sh in second_half:
                    number_str = fh + str(c) + sh
                    number = int(number_str)
                    mountains.add(number)
    mountains = sorted(mountains)
    return mountains

def main():
    import sys
    import threading
    def run():
        mountains = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for test_case in range(1, T+1):
            A, B, M = sys.stdin.readline().strip().split()
            A = int(A)
            B = int(B)
            M = int(M)
            # Find the indices in mountains where mountain >= A and mountain <= B
            left = bisect.bisect_left(mountains, A)
            right = bisect.bisect_right(mountains, B)
            count = 0
            for num in mountains[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{test_case}: {count}")
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()