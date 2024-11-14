import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr +=1
    for tc in range(1, T+1):
        N = int(input[ptr])
        ptr +=1
        max_lower = 0.0
        min_upper = math.inf
        for i in range(1, N+1):
            A_i = int(input[ptr])
            B_i = int(input[ptr+1])
            ptr +=2
            lower = i / B_i
            if lower > max_lower:
                max_lower = lower
            if A_i >0:
                upper = i / A_i
                if upper < min_upper:
                    min_upper = upper
        if max_lower <= min_upper:
            print(f"Case #{tc}: {max_lower}")
        else:
            print(f"Case #{tc}: -1")

if __name__ == "__main__":
    main()