import sys
import bisect

def generate_mountain_numbers():
    mountains = []

    def backtrack(k, pos, current, last, unique_mid, digits_set, mid_digit, n):
        if pos == n:
            num = int(''.join(map(str, current)))
            mountains.append(num)
            return
        if pos == k:
            # Middle digit, must be unique
            for d in range(1, 10):
                if d not in digits_set:
                    current.append(d)
                    backtrack(k, pos + 1, current, d, True, digits_set | {d}, d, n)
                    current.pop()
        elif pos < k:
            for d in range(last, 10):
                if d not in digits_set:
                    current.append(d)
                    backtrack(k, pos + 1, current, d, unique_mid, digits_set | {d}, mid_digit, n)
                    current.pop()
        else:
            # After middle digit, non-increasing
            for d in range(current[k] if pos == k +1 else current[-1], 0, -1):
                if d not in digits_set:
                    current.append(d)
                    backtrack(k, pos + 1, current, d, unique_mid, digits_set | {d}, mid_digit, n)
                    current.pop()

    for n in range(1, 20, 2):
        k = n // 2
        backtrack(k, 0, [], 0, False, set(), 0, n)

    mountains.sort()
    return mountains

def main():
    mountains = generate_mountain_numbers()
    T = int(sys.stdin.readline())
    for case in range(1, T +1):
        A, B, M = map(int, sys.stdin.readline().split())
        # Find the range in mountains
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()