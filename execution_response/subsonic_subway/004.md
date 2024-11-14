**Key Findings:**

To determine the minimum constant speed \( s \) that allows Sonic to deliver sandwiches to all stations within their respective time windows \([A_i, B_i]\), we can use the following approach:

1. **Time and Speed Relationship:**
   - The time \( t_i \) for Sonic to reach station \( i \) (which is \( i \) miles away) at speed \( s \) is given by \( t_i = \frac{i}{s} \).
   - Sonic must arrive at station \( i \) within the time window \([A_i, B_i]\), so:
     \[
     A_i \leq \frac{i}{s} \leq B_i
     \]
   - Rearranging the inequalities for \( s \):
     \[
     \frac{i}{B_i} \leq s \leq \frac{i}{A_i}
     \]
     (Note: Since \( A_i < B_i \), \( \frac{i}{B_i} \) will be less than \( \frac{i}{A_i} \)).

2. **Determining Feasibility:**
   - For all stations, the speed \( s \) must satisfy:
     \[
     s \geq \max\left( \frac{i}{B_i} \right) \quad \text{and} \quad s \leq \min\left( \frac{i}{A_i} \right)
     \]
   - If \( \max\left( \frac{i}{B_i} \right) \leq \min\left( \frac{i}{A_i} \right) \), then such a speed \( s \) exists, and the minimum possible \( s \) is \( \max\left( \frac{i}{B_i} \right) \).
   - If \( \max\left( \frac{i}{B_i} \right) > \min\left( \frac{i}{A_i} \right) \), no such constant speed exists, and the output should be \(-1\).

3. **Implementation Considerations:**
   - Since \( N \) can be up to \( 10^6 \) and the sum of \( N \) across test cases is up to \( 5 \times 10^6 \), the solution must be efficient.
   - Floating-point precision is crucial, as the answer must be accurate within \( 10^{-6} \).

**Python Code:**

```python
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
```

**Explanation of the Code:**

1. **Reading Input Efficiently:**
   - The entire input is read at once and split into a list for faster access, which is crucial given the large input size constraints.

2. **Processing Each Test Case:**
   - For each test case, we initialize:
     - `max_i_over_Bi` to track the maximum value of \( \frac{i}{B_i} \).
     - `min_i_over_Ai` to track the minimum value of \( \frac{i}{A_i} \).
   - We iterate through each station, updating these two variables accordingly.
   - We also handle edge cases:
     - If \( B_i = 0 \), delivery is impossible for that station.
     - If \( A_i = 0 \), \( \frac{i}{A_i} \) is considered infinity since Sonic can take an infinitely slow speed and still deliver on time.

3. **Determining the Result:**
   - After processing all stations, we check if \( \max\left( \frac{i}{B_i} \right) \leq \min\left( \frac{i}{A_i} \right) \).
   - If so, the minimum speed \( s \) is \( \max\left( \frac{i}{B_i} \right) \); otherwise, output \(-1\).

4. **Output Formatting:**
   - The result is printed with up to 10 decimal places, trimming any trailing zeros and decimal points to match the required precision.

**Handling Precision:**
- The solution ensures that floating-point arithmetic is handled carefully to maintain the required precision, especially when comparing \( \max\left( \frac{i}{B_i} \right) \) and \( \min\left( \frac{i}{A_i} \right) \).