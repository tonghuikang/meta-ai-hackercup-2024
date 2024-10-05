import sys
import sys
def main():
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    input = sys.stdin.read().split()
    idx =0
    T=int(input[idx]);idx+=1
    for test_case in range(1,T+1):
        N=int(input[idx]);G=int(input[idx+1]);idx+=2
        E=[]
        for _ in range(N):
            E.append(int(input[idx]))
            idx+=1
        p=[0]*N
        # Assign from last to first
        p[-1]=E[-1]
        for i in range(N-2,-1,-1):
            p[i]=max(E[i],p[i+1]+1)
        # Find the stone closest to G
        min_dist = None
        min_idx = None
        for i in range(N):
            dist = abs(G - p[i])
            if min_dist is None or dist < min_dist or (dist == min_dist and i+1 < min_idx):
                min_dist = dist
                min_idx = i+1
        print(f"Case #{test_case}: {min_idx} {min_dist}")
if __name__ == "__main__":
    main()