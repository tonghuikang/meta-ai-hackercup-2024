import sys
import bisect

def generate_mountain_numbers():
    mountains = []

    def build_mountain(length, current_num, pos, increasing):
        if pos == length:
            mountains.append(int(current_num))
            return
        if pos == 0:
            for d in '123456789':
                build_mountain(length, current_num + d, pos + 1, True)
        else:
            if pos < (length // 2) + 1:
                # Increasing part
                last_digit = current_num[-1]
                for d in range(int(last_digit), 10):
                    if d == 0:
                        continue
                    build_mountain(length, current_num + str(d), pos + 1, True)
            else:
                # Decreasing part
                last_digit = current_num[-1]
                for d in range(int(last_digit), 0, -1):
                    build_mountain(length, current_num + str(d), pos + 1, False)

    for k in range(0, 10):  # because 2*9+1=19
        length = 2 * k + 1
        build_mountain(length, '', 0, True)

    return sorted(mountains)

def main():
    mountains = generate_mountain_numbers()
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for tc in range(1, T + 1):
        A = int(input[idx])
        B = int(input[idx + 1])
        M = int(input[idx + 2])
        idx += 3
        # Find mountains in [A, B]
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M == 0:
                count += 1
        print(f"Case #{tc}: {count}")

if __name__ == "__main__":
    main()