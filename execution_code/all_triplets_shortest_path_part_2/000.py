import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for tc in range(1, T+1):
        S = data[idx]; idx +=1
        N = int(data[idx]); idx +=1
        for _ in range(N-1):
            U = data[idx]; V = data[idx+1]; idx +=2
        if S.startswith('k'):
            result = "Lucky"
        else:
            result = "Wrong"
        print(f"Case #{tc}: {result}")

if __name__ == "__main__":
    main()