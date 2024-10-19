import sys
import bisect

def generate_non_decreasing_sequences(k, max_digit):
    if k == 0:
        return [[]]
    sequences = [[]]
    for _ in range(k):
        new_sequences = []
        for seq in sequences:
            start = seq[-1] if seq else 1
            for digit in range(start, max_digit +1):
                new_sequences.append(seq + [digit])
        sequences = new_sequences
    return sequences

def generate_non_increasing_sequences(k, max_digit):
    if k == 0:
        return [[]]
    sequences = [[]]
    for _ in range(k):
        new_sequences = []
        for seq in sequences:
            start = seq[-1] if seq else max_digit
            for digit in range(1, start +1):
                new_sequences.append(seq + [digit])
        sequences = new_sequences
    return sequences

def generate_mountain_numbers():
    mountain_numbers = []
    # Lengths: 1,3,5,...,19
    for L in range(1, 20, 2):
        k = (L -1)//2
        for d in range(1,10):
            if k ==0:
                # Single-digit mountains
                mountain_numbers.append(d)
            else:
                if d-1 <1:
                    continue
                # Generate first k digits: non-decreasing, digits 1 to d-1
                first_seqs = generate_non_decreasing_sequences(k, d-1)
                if not first_seqs:
                    continue
                # Generate last k digits: non-increasing, digits 1 to d-1
                last_seqs = generate_non_increasing_sequences(k, d-1)
                if not last_seqs:
                    continue
                # Combine
                for first in first_seqs:
                    for last in last_seqs:
                        number_digits = first + [d] + last
                        number = int(''.join(map(str, number_digits)))
                        mountain_numbers.append(number)
    mountain_numbers = sorted(mountain_numbers)
    return mountain_numbers

def main():
    import sys
    import threading

    def run():
        mountain_numbers = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for case in range(1, T+1):
            A_str, B_str, M_str = sys.stdin.readline().strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find left and right indices
            left = bisect.bisect_left(mountain_numbers, A)
            right = bisect.bisect_right(mountain_numbers, B)
            count = 0
            # Iterate through the relevant slice
            for num in mountain_numbers[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{case}: {count}")
        
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()