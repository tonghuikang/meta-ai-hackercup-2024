import sys

def main():
    import sys
    import math

    import sys

    def input():
        return sys.stdin.read()

    data = sys.stdin.read().split()
    idx = 0
    T = int(data[idx]); idx += 1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        lower_S = 0.0
        upper_S = float('inf')
        for i in range(1, N+1):
            A_i = int(data[idx]); idx +=1
            B_i = int(data[idx]); idx +=1
            if B_i == 0:
                # Not possible since A_i < B_i and B_i >=0, but safe check
                constraints_possible = False
                break
            si_lower = i / B_i
            if si_lower > lower_S:
                lower_S = si_lower
            if A_i > 0:
                si_upper = i / A_i
                if si_upper < upper_S:
                    upper_S = si_upper
        # After processing all stations
        # Check feasibility
        feasible = True
        if lower_S > upper_S + 1e-12:  # Adding small epsilon to account for floating point
            feasible = False
        if feasible:
            # To meet the required precision, format the speed with enough decimal places
            # But the problem allows any format as long as it's within error
            # So we can print lower_S directly
            print(f"Case #{test_case}: {lower_S}")
        else:
            print(f"Case #{test_case}: -1")

if __name__ == "__main__":
    main()