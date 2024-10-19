import sys
import bisect

def generate_mountains():
    mountains = []
    # Generate mountains for all possible odd lengths up to 19 digits
    for n in range(1, 20, 2):
        k = (n - 1) // 2
        def backtrack(left, pos, current, last_digit):
            if pos == k + 1:
                # Now, determine the middle digit
                # It should be greater or equal to the last digit in left
                # Then, generate the right part which is non-increasing starting from middle
                for middle_digit in range(1, 10):
                    # Middle digit must be equal to current[-1]
                    if middle_digit != current[-1]:
                        continue
                    # Check uniqueness later
                    # Now generate the right part
                    def backtrack_right(right, pos_right, current_right, last_right_digit):
                        if pos_right == n:
                            # Now, build the number and check the uniqueness of the middle digit
                            number = int(''.join(map(str, current_right)))
                            if str(current_right[k]).count(str(current_right[k])) == 1:
                                mountains.append(number)
                            return
                        for d in range(1, last_right_digit + 1):
                            current_right.append(d)
                            backtrack_right(right, pos_right + 1, current_right, d)
                            current_right.pop()
                    current_right = list(current)
                    backtrack_right(current_right, k + 1, current_right, current[-1])
                return
            for d in range(last_digit, 10):
                current.append(d)
                backtrack(left, pos + 1, current, d)
                current.pop()
        backtrack([], 0, [], 1)
    # However, the above approach is not efficient. Instead, a better method:
    mountains = []
    from itertools import combinations_with_replacement, product
    for n in range(1, 20, 2):
        k = (n - 1) // 2
        # Generate all non-decreasing sequences of length k+1
        def generate_non_decreasing(length):
            if length == 0:
                return []
            if length == 1:
                return [[d] for d in range(1,10)]
            sequences = []
            def helper(seq, last, l):
                if l == length:
                    sequences.append(seq.copy())
                    return
                for d in range(last, 10):
                    seq.append(d)
                    helper(seq, d, l+1)
                    seq.pop()
            helper([], 1, 0)
            return sequences

        left_sequences = generate_non_decreasing(k+1)
        for left in left_sequences:
            middle = left[-1]
            # Now, generate non-increasing sequences of length k+1 starting with middle
            def generate_non_increasing(length, start):
                if length == 0:
                    return []
                if length == 1:
                    return [[d] for d in range(1, start+1)]
                sequences = []
                def helper(seq, last, l):
                    if l == length:
                        sequences.append(seq.copy())
                        return
                    for d in range(1, last+1):
                        seq.append(d)
                        helper(seq, d, l+1)
                        seq.pop()
                helper([], start, 0)
                return sequences
            right_sequences = generate_non_increasing(k+1, middle)
            for right in right_sequences:
                # Now, combine left and right, ensuring middle digit is unique
                full_digits = left + right[1:]
                # Check if the middle digit occurs exactly once
                if full_digits.count(middle) == 1:
                    # Convert to integer
                    number = int(''.join(map(str, full_digits)))
                    mountains.append(number)
    mountains = sorted(set(mountains))
    return mountains

def main():
    import sys
    import bisect
    mountains = generate_mountains()
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        A, B, M = map(int, sys.stdin.readline().split())
        # Find the indices where mountains >= A and <= B
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M == 0:
                count += 1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()