import sys
import bisect

def generate_mountain_numbers():
    mountain_numbers = set()
    
    for total_digits in range(1, 20, 2):  # 1,3,5,...,19
        k = (total_digits -1)//2
        if k ==0:
            # Single-digit numbers
            for d in range(1,10):
                mountain_numbers.add(d)
            continue
        # For k >=1
        # Generate left part: k digits, non-decreasing, digits 1-9
        # Generate right part: k digits, non-increasing, digits <= peak
        def backtrack_left(pos, current, last_digit):
            if pos == k:
                return [current]
            nums = []
            for d in range(last_digit, 10):
                nums += backtrack_left(pos+1, current*10 + d, d)
            return nums
        
        left_parts = backtrack_left(0, 0,1)
        # For each left part, choose peak digit > last digit of left
        for left in left_parts:
            last_digit = left %10
            for peak in range(last_digit +1,10):
                # Now generate right part: k digits, non-increasing, <= peak
                def backtrack_right(pos, current, last_digit_right):
                    if pos ==k:
                        return [current]
                    nums = []
                    for d in range(1, last_digit_right +1):
                        nums += backtrack_right(pos+1, current*10 + d, d)
                    return nums
                right_parts = backtrack_right(0,0,peak)
                for right in right_parts:
                    mountain = left * (10**(k+1)) + peak * (10**k) + right
                    mountain_numbers.add(mountain)
    mountain_list = sorted(mountain_numbers)
    return mountain_list

def main():
    mountain_list = generate_mountain_numbers()
    input = sys.stdin.read().split()
    T = int(input[0])
    ptr =1
    for test_case in range(1, T+1):
        A = int(input[ptr])
        B = int(input[ptr+1])
        M = int(input[ptr+2])
        ptr +=3
        # Find left and right indices
        left_idx = bisect.bisect_left(mountain_list, A)
        right_idx = bisect.bisect_right(mountain_list, B)
        count =0
        for num in mountain_list[left_idx:right_idx]:
            if num % M ==0:
                count +=1
        print(f"Case #{test_case}: {count}")

if __name__ == "__main__":
    main()