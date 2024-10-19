import sys
import threading

def main():
    import sys

    sys.setrecursionlimit(1 << 25)
    max_length = 19  # Maximum possible length up to 19 digits

    mountain_numbers = []

    # Function to generate mountain numbers
    def generate_mountains():
        for k in range(0, (max_length - 1) // 2 + 1):
            if k == 0:
                # For k = 0, length = 1
                for d in range(1, 10):
                    number = d
                    mountain_numbers.append(number)
            else:
                seq = []
                generate_sequence(0, k, seq)

    # Recursive function to generate sequences
    def generate_sequence(pos, k, seq):
        if pos == 0:
            # First position, digits from 1 to 9
            for d in range(1, 10):
                seq.append(d)
                generate_sequence(pos + 1, k, seq)
                seq.pop()
        elif pos < k:
            # Positions before the middle digit
            for d in range(seq[pos - 1], 10):
                seq.append(d)
                generate_sequence(pos +1, k, seq)
                seq.pop()
        elif pos == k:
            # Middle digit, must be unique
            for d in range(seq[pos - 1], 10):
                if d not in seq:
                    seq.append(d)
                    # Build the mountain number
                    number_digits = seq + seq[k -1::-1]
                    number = int(''.join(map(str, number_digits)))
                    mountain_numbers.append(number)
                    seq.pop()

    generate_mountains()
    mountain_numbers.sort()

    import bisect

    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        line = sys.stdin.readline()
        while line.strip() == '':
            line = sys.stdin.readline()
        A_and_rest = line.strip().split()
        while len(A_and_rest) < 3:
            line = sys.stdin.readline()
            if not line:
                break
            A_and_rest += line.strip().split()
        A, B, M = map(int, A_and_rest)

        # Find the indices of mountain numbers within [A, B]
        left = bisect.bisect_left(mountain_numbers, A)
        right = bisect.bisect_right(mountain_numbers, B)

        count = 0
        for num in mountain_numbers[left:right]:
            if num % M == 0:
                count +=1
        print(f"Case #{case_num}: {count}")

threading.Thread(target=main).start()