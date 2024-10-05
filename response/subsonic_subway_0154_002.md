**Key Findings:**

To determine the minimum constant speed \( S \) that allows Sonic to deliver sandwiches to all stations within their respective delivery windows, we analyze the constraints for each station:

1. **Arrival Time Constraint:** For each station \( i \), Sonic must arrive within the time window \([A_i, B_i]\). Since Sonic's speed is constant, his arrival time at station \( i \) is \( t_i = \frac{i}{S} \).

2. **Speed Constraints:**
   - To satisfy \( t_i \leq B_i \), we derive \( S \geq \frac{i}{B_i} \).
   - To satisfy \( t_i \geq A_i \), we derive \( S \leq \frac{i}{A_i} \). However, if \( A_i = 0 \), this imposes no upper bound on \( S \).

3. **Feasibility Check:** 
   - Find the maximum value of \( \frac{i}{B_i} \) across all stations. This is the minimum speed required to meet the latest delivery window.
   - Find the minimum value of \( \frac{i}{A_i} \) across all stations where \( A_i > 0 \). This is the maximum allowable speed to avoid arriving before the delivery window opens.
   - If the maximum required speed \( \leq \) minimum allowable speed, a feasible speed exists, and the minimal such speed is the maximum required speed.
   - If not, it's impossible to satisfy all delivery windows simultaneously.

4. **Edge Cases:**
   - If \( A_i = 0 \) for any station, it does not constrain the upper speed limit.
   - All divisions should handle \( A_i = 0 \) appropriately to avoid division by zero errors.

**Python Code:**

```python
import sys
import math

def main():
    import sys
    import threading

    def run():
        T = int(sys.stdin.readline())
        for test_case in range(1, T+1):
            N_line = ''
            # Read until a non-empty line
            while N_line.strip() == '':
                N_line = sys.stdin.readline()
            N = int(N_line)
            max_lower = 0.0
            min_upper = float('inf')
            for i in range(1, N+1):
                line = ''
                while line.strip() == '':
                    line = sys.stdin.readline()
                A_i_str, B_i_str = line.strip().split()
                A_i = int(A_i_str)
                B_i = int(B_i_str)
                # Compute i / B_i
                lower = i / B_i
                if lower > max_lower:
                    max_lower = lower
                # Compute i / A_i if A_i >0
                if A_i > 0:
                    upper = i / A_i
                    if upper < min_upper:
                        min_upper = upper
            if max_lower <= min_upper:
                # Output max_lower with sufficient precision
                # To ensure the required precision, format with 10 decimal places
                # and remove trailing zeros
                S = max_lower
                print(f"Case #{test_case}: {S:.10f}".rstrip('0').rstrip('.'))
            else:
                print(f"Case #{test_case}: -1")

    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()
```