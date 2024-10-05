import sys
import sys
import sys

def main():
    import sys
    import sys
    from sys import stdin
    import sys

    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); G = int(data[idx+1]); idx +=2
        stones = []
        for i in range(1, N+1):
            E_i = int(data[idx]); idx +=1
            stones.append( ( -E_i, i, E_i ) )  # sort descending
        stones.sort()
        pos = [0]*(N+1)
        last_pos = 10**9
        for s in stones:
            _, i, E_i = s
            final_pos = min(E_i, last_pos -1)
            if final_pos <1:
                final_pos =1
            pos[i] = final_pos
            last_pos = final_pos
        # Now find the stone with minimum |pos[i]-G|
        min_distance = None
        min_index = None
        for i in range(1, N+1):
            distance = abs(pos[i] - G)
            if min_distance is None or distance < min_distance or (distance == min_distance and i < min_index):
                min_distance = distance
                min_index = i
        print(f"Case #{test_case}: {min_index} {min_distance}")

if __name__ == "__main__":
    main()

import sys
import sys
import sys

def main():
    import sys
    import sys
    from sys import stdin
    import sys

    input = sys.stdin.read
    data = input().split()
    idx = 0
    T = int(data[idx]); idx +=1
    for test_case in range(1, T+1):
        N = int(data[idx]); G = int(data[idx+1]); idx +=2
        stones = []
        for i in range(1, N+1):
            E_i = int(data[idx]); idx +=1
            stones.append( ( -E_i, i, E_i ) )  # sort descending
        stones.sort()
        pos = [0]*(N+1)
        last_pos = 10**9
        for s in stones:
            _, i, E_i = s
            final_pos = min(E_i, last_pos -1)
            if final_pos <1:
                final_pos =1
            pos[i] = final_pos
            last_pos = final_pos
        # Now find the stone with minimum |pos[i]-G|
        min_distance = None
        min_index = None
        for i in range(1, N+1):
            distance = abs(pos[i] - G)
            if min_distance is None or distance < min_distance or (distance == min_distance and i < min_index):
                min_distance = distance
                min_index = i
        print(f"Case #{test_case}: {min_index} {min_distance}")

if __name__ == "__main__":
    main()