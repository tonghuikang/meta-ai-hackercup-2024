import sys

def main():
    import sys
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for tc in range(1, T+1):
        S = data[idx]; idx +=1
        N = int(data[idx]); idx +=1
        # Skip the next N-1 lines
        idx += 2*(N-1)
        if S[0] == 'k':
            result = "Lucky"
        else:
            result = "Wrong"
        print(f"Case #{tc}: {result}")

if __name__ == "__main__":
    main()