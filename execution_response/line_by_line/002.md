**Key Findings:**

To solve this problem, we need to determine how much the probability \( P \) must increase to achieve the same success rate when typing \( N \) lines of code compared to typing \( N-1 \) lines with the original probability.

1. **Understanding the Success Probability:**
   - The probability of successfully typing all \( N \) lines correctly is \( \left(\frac{P}{100}\right)^N \).
   - The probability of successfully typing \( N-1 \) lines correctly is \( \left(\frac{P}{100}\right)^{N-1} \).

2. **Establishing the Relationship:**
   - To have the same success probability when typing \( N \) lines with an increased probability \( P' \), we set:
     \[
     \left(\frac{P'}{100}\right)^N = \left(\frac{P}{100}\right)^{N-1}
     \]
   
3. **Solving for the New Probability \( P' \):**
   - Take the \( N \)-th root of both sides:
     \[
     \frac{P'}{100} = \left(\frac{P}{100}\right)^{\frac{N-1}{N}}
     \]
   - Multiply both sides by 100 to get \( P' \):
     \[
     P' = \left(\frac{P}{100}\right)^{\frac{N-1}{N}} \times 100
     \]
   
4. **Calculating the Increase in Probability:**
   - The required increase in probability \( \Delta P \) is:
     \[
     \Delta P = P' - P
     \]
   
5. **Implementation Considerations:**
   - Use precise floating-point arithmetic to ensure the result is accurate within the specified error margin.
   - Handle multiple test cases efficiently.

**Python Code:**

```python
import math
import sys

def calculate_delta_p(N, P):
    # Convert P to decimal
    P_decimal = P / 100.0
    # Calculate P' as (P / 100)^( (N-1)/N ) * 100
    exponent = (N - 1) / N
    P_new = (P_decimal ** exponent) * 100.0
    # Calculate delta P
    delta_P = P_new - P
    return delta_P

def main():
    T = int(sys.stdin.readline())
    for case in range(1, T + 1):
        line = sys.stdin.readline().strip()
        if not line:
            # If the line is empty, read next line
            line = sys.stdin.readline().strip()
        N_P = line.split()
        N = int(N_P[0])
        P = float(N_P[1])
        delta_P = calculate_delta_p(N, P)
        # Ensure the output has enough decimal places
        print(f"Case #{case}: {delta_P}")

if __name__ == "__main__":
    main()
```