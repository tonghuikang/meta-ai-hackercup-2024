import sys

def main():
    import sys
    import threading

    def solve():
        import sys

        T = int(sys.stdin.readline())
        for test_case in range(1, T+1):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            N = int(line.strip())
            v_min = 0.0
            v_max = float('inf')
            for i in range(1, N+1):
                while True:
                    line = sys.stdin.readline()
                    if line.strip() != '':
                        break
                A_str, B_str = line.strip().split()
                A_i = float(A_str)
                B_i = float(B_str)
                v_current_min = i / B_i
                if v_current_min > v_min:
                    v_min = v_current_min
                if A_i > 0:
                    v_current_max = i / A_i
                    if v_current_max < v_max:
                        v_max = v_current_max
            if v_min <= v_max:
                # To ensure the output meets the precision requirement
                print(f"Case #{test_case}: {v_min:.10f}".rstrip('0').rstrip('.'))
            else:
                print(f"Case #{test_case}: -1")
    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()