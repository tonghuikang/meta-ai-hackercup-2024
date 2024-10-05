import sys
import numpy as np

def main():
    import sys
    import numpy as np

    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr])
    ptr +=1
    for case in range(1, T+1):
        N = int(input[ptr])
        ptr +=1
        if N <2:
            # All points are on a line
            M=0
            ptr += 2*N
        else:
            # Read N pairs
            points = np.array(list(map(int, input[ptr:ptr+2*N])), dtype=np.int64).reshape(N,2)
            ptr +=2*N
            x1, y1 = points[0]
            x2, y2 = points[1]
            dx = x2 - x1
            dy = y2 - y1
            if dx ==0:
                # Vertical line: x ==x1
                count = np.sum(points[:,0] == x1)
            else:
                # Non-vertical line: dy*(x -x1) == dx*(y - y1)
                lhs = dy * (points[:,0] - x1)
                rhs = dx * (points[:,1] - y1)
                count = np.sum(lhs == rhs)
            M = N - count
        print(f"Case #{case}: {M}")

if __name__ == "__main__":
    main()