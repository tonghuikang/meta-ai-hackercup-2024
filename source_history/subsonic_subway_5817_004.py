import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx += 1
    for tc in range(1, T + 1):
        N = int(input[idx])
        idx += 1
        max_i_over_Bi = 0.0
        min_i_over_Ai = math.inf
        possible = True
        for i in range(1, N + 1):
            Ai = float(input[idx])
            Bi = float(input[idx + 1])
            idx += 2
            if Bi == 0:
                possible = False
                continue
            current_max = i / Bi
            if current_max > max_i_over_Bi:
                max_i_over_Bi = current_max
            if Ai == 0:
                current_min = math.inf
            else:
                current_min = i / Ai
            if current_min < min_i_over_Ai:
                min_i_over_Ai = current_min
        if not possible:
            result = -1
        elif max_i_over_Bi <= min_i_over_Ai:
            result = max_i_over_Bi
        else:
            result = -1
        if result == -1:
            print(f"Case #{tc}: -1")
        else:
            # To ensure precision up to 1e-7 to handle rounding
            print(f"Case #{tc}: {result:.10f}".rstrip('0').rstrip('.'))
            

if __name__ == "__main__":
    main()