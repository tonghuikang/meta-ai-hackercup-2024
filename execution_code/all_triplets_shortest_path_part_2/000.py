import sys

import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for case in range(1, T+1):
        S = data[idx]; idx +=1
        N = int(data[idx]); idx +=1
        # Skip N-1 edges
        idx += 2*(N-1)
        # Determine if loop order starts with 'k'
        if S[0] == 'k':
            result = "Lucky"
        else:
            result = "Wrong"
        print(f"Case #{case}: {result}")

if __name__ == "__main__":
    main()