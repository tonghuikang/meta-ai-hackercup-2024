import sys
import bisect

def main():
    import sys
    import threading

    def run():
        T_and_rest = sys.stdin.read().split()
        T = int(T_and_rest[0])
        ptr = 1
        for test_case in range(1, T+1):
            N = int(T_and_rest[ptr])
            G = int(T_and_rest[ptr+1])
            ptr +=2
            E_list = list(map(int, T_and_rest[ptr:ptr+N]))
            ptr +=N
            sorted_stones = []
            final_pos = [0]*(N+1)  # 1-based indexing
            for i in range(1, N+1):
                moving_stone = i
                current_pos = 0
                remaining_energy = E_list[i-1]
                while remaining_energy >0:
                    # Find the first stone with position > current_pos
                    idx = bisect.bisect_right(sorted_stones, (current_pos, -1))
                    if idx < len(sorted_stones) and sorted_stones[idx][0] <= current_pos + remaining_energy:
                        x, j = sorted_stones[idx]
                        dx = x - current_pos
                        remaining_energy -= dx
                        final_pos[moving_stone] = x
                        # Remove the collided stone
                        del sorted_stones[idx]
                        # Now, the collided stone becomes the moving stone
                        moving_stone = j
                        current_pos = x
                    else:
                        # No collision, stone stops here
                        final_x = current_pos + remaining_energy
                        final_pos[moving_stone] = final_x
                        bisect.insort(sorted_stones, (final_x, moving_stone))
                        break
            # Find the stone closest to G
            best_distance = abs(final_pos[1] - G)
            best_index =1
            for i in range(2, N+1):
                distance = abs(final_pos[i] - G)
                if distance < best_distance or (distance == best_distance and i < best_index):
                    best_distance = distance
                    best_index =i
            print(f"Case #{test_case}: {best_index} {best_distance}")
    
    threading.Thread(target=run).start()

if __name__ == "__main__":
    main()