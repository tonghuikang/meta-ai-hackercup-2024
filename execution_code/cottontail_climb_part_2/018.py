import sys
import bisect

def generate_mountain_numbers():
    mountains = set()

    def recurse(k, current, last_digit, used_digits, pos, total_len):
        if pos == k:
            # Choosing the middle digit
            for mid_digit in range(1, 10):
                if mid_digit not in used_digits:
                    # Now build the decreasing part
                    def build_decreasing(current_decr, pos_decr, last_decr):
                        if pos_decr == k:
                            number = ''.join(map(str, current)) + str(mid_digit) + ''.join(map(str, current_decr))
                            mountains.add(int(number))
                            return
                        for d in range(1, last_decr +1):
                            if d != mid_digit:
                                current_decr.append(d)
                                build_decreasing(current_decr, pos_decr +1, d)
                                current_decr.pop()
                    build_decreasing([],0, mid_digit)
        else:
            for d in range(last_digit, 10):
                if d not in used_digits:
                    current.append(d)
                    recurse(k, current, d, used_digits | {d}, pos +1, total_len)
                    current.pop()

    # For k from 0 to 9 (2k+1 from 1 to19)
    for k in range(0, 10):
        total_len = 2 * k +1
        recurse(k, [], 1, set(), 0, total_len)

    # Also need to include numbers where the middle digit may repeat in sequences, but is unique in the entire number
    # For example, 1223221: '3' appears once, others can repeat
    # Modify the above to allow repetition in the first k digits as long as they don't include the middle digit
    mountains = set()

    def build_mountains(k):
        # Build first k +1 digits (positions 0 to k)
        def build_first_half(pos, current, last_digit, used_digits):
            if pos == k +1:
                # The current list has k +1 digits, last digit is current[-1]
                # The middle digit is current[-1], which must appear only once
                # So, the first k digits must not include the middle digit
                if current[:-1].count(current[-1]) > 0:
                    return
                mid_digit = current[-1]
                # Now build the last k digits, which must be non-increasing and not include mid_digit
                def build_second_half(pos2, second_half, last_decr):
                    if pos2 == k:
                        number = int(''.join(map(str, current + second_half)))
                        mountains.add(number)
                        return
                    for d in range(1, last_decr +1):
                        if d != mid_digit:
                            second_half.append(d)
                            build_second_half(pos2 +1, second_half, d)
                            second_half.pop()
                build_second_half(0, [], mid_digit)
                return
            # Choose next digit >= last_digit
            for d in range(last_digit, 10):
                current.append(d)
                build_first_half(pos +1, current, d, used_digits | {d})
                current.pop()

        build_first_half(0, [], 1, set())

    for k in range(0, 10):
        build_mountains(k)

    # Single-digit mountain numbers:
    if 1 >=0:
        for d in range(1,10):
            mountains.add(d)

    return sorted(mountains)

def main():
    mountains = generate_mountain_numbers()
    # Read input
    T = int(sys.stdin.readline())
    for tc in range(1, T +1):
        A_str, B_str, M_str = sys.stdin.readline().strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        # Binary search to find range
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{tc}: {count}")

if __name__ == "__main__":
    main()