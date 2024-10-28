import sys
import bisect
from itertools import combinations_with_replacement, product

def generate_mountain_numbers():
    mountains = set()
    # Single-digit mountain numbers
    for d in range(1, 10):
        mountains.add(d)
    
    # Generate for lengths 3,5,...,19
    for total_digits in range(3, 20, 2):
        k = (total_digits - 1) // 2
        # Middle digit
        for m in range(1, 10):
            # Generate first k digits: non-decreasing, digits from 1 to m-1
            if k == 0:
                first_k_digits_list = ['']
            else:
                # Generate all non-decreasing sequences of length k from 1 to m-1
                # using combinations with replacement
                first_k_digits_list = []
                for comb in combinations_with_replacement(range(1, m), k):
                    first_k_digits_list.append(''.join(map(str, comb)))
                if not first_k_digits_list:
                    continue  # No valid first k digits
            # Generate last k digits: non-increasing, digits from 1 to m-1
            if k == 0:
                last_k_digits_list = ['']
            else:
                # Generate all non-increasing sequences of length k from 1 to m-1
                # This is similar to generating all combinations with replacement
                # in reverse order
                last_k_digits_list = []
                for comb in combinations_with_replacement(range(1, m), k):
                    # To make it non-increasing, sort in reverse
                    sorted_comb = sorted(comb, reverse=True)
                    last_k_digits_list.append(''.join(map(str, sorted_comb)))
                if not last_k_digits_list:
                    continue  # No valid last k digits
            # Combine first k digits, middle digit, and last k digits
            for first in first_k_digits_list:
                for last in last_k_digits_list:
                    num_str = first + str(m) + last
                    # Ensure that the middle digit m does not appear in the last k digits
                    if 'm' in last:
                        continue
                    mountains.add(int(num_str))
    return sorted(mountains)

def main():
    import sys
    import threading
    def run():
        mountains = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for tc in range(1, T+1):
            A_str, B_str, M_str = sys.stdin.readline().strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find the indices in mountains where mountain >= A and mountain <= B
            left = bisect.bisect_left(mountains, A)
            right = bisect.bisect_right(mountains, B)
            count = 0
            for num in mountains[left:right]:
                if num % M == 0:
                    count +=1
            print(f"Case #{tc}: {count}")
    threading.Thread(target=run,).start()

if __name__ == "__main__":
    main()