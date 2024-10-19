import sys
import bisect

def generate_mountain_numbers():
    mountains = []

    def recurse(prefix, length, is_increasing, last_digit, k, middle_index, digit_counts):
        if len(prefix) == length:
            mountains.append(int(prefix))
            return

        for digit in range(1, 10):
            if is_increasing:
                if digit < last_digit:
                    continue
            else:
                if digit > last_digit:
                    continue
            # Check uniqueness for middle digit
            if len(prefix) == middle_index:
                if digit_counts.get(digit, 0) >=1:
                    continue
                new_counts = digit_counts.copy()
                new_counts[digit] = new_counts.get(digit,0) +1
            else:
                new_counts = digit_counts.copy()
                new_counts[digit] = new_counts.get(digit,0) +1

            recurse(prefix + str(digit), length, is_increasing, digit, k, middle_index, new_counts)

    # Generate mountain numbers with odd length from 1 to 17
    for k in range(0, 9):  # 2k+1 <=17 when k<=8
        length = 2*k +1
        if length ==1:
            for digit in range(1,10):
                mountains.append(digit)
            continue
        middle_index = k
        # Build first half including middle digit
        def build_first_half(current, pos, last, digit_counts):
            if pos == middle_index:
                # Middle digit, needs to be unique
                for digit in range(last,10):
                    if digit_counts.get(digit,0) ==0:
                        new_counts = digit_counts.copy()
                        new_counts[digit] =1
                        build_second_half(current + [digit], pos+1, digit, new_counts)
                return
            for digit in range(last,10):
                new_counts = digit_counts.copy()
                new_counts[digit] = new_counts.get(digit,0) +1
                build_first_half(current + [digit], pos+1, digit, new_counts)

        def build_second_half(current, pos, last, digit_counts):
            if pos == length:
                # Now, reconstruct the number
                num = int(''.join(map(str, current)))
                mountains.append(num)
                return
            for digit in range(1, last+1):
                if digit_counts.get(digit,0) >=1 and pos != middle_index:
                    continue
                new_counts = digit_counts.copy()
                new_counts[digit] = new_counts.get(digit,0) +1
                build_second_half(current + [digit], pos+1, digit, new_counts)

        build_first_half([], 0, 1, {})

    mountains = sorted(set(mountains))
    return mountains

def main():
    mountains = generate_mountain_numbers()
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        A_str, B_str, M_str = sys.stdin.readline().strip().split()
        A = int(A_str)
        B = int(B_str)
        M = int(M_str)
        # Find left and right indices
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{tc}: {count}")

if __name__ == "__main__":
    main()