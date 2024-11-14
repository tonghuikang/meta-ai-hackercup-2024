**Key Findings:**

1. **Speed Constraints per Station:**
   - To deliver at station \(i\) within the window \([A_i, B_i]\), Sonic's speed \(S\) must satisfy:
     \[
     S \geq \frac{i}{B_i} \quad \text{and} \quad S \leq \frac{i}{A_i} \quad \text{(if } A_i > 0\text{)}
     \]
   - If \(A_i = 0\), there's no upper bound for \(S\) from that station.

2. **Overall Speed Determination:**
   - **Lower Bound:** The minimum speed \(S\) must be at least the maximum value of \(\frac{i}{B_i}\) across all stations:
     \[
     \text{max\_lower} = \max\left(\frac{1}{B_1}, \frac{2}{B_2}, \dots, \frac{N}{B_N}\right)
     \]
   - **Upper Bound:** The maximum permissible speed \(S\) is the minimum value of \(\frac{i}{A_i}\) across all stations where \(A_i > 0\):
     \[
     \text{min\_upper} = \min\left(\frac{i}{A_i} \text{ for all } i \text{ with } A_i > 0\right)
     \]
   - **Feasibility Check:** If \(\text{max\_lower} \leq \text{min\_upper}\), the minimum feasible speed is \(\text{max\_lower}\). Otherwise, it's impossible to satisfy all delivery windows, and the answer is \(-1\).

3. **Implementation Considerations:**
   - Efficiently handle large inputs by processing each test case independently.
   - Use floating-point precision carefully to ensure accuracy within the required tolerance.
   - Handle cases where \(A_i = 0\) appropriately to avoid division by zero.

```python
import sys
import math

def main():
    import sys
    import threading

    def solve():
        import sys

        T = int(sys.stdin.readline())
        for case in range(1, T +1):
            N_line = ''
            while N_line.strip() == '':
                N_line = sys.stdin.readline()
            N = int(N_line)
            max_lower = 0.0
            min_upper = math.inf
            for i in range(1, N+1):
                line = ''
                while line.strip() == '':
                    line = sys.stdin.readline()
                A_i_str, B_i_str = line.strip().split()
                A_i = float(A_i_str)
                B_i = float(B_i_str)
                lower = i / B_i
                if lower > max_lower:
                    max_lower = lower
                if A_i > 0:
                    upper = i / A_i
                    if upper < min_upper:
                        min_upper = upper
            # If there are no A_i >0, min_upper remains inf
            # To handle this, min_upper should be inf, so check max_lower <= inf is always true
            # So S = max_lower
            if max_lower <= min_upper:
                # For output, need to handle precision up to 1e-6
                # But the problem allows any precision as long as within 1e-6
                print(f"Case #{case}: {max_lower}")
            else:
                print(f"Case #{case}: -1")
    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()
```