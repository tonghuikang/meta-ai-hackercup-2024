**Key Findings:**

To solve the problem, we need to determine the minimum constant speed `v` such that Sonic can deliver sandwiches to all stations within their respective delivery windows `[A_i, B_i]`. Here's a step-by-step breakdown of the approach:

1. **Time Calculation:**
   - For each station `i`, located `i` miles away, the time `t_i` taken by Sonic to reach it is `t_i = i / v`.
   - This time must satisfy the delivery window: `A_i ≤ t_i ≤ B_i`.

2. **Deriving Speed Constraints:**
   - From the inequality `A_i ≤ i / v ≤ B_i`, we can rearrange to obtain constraints on the speed `v`:
     - Lower bound for `v`: `v ≥ i / B_i`.
     - Upper bound for `v`: `v ≤ i / A_i` (only if `A_i > 0`).

3. **Determining Feasibility:**
   - The minimum possible speed `v` must be at least the maximum of all `i / B_i` across all stations.
   - Additionally, for all stations where `A_i > 0`, this minimum speed must not exceed `i / A_i`.
   - If these conditions are met, the minimum speed is the maximum `i / B_i`. Otherwise, it's impossible to satisfy all delivery windows, and we output `-1`.

4. **Edge Cases:**
   - Stations with `A_i = 0` do not impose an upper bound on the speed.
   - All computations should handle floating-point precision accurately.

The implementation efficiently processes each test case by iterating through the stations once to determine the necessary bounds and then checks for feasibility.

```python
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
```