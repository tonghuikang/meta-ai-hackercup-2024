import sys
import bisect

def main():
    import sys
    import threading

    def solve():
        import sys

        T = int(sys.stdin.readline())
        for test_case in range(1, T+1):
            N, G = map(int, sys.stdin.readline().split())
            stones = []
            for i in range(N):
                E = int(sys.stdin.readline())
                stones.append( ( -E, i+1, E ) )  # use negative energy for sorting descending

            # Sort stones by decreasing energy
            stones.sort()

            positions = []
            stone_info = dict()  # position : (index, E)

            for neg_E, idx, E in stones:
                intended_pos = E
                # Find the smallest position >= intended_pos that is already occupied
                pos = intended_pos
                while True:
                    # Find the insertion point
                    insert_loc = bisect.bisect_left(positions, pos)
                    if insert_loc < len(positions) and positions[insert_loc] == pos:
                        # Collision occurs, transfer remaining energy to the stone at pos
                        # Remaining energy is current E - (pos - 0) = E - pos
                        E_new = E - pos
                        if E_new <=0:
                            break
                        # Now, the stone at pos becomes moving with E_new
                        idx_new = stone_info[pos][0]
                        pos_new = E_new
                        # Reset to new moving stone
                        pos = E_new
                        # Update E and idx for the new moving stone
                        E = E_new
                        idx = idx_new
                        intended_pos = pos
                        continue
                    else:
                        # No collision, place the stone here
                        bisect.insort(positions, pos)
                        stone_info[pos] = (idx, E)
                        break

            # Now, find the stone closest to G
            min_dist = None
            min_idx = None
            for pos, (idx, E) in stone_info.items():
                dist = abs(G - pos)
                if (min_dist is None) or (dist < min_dist) or (dist == min_dist and idx < min_idx):
                    min_dist = dist
                    min_idx = idx

            print(f"Case #{test_case}: {min_idx} {min_dist}")

    threading.Thread(target=solve,).start()

if __name__ == "__main__":
    main()