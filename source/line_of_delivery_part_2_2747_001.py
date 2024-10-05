import sys
import bisect

def main():
    import sys
    import threading

    def process():
        import sys

        T = int(sys.stdin.readline())
        for test_case in range(1, T +1):
            line = ''
            while line.strip() == '':
                line = sys.stdin.readline()
            N_G = line.strip().split()
            N = int(N_G[0])
            G = int(N_G[1])
            E_list = []
            count =0
            while count < N:
                e_line = sys.stdin.readline()
                if e_line.strip()=='':
                    continue
                E_i = int(e_line.strip())
                E_list.append(E_i)
                count +=1
            # Initialize positions and values
            positions = []
            values = []
            # Initialize a list to store final positions per stone
            # stone indices from 1 to N
            final_pos = [0] * (N +1)  # final_pos[stone_idx] = position
            for i in range(1, N+1):
                E_i = E_list[i-1]
                p =0
                e = E_i
                stone_idx = i
                while True:
                    # Find the first occupied position >= p +1
                    idx = bisect.bisect_left(positions, p +1)
                    if idx == len(positions):
                        # No stone to block
                        p_new = p + e
                        bisect.insort(positions, p_new)
                        values.insert(idx, stone_idx)
                        final_pos[stone_idx] = p_new
                        break
                    next_p = positions[idx]
                    if next_p > p + e:
                        # Can move to p + e without obstruction
                        p_new = p + e
                        bisect.insort(positions, p_new)
                        values.insert(idx, stone_idx)
                        final_pos[stone_idx] = p_new
                        break
                    d = next_p - p -1
                    if d >= e:
                        # Can move to p + e without reaching the next stone
                        p_new = p + e
                        bisect.insort(positions, p_new)
                        values.insert(idx, stone_idx)
                        final_pos[stone_idx] = p_new
                        break
                    else:
                        # Move to next_p -1
                        p_new = next_p -1
                        remaining_e = e - (d +1)
                        # Remove the stone at next_p
                        transfer_stone_idx = values.pop(idx)
                        positions.pop(idx)
                        # Place current stone at p_new
                        bisect.insort(positions, p_new)
                        values.insert(idx, stone_idx)
                        final_pos[stone_idx] = p_new
                        # Now, transfer the remaining energy to transfer_stone_idx
                        p = p_new +1
                        e = remaining_e
                        stone_idx = transfer_stone_idx
            # Now, find the stone closest to G
            min_distance = None
            min_stone = None
            for stone_idx in range(1, N+1):
                pos = final_pos[stone_idx]
                distance = abs(G - pos)
                if min_distance is None or distance < min_distance or (distance == min_distance and stone_idx < min_stone):
                    min_distance = distance
                    min_stone = stone_idx
            # Output the result
            print(f"Case #{test_case}: {min_stone} {min_distance}")

    threading.Thread(target=process).start()

if __name__ == "__main__":
    main()