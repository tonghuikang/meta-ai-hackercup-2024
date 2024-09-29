def calculate_needed_increase(N, P):
    # Probability of getting all lines correct with N lines of code
    P_success_N = (P / 100) ** N
    
    # Probability of getting all lines correct with N-1 lines of code
    P_success_N_minus_1 = (P / 100) ** (N - 1)
    
    # We want to find the new probability (P_new) such that:
    # (P_new / 100) ** N = P_success_N_minus_1
    # => P_new / 100 = (P_success_N_minus_1) ** (1/N)
    # => P_new = 100 * (P_success_N_minus_1) ** (1/N)
    
    P_new = 100 * (P_success_N_minus_1 ** (1/N))
    
    # Increase needed in percentage
    increase_needed = P_new - P
    
    return increase_needed

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])  # Number of test cases
    results = []
    
    for i in range(1, T + 1):
        N, P = map(int, data[i].split())
        increase = calculate_needed_increase(N, P)
        results.append(f"Case #{i}: {increase}")
    
    # Printing results
    for result in results:
        print(result)

if __name__ == "__main__":
    main()