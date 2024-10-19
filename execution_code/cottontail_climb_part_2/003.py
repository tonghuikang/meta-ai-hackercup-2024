import sys
import bisect

def generate_mountain_numbers():
    mountains = []

    def backtrack(prefix, length, k, is_increasing, last_digit):
        if len(prefix) == length:
            if k > 0:
                # Check the peak uniqueness
                peak = prefix[k]
                if prefix[k-1] < peak and prefix[k] > prefix[k+1]:
                    number = int(''.join(map(str, prefix)))
                    mountains.append(number)
            else:
                # Single digit, always a mountain
                number = int(''.join(map(str, prefix)))
                mountains.append(number)
            return

        if len(prefix) < k +1:
            # Build the increasing part
            for d in range(last_digit, 10):
                if d == 0:
                    continue
                prefix.append(d)
                backtrack(prefix, length, k, True, d)
                prefix.pop()
        else:
            # Build the decreasing part
            for d in range(1, prefix[k] +1):
                prefix.append(d)
                backtrack(prefix, length, k, False, d)
                prefix.pop()

    # Generate for different k
    for k in range(0, 9):
        length = 2 * k +1
        if length ==1:
            for d in range(1,10):
                mountains.append(d)
            continue
        backtrack([], length, k, True, 1)
    mountains = sorted(set(mountains))
    return mountains

def main():
    mountains = generate_mountain_numbers()
    T = int(sys.stdin.readline())
    for case in range(1, T+1):
        A, B, M = map(int, sys.stdin.readline().split())
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        count = 0
        for num in mountains[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{case}: {count}")

if __name__ == "__main__":
    main()