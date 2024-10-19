import sys
import itertools
import bisect

def generate_mountain_numbers():
    mountains = []
    # Single-digit mountains
    for d in range(1, 10):
        mountains.append(d)
    # Multi-digit mountains
    for l in range(3, 20, 2):
        k = (l -1) //2
        for Dmid in range(2, 10):
            # Generate all non-decreasing sequences of length k with digits <= Dmid -1
            first_digits = list(itertools.combinations_with_replacement(range(1, Dmid), k))
            if k ==0:
                first_digits = [()]
            # Generate all non-increasing sequences of length k with digits <= Dmid -1
            last_digits = list(itertools.combinations_with_replacement(range(1, Dmid), k))
            if k ==0:
                last_digits = [()]
            for first in first_digits:
                for last in last_digits:
                    # Ensure that the last digits are non-increasing
                    last_sorted = sorted(last, reverse=True)
                    # Construct the number
                    number = 0
                    for d in first:
                        number = number *10 + d
                    number = number *10 + Dmid
                    for d in last_sorted:
                        number = number *10 + d
                    mountains.append(number)
    mountains = sorted(mountains)
    return mountains

def main():
    mountains = generate_mountain_numbers()
    input = sys.stdin.read().split()
    T = int(input[0])
    idx =1
    for t in range(1, T +1):
        A = int(input[idx])
        B = int(input[idx +1])
        M = int(input[idx +2])
        idx +=3
        # Find the range of mountains within [A,B]
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count =0
        for num in mountains[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{t}: {count}")

if __name__ == "__main__":
    main()