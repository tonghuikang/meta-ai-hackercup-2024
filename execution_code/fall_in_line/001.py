import sys
from itertools import groupby

def max_freq(lst):
    sorted_lst = sorted(lst)
    return max((sum(1 for _ in g) for k, g in groupby(sorted_lst)), default=0)

def main():
    import sys
    import sys
    data = sys.stdin.read().split()
    ptr = 0
    T = int(data[ptr])
    ptr +=1
    for test_case in range(1, T+1):
        N = int(data[ptr])
        ptr +=1
        xs = []
        ys = []
        y_minus_x = []
        y_plus_x = []
        for _ in range(N):
            x = int(data[ptr])
            y = int(data[ptr+1])
            ptr +=2
            xs.append(x)
            ys.append(y)
            y_minus_x.append(y - x)
            y_plus_x.append(y + x)
        max_x = max_freq(xs)
        max_y = max_freq(ys)
        max_y_minus_x = max_freq(y_minus_x)
        max_y_plus_x = max_freq(y_plus_x)
        P = max(max_x, max_y, max_y_minus_x, max_y_plus_x)
        M = N - P
        print(f"Case #{test_case}: {M}")

if __name__ == "__main__":
    main()