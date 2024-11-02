import sys
import sys
import sys
def main():
    import sys
    import sys
    from sys import stdin
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for tc in range(1, T+1):
        N = int(input[idx])
        idx +=1
        degree = [0]*(N+1)
        for _ in range(N-1):
            u = int(input[idx])
            v = int(input[idx+1])
            degree[u] +=1
            degree[v] +=1
            idx +=2
        count = 0
        for d in degree:
            if d >2:
                count +=1
        if count <=1:
            result = "Lucky"
        else:
            result = "Wrong"
        print(f"Case #{tc}: {result}")
if __name__ == "__main__":
    main()