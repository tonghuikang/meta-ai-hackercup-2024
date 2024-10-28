import sys
import bisect

def generate_mountain_numbers():
    mountains = []

    def backtrack(length, pos, current, prev, phase, central_digit, k):
        if pos == length:
            num = int(''.join(map(str, current)))
            mountains.append(num)
            return

        if phase == "increasing":
            if pos == k:
                # At central digit, it must be greater than previous
                for d in range(prev + 1, 10):
                    current.append(d)
                    backtrack(length, pos + 1, current, d, "decreasing", d, k)
                    current.pop()
            else:
                # Non-decreasing before central digit
                for d in range(prev, 10):
                    current.append(d)
                    backtrack(length, pos + 1, current, d, "increasing", central_digit, k)
                    current.pop()
        elif phase == "decreasing":
            # After central digit, non-increasing
            for d in range(1, central_digit):
                # Middle digit must be greater than next digit
                if d > current[-1]:
                    continue
                current.append(d)
                backtrack(length, pos + 1, current, d, "decreasing", central_digit, k)
                current.pop()

    # Updated backtrack function to correctly handle decreasing phase
    def backtrack_correct(length, pos, current, prev, phase, central_digit, k):
        if pos == length:
            num = int(''.join(map(str, current)))
            mountains.append(num)
            return
        if phase == "increasing":
            if pos == k:
                # At central digit, it must be greater than previous
                for d in range(prev + 1, 10):
                    current.append(d)
                    backtrack_correct(length, pos + 1, current, d, "decreasing", d, k)
                    current.pop()
            else:
                # Non-decreasing before central digit
                for d in range(prev, 10):
                    current.append(d)
                    backtrack_correct(length, pos + 1, current, d, "increasing", central_digit, k)
                    current.pop()
        elif phase == "decreasing":
            # After central digit, non-increasing
            for d in range(1, central_digit +1):
                if pos > k:
                    # Ensure non-increasing
                    if d > prev:
                        continue
                current.append(d)
                backtrack_correct(length, pos + 1, current, d, "decreasing", central_digit, k)
                current.pop()

    for L in range(1, 20, 2):  # Odd lengths from 1 to 19
        k = (L -1)//2
        def helper(pos, current, phase, prev, central_digit):
            if pos == L:
                num = int(''.join(map(str, current)))
                mountains.append(num)
                return
            if phase == "increasing":
                if pos == k:
                    # Assign central digit, must be greater than previous
                    for d in range(prev +1, 10):
                        current.append(d)
                        helper(pos +1, current, "decreasing", d, d)
                        current.pop()
                else:
                    # Assign non-decreasing digits before central
                    for d in range(prev, 10):
                        current.append(d)
                        helper(pos +1, current, "increasing", d, central_digit)
                        current.pop()
            elif phase == "decreasing":
                # Assign non-increasing digits after central
                for d in range(1, central_digit):
                    if d > prev:
                        continue
                    current.append(d)
                    helper(pos +1, current, "decreasing", d, central_digit)
                    current.pop()
        # Initialize the first digit from 1 to 9
        for first_d in range(1, 10):
            helper(1, [first_d], "increasing", first_d, None)

    return sorted(mountains)

def main():
    import sys
    import threading
    def run():
        mountains = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for tc in range(1, T+1):
            A_str, B_str, M_str = sys.stdin.readline().strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            # Find the range in mountains
            left = bisect.bisect_left(mountains, A)
            right = bisect.bisect_right(mountains, B)
            count = 0
            if M ==1:
                count = right - left
            else:
                for num in mountains[left:right]:
                    if num % M ==0:
                        count +=1
            print(f"Case #{tc}: {count}")
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()