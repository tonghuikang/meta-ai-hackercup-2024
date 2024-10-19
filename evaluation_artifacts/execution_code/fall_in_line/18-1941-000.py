import sys
import math

def are_colinear(x1, y1, x2, y2, x3, y3):
    # Check if (y2 - y1)*(x3 - x1) == (y3 - y1)*(x2 - x1)
    return (y2 - y1)*(x3 - x1) == (y3 - y1)*(x2 - x1)

def main():
    import sys
    import threading

    def run():
        input = sys.stdin.read().split()
        idx = 0
        T = int(input[idx])
        idx +=1
        for test_case in range(1, T+1):
            N = int(input[idx])
            idx +=1
            points = []
            for _ in range(N):
                X = int(input[idx])
                Y = int(input[idx+1])
                points.append( (X,Y) )
                idx +=2
            if N <=2:
                A=0
            else:
                x1, y1 = points[0]
                x2, y2 = points[1]
                all_colinear = True
                for i in range(2, N):
                    xi, yi = points[i]
                    if not are_colinear(x1, y1, x2, y2, xi, yi):
                        all_colinear = False
                        break
                if all_colinear:
                    A=0
                else:
                    A = N - (N//2)
            print(f"Case #{test_case}: {A}")

    threading.Thread(target=run,).start()

if __name__ == "__main__":
    main()