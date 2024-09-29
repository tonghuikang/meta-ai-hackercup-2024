def calculate_increase_probability(N, P):
    # Convert P from percentage to a fraction
    P_fraction = P / 100.0
    
    # The success chance for the original N lines of code
    success_chance_N = P_fraction ** N
    
    # The success chance for just N-1 lines of code
    success_chance_N1 = P_fraction ** (N - 1)
    
    # We need to find the required P_new such that (P_new / 100.0) ** N = success_chance_N1
    # Solving for P_new:
    # (P_new / 100.0) = success_chance_N1 ** (1/N)
    # P_new = 100.0 * (success_chance_N1 ** (1/N))
    
    success_probability_N1 = success_chance_N1 ** (1 / (N - 1))
    
    P_new = 100.0 * success_probability_N1
    
    # Return how much higher P needs to be
    return P_new - P

def main():
    T = int(input().strip())
    
    for i in range(1, T + 1):
        N, P = map(int, input().strip().split())
        increase = calculate_increase_probability(N, P)
        print(f"Case #{i}: {increase:.12f}")

if __name__ == "__main__":
    main()