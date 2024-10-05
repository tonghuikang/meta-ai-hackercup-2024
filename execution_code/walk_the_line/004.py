def bridge_crossing():
    import sys
    import sys
    import sys
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        N_K = line.strip().split()
        N = int(N_K[0])
        K = int(N_K[1])
        S = []
        count = 0
        while count < N:
            s_line = sys.stdin.readline()
            if s_line.strip() != '':
                S.append(int(s_line.strip()))
                count +=1
        S.sort()
        total_time =0
        n = N
        while n >3:
            option1 = 2*S[1] + S[0] + S[n-1]
            option2 = 2*S[0] + S[n-2] + S[n-1]
            total_time += min(option1, option2)
            n -=2
        if n ==3:
            total_time += S[0] + S[1] + S[2]
        elif n ==2:
            total_time += S[1]
        elif n ==1:
            total_time += S[0]
        if total_time <= K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    bridge_crossing()

def bridge_crossing():
    import sys
    import sys
    import sys
    T = int(sys.stdin.readline())
    for test_case in range(1, T+1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        N_K = line.strip().split()
        N = int(N_K[0])
        K = int(N_K[1])
        S = []
        count = 0
        while count < N:
            s_line = sys.stdin.readline()
            if s_line.strip() != '':
                S.append(int(s_line.strip()))
                count +=1
        S.sort()
        total_time =0
        n = N
        while n >3:
            option1 = 2*S[1] + S[0] + S[n-1]
            option2 = 2*S[0] + S[n-2] + S[n-1]
            total_time += min(option1, option2)
            n -=2
        if n ==3:
            total_time += S[0] + S[1] + S[2]
        elif n ==2:
            total_time += S[1]
        elif n ==1:
            total_time += S[0]
        if total_time <= K:
            result = "YES"
        else:
            result = "NO"
        print(f"Case #{test_case}: {result}")

if __name__ == "__main__":
    bridge_crossing()