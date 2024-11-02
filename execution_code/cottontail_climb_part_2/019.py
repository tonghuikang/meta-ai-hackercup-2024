import sys
import bisect

def generate_mountain_numbers():
    mountains = []

    def build_number(left, peak, right_length):
        number = ''.join(map(str, left)) + str(peak) + ''.join(map(str, left[::-1]))
        mountains.append(int(number))

    def dfs(length, current, increasing, peak_set):
        if len(current) == length:
            if peak_set:
                number = int(''.join(map(str, current)))
                mountains.append(number)
            return
        start_digit = 1 if len(current) == 0 else current[-1] if increasing else 1
        for digit in range(1, 10):
            if len(current) < (length // 2) + 1:
                if len(current) == 0 or digit >= current[-1]:
                    dfs(length, current + [digit], True, False)
            else:
                if digit <= current[-1]:
                    if not peak_set:
                        # Ensure the peak is unique
                        if digit < current[-1]:
                            dfs(length, current + [digit], False, True)
                    else:
                        if digit <= current[-1]:
                            dfs(length, current + [digit], False, peak_set)
    
    for total_length in range(1, 20, 2):
        dfs(total_length, [], True, False)
    
    mountains = sorted(list(set(mountains)))
    return mountains

def main():
    mountains = generate_mountain_numbers()
    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        A, B, M = map(int, sys.stdin.readline().split())
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M == 0:
                count += 1
        print(f"Case #{tc}: {count}")

if __name__ == "__main__":
    main()