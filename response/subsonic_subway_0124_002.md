**Key Findings:**

To determine the minimum constant speed `v` that Sonic needs to maintain to deliver sandwiches to all stations within their respective time windows `[A_i, B_i]`:

1. **Arrival Time Constraint:** For each station `i`, Sonic's arrival time is `i / v`. This must satisfy `A_i ≤ i / v ≤ B_i`.
   
2. **Speed Constraints:**
   - From `A_i ≤ i / v`, we derive `v ≥ i / B_i` for each station.
   - From `i / v ≤ B_i`, we derive `v ≤ i / A_i` for each station where `A_i > 0`. If `A_i = 0`, there is no upper bound on `v`.

3. **Overall Conditions:**
   - The minimum required speed is the maximum of all `i / B_i`.
   - The upper bound on speed is the minimum of all `i / A_i` for stations where `A_i > 0`. If any `A_i` is `0`, the upper bound remains infinity.
   - If the maximum lower bound (`max_lower_v`) is less than or equal to the minimum upper bound (`min_upper_v`), the minimum required speed is `max_lower_v`. Otherwise, it's impossible to satisfy all constraints, and the answer is `-1`.

4. **Edge Cases:**
   - Handle `A_i = 0` appropriately by not constraining the upper bound for those stations.
   - Ensure precision when dealing with floating-point calculations to meet the required error margins.

**Python Code:**

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
        max_lower_v = 0.0
        min_upper_v = math.inf
        for i in range(1, N+1):
            A_i = int(input[ptr])
            B_i = int(input[ptr+1])
            ptr +=2
            lower_v_i = i / B_i
            if lower_v_i > max_lower_v:
                max_lower_v = lower_v_i
            if A_i >0:
                upper_v_i = i / A_i
                if upper_v_i < min_upper_v:
                    min_upper_v = upper_v_i
        if max_lower_v <= min_upper_v:
            # To ensure enough precision, format with 10 decimal places
            print(f"Case #{tc}: {max_lower_v:.10f}".rstrip('0').rstrip('.') if '.' in f"{max_lower_v:.10f}" else f"{max_lower_v:.10f}")
        else:
            print(f"Case #{tc}: -1")

if __name__ == "__main__":
    main()
```