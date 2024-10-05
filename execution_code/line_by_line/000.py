import math
import sys

def main():
    T = int(sys.stdin.readline())
    for case in range(1, T +1):
        N_str, P_str = sys.stdin.readline().strip().split()
        N = int(N_str)
        P = int(P_str)
        p = P /100.0
        if p ==0:
            delta_p =0.0
        else:
            # Compute log(p) * (N-1)/N
            exponent = (N-1)/N
            new_p = math.exp(math.log(p) * exponent) *100
            delta_p = new_p - P
        print(f"Case #{case}: {delta_p}")
            
if __name__ == "__main__":
    main()