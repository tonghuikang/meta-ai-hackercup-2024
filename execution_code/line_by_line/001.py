import sys
import math

def calculate_increase(T, test_cases):
    results = []
    for i in range(T):
        N, P = test_cases[i]
        
        # Convert P from percentage to a fraction
        probability_success = P / 100.0
        
        # Success probability for N lines
        total_probability_N = probability_success ** N
        
        # Success probability for N-1 lines
        total_probability_N_minus_1 = probability_success ** (N - 1)

        # We need the square root of the current probability to match the N-1 line case
        required_probability = math.sqrt(total_probability_N_minus_1)
        
        # Convert required probability back to percentage
        required_probability_percentage = required_probability * 100
        
        # Calculate the increase needed
        increase_needed = required_probability_percentage - P
        results.append(f"Case #{i + 1}: {increase_needed}")
    
    return results

def main():
    input_data = sys.stdin.read()
    lines = input_data.strip().split('\n')
    T = int(lines[0])
    test_cases = [tuple(map(int, line.split())) for line in lines[1:T + 1]]
    
    results = calculate_increase(T, test_cases)
    print("\n".join(results))

if __name__ == "__main__":
    main()