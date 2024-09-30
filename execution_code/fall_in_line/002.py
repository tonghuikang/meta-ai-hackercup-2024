import sys
import itertools

def main():
    data = sys.stdin.read().split()
    it = iter(data)
    T = int(next(it))
    for tc in range(1, T + 1):
        N = int(next(it))
        x_list = []
        y_list = []
        y_minus_x = []
        y_plus_x = []
        for _ in range(N):
            x = int(next(it))
            y = int(next(it))
            x_list.append(x)
            y_list.append(y)
            y_minus_x.append(y - x)
            y_plus_x.append(y + x)
        max_count = 0
        for lst in [x_list, y_list, y_minus_x, y_plus_x]:
            lst.sort()
            if not lst:
                continue
            # Use itertools.groupby to find the maximum frequency
            current_max = max(len(list(group)) for key, group in itertools.groupby(lst))
            if current_max > max_count:
                max_count = current_max
        M = N - max_count
        print(f"Case #{tc}: {M}")

if __name__ == "__main__":
    main()