import sys
import bisect

def main():
    import sys
    import sys
    from bisect import bisect_right, bisect_left

    input = sys.stdin.read().split()
    ptr = 0
    T = int(input[ptr]); ptr +=1
    for test_case in range(1, T+1):
        N, G = int(input[ptr]), int(input[ptr+1]); ptr +=2
        E_list = []
        for _ in range(N):
            E_list.append(int(input[ptr]))
            ptr +=1
        # Initialize
        sorted_positions = []
        pos_to_index = []
        final_pos = [0]*N
        for stone_num in range(1, N+1):
            current_stone = stone_num
            current_pos = 0
            energy = E_list[stone_num-1]
            while energy >0:
                # Find the first stone at position > current_pos
                i = bisect_right(sorted_positions, current_pos)
                if i < len(sorted_positions):
                    P = sorted_positions[i]
                    stone_p_index = pos_to_index[i]
                    if P <= current_pos + energy:
                        steps = P - current_pos
                        energy -= steps
                        current_pos = P
                        final_pos[current_stone-1] = P
                        current_stone = stone_p_index
                    else:
                        current_pos += energy
                        final_pos[current_stone-1] = current_pos
                        energy =0
                else:
                    current_pos += energy
                    final_pos[current_stone-1] = current_pos
                    energy =0
            # Insert the final position of current_stone
            pos = final_pos[current_stone-1]
            j = bisect_left(sorted_positions, pos)
            sorted_positions.insert(j, pos)
            pos_to_index.insert(j, current_stone)
        # Find the stone closest to G
        min_distance = float('inf')
        min_index = N+1
        for i in range(N):
            distance = abs(final_pos[i] - G)
            if distance < min_distance or (distance == min_distance and (i+1) < min_index):
                min_distance = distance
                min_index = i+1
        print(f"Case #{test_case}: {min_index} {min_distance}")

if __name__ == "__main__":
    main()