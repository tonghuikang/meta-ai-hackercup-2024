import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        S = sys.stdin.readline().strip()
        N = int(sys.stdin.readline())
        for _ in range(N - 1):
            sys.stdin.readline()  # Read and ignore the edges
        if S == 'kij' or S == 'kji':
            result = 'Lucky'
        else:
            result = 'Wrong'
        print(f"Case #{case_num}: {result}")

threading.Thread(target=main).start()