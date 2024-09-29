import sys
import math

def calculate_increase(N, P):
    # Convert P from percentage to a fraction
    p_decimal = P / 100.0
    
    # Chance of success for N lines
    success_N = p_decimal ** N
    
    # Chance of success for N-1 lines
    required_success = success_N ** (1 / (N - 1))
    
    # Convert back to percentage
    required_P = required_success ** (1 / P) * 100
    
    # Calculate the increase in percentage
    increase = required_P - P
    
    return increase

def main():
    input = sys.stdin.read
    data = input().strip().splitlines()
    
    T = int(data[0])
    results = []
    
    for i in range(1, T + 1):
        N, P = map(int, data[i].strip().split())
        increase = calculate_increase(N, P)
        results.append(f"Case #{i}: {increase:.10f}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()