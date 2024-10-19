import sys
from bisect import bisect_left, bisect_right

def generate_mountain_numbers():
    mountain_numbers = []
    
    # Possible lengths: 1,3,5,...,19
    for length in range(1, 20, 2):
        k = (length -1) // 2
        # Build first k+1 digits (non-decreasing)
        def build_first_digits(pos, current, last_digit):
            if pos == k+1:
                # Now build last k digits (non-increasing)
                # The middle digit is current[-1]
                middle_digit = current[-1]
                def build_last_digits(last_pos, last_current, last_dec_digit):
                    if last_pos == length:
                        # Ensure the middle digit is unique
                        if last_current.count(middle_digit) == 1:
                            number = int(''.join(map(str, last_current)))
                            mountain_numbers.append(number)
                        return
                    next_digit_start = 1
                    # To maintain non-increasing
                    for d in range(1, last_dec_digit+1):
                        build_last_digits(last_pos+1, last_current + [d], d)
                build_last_digits(k+1, current.copy(), middle_digit)
                return
            for d in range(last_digit,10):
                build_first_digits(pos+1, current + [d], d)
        
        build_first_digits(0, [], 1)
    
    mountain_numbers.sort()
    return mountain_numbers

def main():
    mountain_numbers = generate_mountain_numbers()
    input = sys.stdin.read().split()
    T = int(input[0])
    ptr = 1
    for test_case in range(1, T+1):
        A = int(input[ptr])
        B = int(input[ptr+1])
        M = int(input[ptr+2])
        ptr +=3
        # Find mountain numbers in [A,B]
        left = bisect_left(mountain_numbers, A)
        right = bisect_right(mountain_numbers, B)
        count = 0
        for num in mountain_numbers[left:right]:
            if num % M ==0:
                count +=1
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()