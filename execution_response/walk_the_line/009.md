**Key Findings:**

1. **Problem Understanding:**
   - We need to determine if all travelers can cross the bridge within a given time \( K \).
   - The bridge can support at most two people at a time, and they must use a single flashlight.
   - When two travelers cross together, the crossing time is determined by the traveler carrying the wheelbarrow (i.e., the faster traveler's time).

2. **Optimal Strategy:**
   - **Sorting:** Begin by sorting the travelers' crossing times \( S_i \) in ascending order. This allows us to identify the fastest and slowest travelers easily.
   - **Two Strategies Considered:**
     - **Strategy A (Fastest Person Shuttles):** The fastest traveler escorts each of the slower travelers one by one. This involves the fastest traveler going back and forth to shuttle others.
     - **Strategy B (Pair Slowest Travelers):** Pair the two slowest travelers together to minimize the number of crossings needed for the slowest individuals.
   - **Choosing the Best Strategy:**
     - For each group of travelers, compare the total time taken by both strategies and choose the one that results in the minimal total time.
     - Repeat this process until all travelers have crossed.

3. **Implementation Considerations:**
   - **Edge Cases:**
     - **Single Traveler:** If there's only one traveler, they cross alone.
     - **Two Travelers:** The faster traveler can escort the second one.
   - **Efficiency:** Since \( N \) can be up to \( 1{,}000 \), the solution must be efficient, preferably \( O(N \log N) \) due to sorting.
   - **Total Time Calculation:** Accumulate the total time taken by following the optimal strategy and compare it against \( K \).

Below is the Python implementation based on the above strategy:

```python
import sys

def can_cross_all(S, N, K):
    S.sort()
    total_time = 0
    left = N
    while left > 0:
        if left == 1:
            total_time += S[0]
            left -=1
        elif left ==2:
            total_time += S[0]
            left -=2
        elif left ==3:
            total_time += S[0] + S[1] + S[2]
            left -=3
        else:
            option1 = 2*S[1] + S[0] + S[left-1]
            option2 = S[left-1] + S[0] + S[left-2] + S[0]
            total_time += min(option1, option2)
            left -=2
    return total_time <= K

def main():
    input = sys.stdin.read().split()
    idx = 0
    T = int(input[idx])
    idx +=1
    for case in range(1, T+1):
        N = int(input[idx])
        K = int(input[idx+1])
        idx +=2
        S = []
        for _ in range(N):
            S.append(int(input[idx]))
            idx +=1
        if can_cross_all(S, N, K):
            print(f"Case #{case}: YES")
        else:
            print(f"Case #{case}: NO")

if __name__ == "__main__":
    main()
```