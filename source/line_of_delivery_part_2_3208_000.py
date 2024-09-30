import sys
import threading

def main():
    import sys
    import sys
    import sys
    sys.setrecursionlimit(1 << 25)
    from bisect import bisect_right

    T = int(sys.stdin.readline())
    for test_case in range(1, T +1):
        N, G = map(int, sys.stdin.readline().split())
        E = []
        for _ in range(N):
            E.append(int(sys.stdin.readline()))
        # Initialize DSU
        parent = list(range(G +2))
        pos_to_stone = {}
        final_positions = [0] * (N +1)
        def find_first_occupied(p):
            path = []
            while p <= G and parent[p] != p:
                path.append(p)
                p = parent[p]
            for q in path:
                parent[q] = p
            return p
        for i in range(1, N +1):
            p =0
            e = E[i -1]
            current_stone = i
            while True:
                pos = find_first_occupied(p +1)
                if pos > p + e or pos > G:
                    p_final = min(p + e, G)
                    final_positions[current_stone] = p_final
                    pos_to_stone[p_final] = current_stone
                    parent[p_final] = p_final
                    break
                else:
                    remaining_e = e - (pos - p)
                    p_stop = pos -1
                    final_positions[current_stone] = p_stop
                    pos_to_stone[p_stop] = current_stone
                    parent[p_stop] = p_stop
                    # Transfer to stone at pos
                    j = pos_to_stone[pos]
                    current_stone = j
                    p = p_stop
                    e = remaining_e
        # Find the stone closest to G
        min_dist = G +1
        min_stone = N +1
        for i in range(1, N +1):
            dist = G - final_positions[i]
            if dist < min_dist or (dist == min_dist and i < min_stone):
                min_dist = dist
                min_stone = i
        print(f"Case #{test_case}: {min_stone} {min_dist}")

threading.Thread(target=main).start()