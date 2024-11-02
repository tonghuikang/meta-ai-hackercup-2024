import sys
import bisect

def generate_non_decreasing(length, min_digit, max_digit):
    sequences = []

    def backtrack(pos, current, last):
        if pos == length:
            sequences.append(list(current))
            return
        for d in range(last, max_digit +1):
            current.append(d)
            backtrack(pos +1, current, d)
            current.pop()

    backtrack(0, [], min_digit)
    return sequences

def generate_non_increasing(length, max_digit, min_digit):
    sequences = []

    def backtrack(pos, current, last):
        if pos == length:
            sequences.append(list(current))
            return
        for d in range(last, min_digit -1, -1):
            current.append(d)
            backtrack(pos +1, current, d)
            current.pop()

    backtrack(0, [], max_digit)
    return sequences

def generate_mountains():
    mountains = set()

    # Add single-digit mountains
    mountains.update(range(1,10))

    for total_digits in range(3, 20, 2):
        k = (total_digits -1)//2
        for Dmiddle in range(2, 10):
            # Generate all non-decreasing sequences for the first k digits
            left_sequences = generate_non_decreasing(k, 1, Dmiddle -1)
            # Generate all non-increasing sequences for the last k digits
            right_sequences = generate_non_increasing(k, Dmiddle -1, 1)
            for left in left_sequences:
                for right in right_sequences:
                    # Combine to form the full number
                    number_digits = left + [Dmiddle] + right
                    number = 0
                    for d in number_digits:
                        number = number *10 + d
                    mountains.add(number)
    return sorted(mountains)

def main():
    mountains = generate_mountains()
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        A, B, M = map(int, line.strip().split())
        # Find the left and right indices using bisect
        left_idx = bisect.bisect_left(mountains, A)
        right_idx = bisect.bisect_right(mountains, B)
        count = 0
        for m in mountains[left_idx:right_idx]:
            if m % M ==0:
                count +=1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()