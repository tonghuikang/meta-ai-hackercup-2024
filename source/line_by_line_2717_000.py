import math

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    idx = 1
    for tc in range(1, T+1):
        N = int(data[idx])
        P = int(data[idx+1])
        idx +=2
        if P ==0:
            # If P=0, no chance of success, to make P'>0 it's infinite, but constraints say P>=1
            difference = 0.0
        elif P ==100:
            # If P=100, already perfect, no need to increase
            difference =0.0
        else:
            power = (N-1)/N
            P_prime = 100 * math.pow(P /100.0, power)
            difference = P_prime - P
        print(f"Case #{tc}: {difference}")
        
if __name__ == "__main__":
    main()