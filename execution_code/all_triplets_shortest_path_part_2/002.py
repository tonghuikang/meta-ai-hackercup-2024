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
        degree = [0]*(N+1)
        for _ in range(N-1):
            u = int(data[idx]); v = int(data[idx+1]); idx +=2
            degree[u] +=1
            degree[v] +=1
        # Check if S starts with 'k'
        if S[0] == 'k':
            result = "Lucky"
        else:
            # Check if the tree is a path or a star
            cnt_deg1 = 0
            cnt_degN_1 = 0
            for d in degree[1:]:
                if d ==1:
                    cnt_deg1 +=1
                elif d == N-1:
                    cnt_degN_1 +=1
            if (cnt_deg1 ==2 and all(d ==2 or d ==1 for d in degree[1:])) or (cnt_degN_1 ==1 and all(d ==1 or d ==N-1 for d in degree[1:])):
                result = "Lucky"
            else:
                result = "Wrong"
        print(f"Case #{tc}: {result}")

if __name__ == "__main__":
    main()