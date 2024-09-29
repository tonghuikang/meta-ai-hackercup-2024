def main():
    import sys
    import sys
    import sys
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        line=''
        while line.strip()=='':
            line = sys.stdin.readline()
        N,K = map(int,line.strip().split())
        S = []
        count=0
        while count<N:
            s = sys.stdin.readline()
            if s.strip()=='':
                continue
            S.append(int(s.strip()))
            count+=1
        S.sort()
        sum_time =0
        i = N
        while i >2:
            option1 = 2 * S[1] + S[0] + S[i-1]
            option2 = 2 * S[0] + S[i-2] + S[i-1]
            sum_time += min(option1, option2)
            i -=2
        if i ==2:
            sum_time += S[1]
        elif i ==1:
            sum_time += S[0]
        result = "YES" if sum_time <= K else "NO"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    main()