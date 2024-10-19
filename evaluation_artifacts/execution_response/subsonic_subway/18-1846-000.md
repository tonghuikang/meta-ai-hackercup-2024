**Key Findings:**

1. **Understanding the Delivery Constraints:**
   - For each station \( i \), Sonic must arrive within the time window \([A_i, B_i]\).
   - Sonic's constant speed \( S \) must satisfy \( A_i \leq \frac{i}{S} \leq B_i \) for all stations.

2. **Deriving Speed Bounds:**
   - Rearranging the inequality gives two constraints:
     - \( S \geq \frac{i}{B_i} \) (to arrive before the window closes).
     - \( S \leq \frac{i}{A_i} \) if \( A_i > 0 \) (to not arrive after the window opens).
   - If \( A_i = 0 \), there's no upper bound on \( S \) from that station.

3. **Determining Feasibility:**
   - To satisfy all stations, \( S \) must be at least the maximum of \( \frac{i}{B_i} \) across all stations.
   - Simultaneously, \( S \) must be no greater than the minimum of \( \frac{i}{A_i} \) across all stations where \( A_i > 0 \).
   - If the maximum lower bound exceeds the minimum upper bound, it's impossible to find such a speed \( S \).

4. **Edge Cases:**
   - Stations with \( A_i = 0 \) require careful handling, as they impose no upper bound on \( S \).
   - If all stations have \( A_i = 0 \), any \( S \) greater than or equal to the maximum \( \frac{i}{B_i} \) is acceptable.

5. **Implementation Considerations:**
   - Given the large input size, efficient input parsing is crucial. Utilizing buffered reading methods in Python can help manage this.
   - Floating-point precision should be handled carefully to ensure the output meets the required accuracy.

**Python Code:**

```python
import sys

def solve():
    import sys
    import math

    import sys

    def readints():
        import sys
        return list(map(int, sys.stdin.read().split()))

    data = readints()
    idx = 0
    T = data[idx]
    idx +=1
    for test_case in range(1, T+1):
        N = data[idx]
        idx +=1
        max_lower = 0.0
        min_upper = float('inf')
        for i in range(1, N+1):
            A_i = data[idx]
            B_i = data[idx+1]
            idx +=2
            # Compute i / B_i
            if B_i ==0:
                # If B_i is 0, Sonic must reach exactly at t=0, which is impossible unless i=0
                # But i >=1, so no solution
                max_lower = float('inf')
                # No need to proceed further
                break
            t_lower = i / B_i
            max_lower = max(max_lower, t_lower)
            if A_i >0:
                t_upper = i / A_i
                min_upper = min(min_upper, t_upper)
            # If A_i ==0, no upper bound from this station
        # After all stations
        if max_lower <= min_upper:
            if math.isinf(max_lower):
                # No solution
                result = -1
            else:
                # Output max_lower with up to 7 decimal places to ensure required precision
                result = max_lower
        else:
            result = -1
        if result == -1:
            print(f"Case #{test_case}: -1")
        else:
            # To ensure floating point precision up to 1e-6, format with 10 decimal places
            print(f"Case #{test_case}: {result:.10f}".rstrip('0').rstrip('.'))
```