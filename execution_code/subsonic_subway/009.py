import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr]); ptr +=1

    for test_case in range(1, T+1):
        N = int(input[ptr]); ptr +=1

        max_lower = 0.0
        min_upper = math.inf
        impossible = False

        for i in range(1, N+1):
            A = int(input[ptr]); ptr +=1
            B = int(input[ptr]); ptr +=1

            # Calculate the lower bound S >= i / B
            lower = i / B
            if lower > max_lower:
                max_lower = lower

            # Calculate the upper bound S <= i / A, if A >0
            if A >0:
                upper = i / A
                if upper < min_upper:
                    min_upper = upper
            else:
                # If A ==0, no upper bound from this station
                pass

        # After processing all stations, determine
        if max_lower <= min_upper:
            # Round to 10 decimal places to handle floating precision
            # But output as per problem's requirements
            print(f"Case #{test_case}: {max_lower}")
        else:
            print(f"Case #{test_case}: -1")

if __name__ == "__main__":
    main()