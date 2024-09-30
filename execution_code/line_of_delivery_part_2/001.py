import sys
import threading

def main():
    import sys
    import bisect

    import sys

    sys.setrecursionlimit(1 << 25)

    T = int(sys.stdin.readline())
    for tc in range(1, T +1):
        line = ''
        while line.strip() == '':
            line = sys.stdin.readline()
        N, G = map(int, line.strip().split())
        E = []
        cnt =0
        while cnt < N:
            e_line = sys.stdin.readline()
            if e_line.strip() == '':
                continue
            E.append(int(e_line.strip()))
            cnt +=1
        pos_to_stone = {}
        for s in range(1, N +1):
            E_i = E[s-1]
            s_current = s
            p =0
            while E_i >0:
                if (p +1) in pos_to_stone:
                    # Collision occurs at p
                    p_stop = p
                    # Steps taken to reach p_stop: p_stop - p_start
                    # Remaining energy: E_i - (p_stop - p_start)
                    # Since p_start is current p, steps taken = p_stop - p
                    # Thus, remaining_E = E_i
                    remaining_E = E_i
                    # Assign current stone to p_stop
                    pos_to_stone[p_stop] = s_current
                    # Transfer energy to the stone at p+1
                    s_new = pos_to_stone[p +1]
                    s_current = s_new
                    p = p_stop
                    E_i = remaining_E
                else:
                    # No collision, move to p+1
                    p +=1
                    E_i -=1
                    if E_i ==0:
                        pos_to_stone[p] = s_current
            # Proceed to next stone

        # After all stones are thrown, find the stone closest to G
        min_distance = float('inf')
        min_stone = N +1
        for p, s in pos_to_stone.items():
            dist = abs(p - G)
            if dist < min_distance or (dist == min_distance and s < min_stone):
                min_distance = dist
                min_stone = s
        print(f"Case #{tc}: {min_stone} {min_distance}")

threading.Thread(target=main).start()