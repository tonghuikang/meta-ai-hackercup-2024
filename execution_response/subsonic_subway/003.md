**Key Findings:**

To determine the minimum constant speed \( s \) that Sonic must maintain to deliver sandwiches to all stations within their respective delivery windows, we analyze each station's constraints:

1. **Time Calculation:**
   - For each station \( i \) located \( i \) miles away, the time \( t_i \) required to reach it is \( t_i = \frac{i}{s} \).
   - Sonic must satisfy the delivery window for each station: \( A_i \leq t_i \leq B_i \).

2. **Speed Constraints:**
   - From \( t_i \leq B_i \): \( s \geq \frac{i}{B_i} \).
   - From \( t_i \geq A_i \) (only if \( A_i > 0 \)): \( s \leq \frac{i}{A_i} \).

3. **Determining Feasibility:**
   - **Minimum Speed (\( s_{\text{min}} \))**: The maximum of all \( \frac{i}{B_i} \) values ensures Sonic arrives on time for the strictest latest delivery window.
   - **Maximum Possible Speed (\( s_{\text{max}} \))**: The minimum of all \( \frac{i}{A_i} \) values (for \( A_i > 0 \)) ensures Sonic doesn't arrive too early for any delivery window.
   - **Condition for a Valid Speed**: \( s_{\text{min}} \leq s_{\text{max}} \). If this condition holds, \( s_{\text{min}} \) is the required speed. Otherwise, it's impossible to satisfy all delivery windows, and the answer is -1.

4. **Edge Cases:**
   - If \( A_i = 0 \) for all stations, there's effectively no upper speed limit, and only \( s_{\text{min}} \) is considered.
   - If any station has \( A_i > B_i \), it’s impossible to satisfy the delivery window, resulting in -1.

Based on these findings, the following Python code efficiently computes the required minimum speed for each test case, even with large inputs.

```python
import sys

def readints():
    return list(map(int, sys.stdin.readline().split()))

def main():
    import sys
    import math
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); idx +=1
        s_min = 0.0
        s_max = math.inf
        has_A_positive = False
        for i in range(1, N+1):
            A_i = int(data[idx]); idx +=1
            B_i = int(data[idx]); idx +=1
            s_candidate_min = i / B_i
            if s_candidate_min > s_min:
                s_min = s_candidate_min
            if A_i > 0:
                s_candidate_max = i / A_i
                if s_candidate_max < s_max:
                    s_max = s_candidate_max
                has_A_positive = True
        possible = True
        if has_A_positive:
            if s_min > s_max + 1e-12:
                possible = False
        # If no A_i >0, then no upper limit
        if possible:
            # To handle precision, format with enough decimal places
            print(f"Case #{test_case}: {s_min if has_A_positive else s_min}")
        else:
            print(f"Case #{test_case}: -1")
            
if __name__ == "__main__":
    main()
```