import sys
import bisect

def generate_non_decreasing(length, start, path, results):
    if len(path) == length:
        results.append(path.copy())
        return
    for digit in range(start, 10):
        path.append(digit)
        generate_non_decreasing(length, digit, path, results)
        path.pop()

def generate_non_increasing(length, max_digit, path, results):
    if len(path) == length:
        results.append(path.copy())
        return
    for digit in range(max_digit, 0, -1):
        path.append(digit)
        generate_non_increasing(length, digit, path, results)
        path.pop()

def main():
    import sys

    mountains = []

    for k in range(0, 10):
        length = 2 * k +1
        if length >19:
            continue
        first_part_results = []
        generate_non_decreasing(k +1, 1, [], first_part_results)
        for first_part in first_part_results:
            mid_digit = first_part[-1]
            if k ==0:
                # Single digit mountain
                number = 0
                for d in first_part:
                    number = number *10 + d
                mountains.append(number)
            else:
                if mid_digit <=1:
                    continue
                last_part_results = []
                generate_non_increasing(k, mid_digit -1, [], last_part_results)
                for last_part in last_part_results:
                    number = 0
                    for d in first_part:
                        number = number *10 + d
                    for d in last_part:
                        number = number *10 + d
                    mountains.append(number)

    # Sort the mountains list
    mountains.sort()

    # Read input
    input = sys.stdin.read().split()
    T = int(input[0])
    idx =1
    for test_case in range(1, T+1):
        A = int(input[idx])
        B = int(input[idx +1])
        M = int(input[idx +2])
        idx +=3
        # Find left and right indices
        left = bisect.bisect_left(mountains, A)
        right = bisect.bisect_right(mountains, B)
        sublist = mountains[left:right]
        count =0
        if M ==1:
            count = len(sublist)
        else:
            for num in sublist:
                if num % M ==0:
                    count +=1
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()