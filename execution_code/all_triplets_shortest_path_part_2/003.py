import sys
import sys
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
        edges = []
        for _ in range(N-1):
            u = int(data[idx]); idx +=1
            v = int(data[idx]); idx +=1
            edges.append( (u,v) )
        # Determine if S starts with 'k'
        if S[0] == 'k':
            res = "Lucky"
        else:
            res = "Wrong"
        print(f"Case #{tc}: {res}")

if __name__ == "__main__":
    main()