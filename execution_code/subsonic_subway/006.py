import sys
import math

def main():
    import sys, math
    from sys import stdin

    data = sys.stdin.read().split()
    it = iter(data)
    try:
        T = int(next(it))
    except StopIteration:
        T = 0

    results = []

    for test_case in range(1, T+1):
        try:
            N = int(next(it))
        except StopIteration:
            N = 0

        v_min = 0.0
        v_max = math.inf

        for i in range(1, N+1):
            try:
                A_i = int(next(it))
                B_i = int(next(it))
            except StopIteration:
                A_i = 0
                B_i = 1  # Assign default to avoid ZeroDivisionError, though per constraints should not happen

            # Calculate lower bound
            if B_i == 0:
                # If B_i is 0, cannot deliver, as t_i = i / v cannot be <=0
                v_min = math.inf
            else:
                lower_bound = i / B_i
                if lower_bound > v_min:
                    v_min = lower_bound

            # Calculate upper bound
            if A_i > 0:
                upper_bound = i / A_i
                if upper_bound < v_max:
                    v_max = upper_bound
            # If A_i ==0, no action needed for v_max

        # Check feasibility
        if v_min <= v_max:
            # Format v_min with up to 10 decimal places, remove trailing zeros and dot if needed
            formatted_v = "{0:.10f}".format(v_min).rstrip('0').rstrip('.') if '.' in "{0:.10f}".format(v_min) else "{0:.10f}".format(v_min)
            results.append(f"Case #{test_case}: {formatted_v}")
        else:
            results.append(f"Case #{test_case}: -1")

    print("\n".join(results))

if __name__ == "__main__":
    main()