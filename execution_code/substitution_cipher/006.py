import sys
import sys
import sys
import sys
sys.setrecursionlimit(1 << 25)

MOD = 998244353

def main():
    import sys
    from collections import defaultdict

    T = int(sys.stdin.readline())
    for tc in range(1, T+1):
        line = sys.stdin.readline().strip()
        if not line:
            line = sys.stdin.readline().strip()
        E, K = line.split()
        K = int(K)
        n = len(E)
        DP = [0] * (n+1)
        Count = [0] * (n+1)
        DP[n] = 1
        Count[n] =1
        assignments = [[] for _ in range(n)]
        # First pass: compute DP and assignments
        for i in range(n-1, -1, -1):
            options = []
            if E[i] != '?':
                d = E[i]
                total =0
                if d != '0':
                    total += DP[i+1]
                if i+1 <n:
                    if E[i+1] != '?':
                        num = int(d + E[i+1])
                        if 10 <= num <=26:
                            total += DP[i+2]
                    else:
                        if d == '1':
                            total += 10 * DP[i+2]
                        elif d == '2':
                            total += 7 * DP[i+2]
                DP[i] = total
                # Assignments not needed for fixed digits
            else:
                # E[i] == '?'
                max_total = -1
                digits_max = []
                # To maximize DP[i}, choose '1' or '2'
                for d in ['1','2']:
                    total =0
                    # Single digit
                    total += DP[i+1]
                    # Two-digit
                    if i+1 <n:
                        if E[i+1] != '?':
                            num = int(d + E[i+1])
                            if 10 <= num <=26:
                                total += DP[i+2]
                        else:
                            if d == '1':
                                total += 10 * DP[i+2]
                            elif d == '2':
                                total +=7 * DP[i+2]
                    if total > max_total:
                        max_total = total
                        digits_max = [d]
                    elif total == max_total:
                        digits_max.append(d)
                DP[i] = max_total
                assignments[i] = digits_max
        # Second pass: compute Count[i]
        Count = [0] * (n+1)
        Count[n] =1
        for i in range(n-1, -1, -1):
            if E[i] != '?':
                d = E[i]
                total =0
                if d != '0':
                    total += Count[i+1]
                if i+1 <n:
                    if E[i+1] != '?':
                        num = int(d + E[i+1})
                        if 10 <= num <=26:
                            total += Count[i+2]
                    else:
                        if d == '1':
                            total += 10 * Count[i+2]
                        elif d == '2':
                            total +=7 * Count[i+2]
                Count[i] = total
            else:
                Count[i] =0
                for d in assignments[i]:
                    if d == '1':
                        Count[i] += Count[i+1]
                        if i+1 <n:
                            if E[i+1] == '?':
                                Count[i] +=10 * Count[i+2]
                            else:
                                num = int(d + E[i+1})
                                if 10 <= num <=26:
                                    Count[i] += Count[i+2]
                    elif d == '2':
                        Count[i] += Count[i+1]
                        if i+1 <n:
                            if E[i+1] == '?':
                                Count[i] +=7 * Count[i+2]
                            else:
                                num = int(d + E[i+1})
                                if 10 <= num <=26:
                                    Count[i] += Count[i+2]
                Count[i] %= MOD
        # Now, find the lex Kth largest U
        result = []
        i =0
        while i <n:
            if E[i] != '?':
                result.append(E[i])
                i +=1
            else:
                digits = sorted(assignments[i], reverse=True)
                for d in digits:
                    # Compute the number of U's starting with this choice
                    if d == '1':
                        cnt = Count[i+1]
                        if i+1 <n:
                            if E[i+1] == '?':
                                cnt *=10
                            else:
                                num = int(d + E[i+1})
                                if 10 <= num <=26:
                                    cnt += Count[i+2]
                    elif d == '2':
                        cnt = Count[i+1]
                        if i+1 <n:
                            if E[i+1} == '?':
                                cnt *=7
                            else:
                                num = int(d + E[i+1})
                                if 10 <= num <=26:
                                    cnt += Count[i+2]
                    else:
                        cnt =0
                    if E[i] == '?':
                        if d == '1':
                            if i+1 <n and E[i+1} == '?':
                                cnt =10 * Count[i+2]
                            elif i+1 <n:
                                num = int(d + E[i+1})
                                cnt = Count[i+1} + (Count[i+2} if 10 <= num <=26 else 0)
                            else:
                                cnt = Count[i+1}
                        elif d == '2':
                            if i+1 <n and E[i+1} == '?':
                                cnt =7 * Count[i+2}
                            elif i+1 <n:
                                num = int(d + E[i+1})
                                cnt = Count[i+1} + (Count[i+2} if 10 <= num <=26 else 0)
                            else:
                                cnt = Count[i+1}
                    if K <= cnt:
                        result.append(d)
                        if E[i+1} == '?':
                            if d == '1':
                                # Assign next digit freely
                                i +=1
                            elif d == '2':
                                # Assign next digit freely within '0'-'6'
                                i +=1
                        else:
                            i +=1
                        break
                    else:
                        K -= cnt
        # Now, reconstruct the maximum DP and Count
        # To get the actual decoding count
        # But as sample shows, the count to report is DP[0}
        # Currently, Count[0} can be used
        print(f"Case #{tc}: {''.join(result)} {Count[0]%MOD}")

if __name__ == "__main__":
    main()