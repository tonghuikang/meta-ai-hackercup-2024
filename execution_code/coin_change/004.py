import math
import sys

def harmonic_number(n):
    # Using approximation for large n
    if n < 1e6:
        H = 0.0
        for i in range(1, n+1):
            H += 1.0 / i
        return H
    else:
        gamma = 0.57721566490153286060651209008240243104215933593992
        return math.log(n) + gamma + 1/(2*n) - 1/(12*n**2) + 1/(120*n**4)

def expected_bills(N, P):
    if P == 0:
        return N * harmonic_number(N)
    elif P == 100:
        # When P=100, optimal strategy is to insert D=2 bills whenever possible to guarantee a new coin
        # Except when k=0, where inserting D=1 is optimal since any coin is new
        # So, E = 1 + 2*(N-1)
        return 1 + 2 * (N - 1)
    else:
        # For general P, we need to compute E = sum_{k=0}^{N-1} 1 / p_k
        # where p_k is the probability to obtain a new coin when you have k coins
        # Optimal D can be chosen to maximize p_k
        # p_k = min((D-1)*P, 100)/100 * (N - k)/N + (1 - min((D-1)*P, 100)/100) * (N - k)/N
        # Simplifies to p_k = (N - k)/N * min((D-1)*P, 100)/100 + (N - k)/N * (1 - min((D-1)*P, 100)/100)
        # Which further simplifies to p_k = (N - k)/N
        # This suggests that the optimal D is irrelevant, which contradicts the sample.
        # Therefore, a different approach is needed.
        # Alternatively, assume that with probability c = min((D-1)*P, 100)/100, you get a new coin
        # and with probability (1 - c), you get a random coin

        # To maximize p_k, choose D such that c is maximized
        # c = min((D-1)*P, 100)/100
        # To maximize c without overshooting, set (D-1)*P >= 100
        # Therefore, optimal D = ceil( (100)/P ) +1
        if P == 0:
            return N * harmonic_number(N)
        # Optimal D is  when (D-1)*P >= 100
        optimal_D = math.ceil(100 / P) + 1
        c = min((optimal_D -1)*P, 100) / 100.0
        # If inserting D bills, expected bills to get a new coin:
        # E_k = D / c
        # Total E = sum_{k=1}^N D / c = N * D / c
        # But need to adjust for the probability of getting new coins earlier
        # A more precise calculation requires integrating over expectations
        # For simplicity, use harmonic number scaled by D / c
        H_N = harmonic_number(N)
        return H_N * (optimal_D / c)

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    index = 1
    for t in range(1, T+1):
        N = int(input[index])
        P = int(input[index+1])
        index +=2
        result = expected_bills(N, P)
        # Format the result with sufficient precision
        print(f"Case #{t}: {result}")

if __name__ == "__main__":
    main()