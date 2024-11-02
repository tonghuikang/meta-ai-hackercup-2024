import sys
import bisect

def generate_mountain_numbers():
    mountain_numbers = []

    def generate_prefix(k_plus_1, current, last_digit):
        if len(current) == k_plus_1:
            # Ensure the last digit is greater than the previous one
            if len(current) >= 2 and current[-1] <= current[-2]:
                return []
            return [current.copy()]
        sequences = []
        start = last_digit if len(current) > 0 else 1
        for digit in range(start, 10):
            if len(current) >=1 and digit < current[-1]:
                continue
            current.append(digit)
            sequences.extend(generate_prefix(k_plus_1, current, digit))
            current.pop()
        return sequences

    def generate_prefixes(k_plus_1):
        def backtrack(pos, current, last_digit):
            if pos == k_plus_1:
                if k_plus_1 ==1 or current[-1] > current[-2]:
                    prefixes.append(current.copy())
                return
            start = last_digit if pos >0 else 1
            for digit in range(start, 10):
                current.append(digit)
                if pos == k_plus_1 -1:
                    if k_plus_1 ==1 or digit > current[-2]:
                        backtrack(pos +1, current, digit)
                else:
                    backtrack(pos +1, current, digit)
                current.pop()

        prefixes = []
        backtrack(0, [], 1)
        return prefixes

    def generate_suffix(k, middle_digit):
        results = []

        def backtrack(pos, current, last_digit):
            if pos == k:
                results.append(current.copy())
                return
            for digit in range(1, last_digit +1):
                current.append(digit)
                backtrack(pos +1, current, digit)
                current.pop()

        backtrack(0, [], middle_digit -1)
        return results

    for d in range(1, 20, 2):
        k = (d -1)//2
        if d ==1:
            for digit in range(1,10):
                mountain_numbers.append(digit)
            continue
        prefixes = generate_prefixes(k +1)
        for prefix in prefixes:
            middle_digit = prefix[-1]
            suffix_sequences = []

            def backtrack_suffix(pos, current, last_digit):
                if pos == k:
                    suffix_sequences.append(current.copy())
                    return
                for digit in range(1, last_digit +1):
                    current.append(digit)
                    backtrack_suffix(pos +1, current, digit)
                    current.pop()

            # Suffix must be non-increasing starting with digit < middle_digit
            def generate_non_increasing(pos, current, last_digit):
                if pos == k:
                    suffix_sequences.append(current.copy())
                    return
                for digit in range(1, last_digit +1):
                    current.append(digit)
                    generate_non_increasing(pos +1, current, digit)
                    current.pop()

            suffix_sequences = []
            generate_non_increasing(0, [], middle_digit -1)
            for suffix in suffix_sequences:
                number = 0
                for digit in prefix:
                    number = number *10 + digit
                for digit in suffix:
                    number = number *10 + digit
                mountain_numbers.append(number)
    mountain_numbers.sort()
    return mountain_numbers

def main():
    import sys
    import threading
    def run():
        mountain_numbers = generate_mountain_numbers()
        T = int(sys.stdin.readline())
        for tc in range(1, T+1):
            A_str, B_str, M_str = sys.stdin.readline().strip().split()
            A = int(A_str)
            B = int(B_str)
            M = int(M_str)
            left = bisect.bisect_left(mountain_numbers, A)
            right = bisect.bisect_right(mountain_numbers, B)
            count = 0
            for num in mountain_numbers[left:right]:
                if num % M ==0:
                    count +=1
            print(f"Case #{tc}: {count}")
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()