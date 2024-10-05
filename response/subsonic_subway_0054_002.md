**Key Findings:**

1. **Understanding the Problem:**
   - Sonic needs to deliver sandwiches to `N` stations, each located `i` miles away.
   - For each station `i`, there's a delivery window `[A_i, B_i]` seconds.
   - Sonic must run at a constant speed `s` such that he arrives at each station within its delivery window.

2. **Formulating the Solution:**
   - The time to reach station `i` at speed `s` is `t_i = i / s`.
   - To satisfy the delivery window, `A_i ≤ t_i ≤ B_i`, which translates to:
     - `s ≥ i / B_i` (to arrive before the window closes)
     - `s ≤ i / A_i` (to arrive after the window opens), provided `A_i > 0`.
   - The minimum speed `s` that satisfies all stations is the maximum of all `i / B_i`.
   - Additionally, this speed must not exceed the minimum of all `i / A_i` for stations where `A_i > 0`.
   - If the maximum `i / B_i` exceeds the minimum `i / A_i`, it's impossible to satisfy all delivery windows, and the answer is `-1`.

3. **Implementation Considerations:**
   - Due to large input sizes (`N` up to 1,000,000 per test case), efficient input processing is crucial.
   - All calculations are performed using floating-point arithmetic to handle divisions accurately.
   - Edge cases, such as when `A_i = 0`, are handled by ignoring the corresponding upper speed limit since `s` can be as large as needed.

4. **Precision Handling:**
   - The final speed is printed with sufficient precision to meet the problem's requirements.
   - If no valid speed exists, `-1` is output.

**Python Code:**

```python
import sys

def main():
    import sys
    import math

    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(input[idx]); idx +=1
        s_min_candidate = 0.0
        s_max_candidate = math.inf
        for i in range(1, N+1):
            A_i = float(input[idx]); idx +=1
            B_i = float(input[idx]); idx +=1
            s_i_min = i / B_i
            s_min_candidate = max(s_min_candidate, s_i_min)
            if A_i > 0:
                s_i_max = i / A_i
                if s_i_max < s_max_candidate:
                    s_max_candidate = s_i_max
        if s_min_candidate <= s_max_candidate:
            # To ensure precision, format with enough decimal places
            print(f"Case #{test_case}: {s_min_candidate:.10f}".rstrip('0').rstrip('.'))
        else:
            print(f"Case #{test_case}: -1")

if __name__ == "__main__":
    main()
```