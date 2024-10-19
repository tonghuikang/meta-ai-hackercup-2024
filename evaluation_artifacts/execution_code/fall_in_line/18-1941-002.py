import sys

def main():
    import sys
    from sys import stdin
    def readints():
        return list(map(int, sys.stdin.read().split()))
    
    data = readints()
    it = iter(data)
    T = next(it)
    for test_case in range(1, T+1):
        N = next(it)
        x_list = []
        y_list = []
        xpy_list = []
        xmy_list = []
        for _ in range(N):
            x = next(it)
            y = next(it)
            x_list.append(x)
            y_list.append(y)
            xpy_list.append(x + y)
            xmy_list.append(x - y)
        max_count = 0
        for lst in [x_list, y_list, xpy_list, xmy_list]:
            lst_sorted = sorted(lst)
            current = 1
            local_max = 1
            for i in range(1, N):
                if lst_sorted[i] == lst_sorted[i-1]:
                    current +=1
                else:
                    if current > local_max:
                        local_max = current
                    current =1
            if current > local_max:
                local_max = current
            if local_max > max_count:
                max_count = local_max
        answer = N - max_count
        print(f"Case #{test_case}: {answer}")

if __name__ == "__main__":
    main()

import sys

def main():
    import sys
    from sys import stdin
    def readints():
        return list(map(int, sys.stdin.read().split()))
    
    data = readints()
    it = iter(data)
    T = next(it)
    for test_case in range(1, T+1):
        N = next(it)
        x_list = []
        y_list = []
        xpy_list = []
        xmy_list = []
        for _ in range(N):
            x = next(it)
            y = next(it)
            x_list.append(x)
            y_list.append(y)
            xpy_list.append(x + y)
            xmy_list.append(x - y)
        max_count = 0
        for lst in [x_list, y_list, xpy_list, xmy_list]:
            lst_sorted = sorted(lst)
            current = 1
            local_max = 1
            for i in range(1, N):
                if lst_sorted[i] == lst_sorted[i-1]:
                    current +=1
                else:
                    if current > local_max:
                        local_max = current
                    current =1
            if current > local_max:
                local_max = current
            if local_max > max_count:
                max_count = local_max
        answer = N - max_count
        print(f"Case #{test_case}: {answer}")

if __name__ == "__main__":
    main()