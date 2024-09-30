def calculate_required_increase(N, P):
    # Convert P to a probability in range [0, 1]
    current_success_probability = P / 100.0

    # Probability of success when typing N-1 lines
    success_N_minus_1 = current_success_probability ** (N - 1)

    # To find the required P_new that gives us the same success probability
    # P_new = (sqrt(success_N_minus_1)) * 100 or P_new = (success_N_minus_1 ** (1/(N-1))) * 100
    # In terms of success probabilities:
    required_success_probability = success_N_minus_1 ** (1 / (N - 1))

    # Convert it back to percentage
    required_P = required_success_probability * 100

    # Increase in P
    increase = required_P - P
    
    return increase

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    T = int(data[0])  # the number of test cases
    results = []

    for i in range(1, T + 1):
        N, P = map(int, data[i].split())
        increase = calculate_required_increase(N, P)
        results.append(f"Case #{i}: {increase}")

    print("\n".join(results))

if __name__ == "__main__":
    main()