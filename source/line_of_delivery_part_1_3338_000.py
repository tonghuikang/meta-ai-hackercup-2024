import sys
import bisect

def main():
    import sys
    import threading
    def solve():
        import sys
        from bisect import bisect_right, insort

        input = sys.stdin.read().split()
        ptr = 0
        T = int(input[ptr])
        ptr +=1
        for test_case in range(1,T+1):
            N, G = int(input[ptr]), int(input[ptr+1])
            ptr +=2
            E = []
            for _ in range(N):
                E.append(int(input[ptr]))
                ptr +=1
            S = []
            pos_to_stone = {}
            final_positions = [0]*N
            for i in range(1,N+1):
                E_i = E[i-1]
                current_stone = i
                current_p =0
                current_e = E_i
                while current_e >0:
                    target_p = current_p + current_e
                    # Find the first p' > current_p and <= target_p
                    index = bisect.bisect_right(S, current_p)
                    if index < len(S) and S[index] <= target_p:
                        p_prime = S[index]
                        e_prime = target_p - p_prime
                        stone_at_p_prime = pos_to_stone.pop(p_prime)
                        S.pop(index)
                        # Assign current_stone to p_prime
                        pos_to_stone[p_prime] = current_stone
                        # Now move the stone_at_p_prime with e_prime
                        current_stone = stone_at_p_prime
                        current_p = p_prime
                        current_e = e_prime
                    else:
                        # No collision, place at target_p
                        pos_to_stone[target_p] = current_stone
                        bisect.insort(S, target_p)
                        final_positions[current_stone -1] = target_p
                        break
            # After all stones are placed, find the stone closest to G
            min_distance = None
            min_index = None
            for idx in range(N):
                distance = abs(final_positions[idx] - G)
                if (min_distance is None) or (distance < min_distance) or (distance == min_distance and (idx+1) < min_index):
                    min_distance = distance
                    min_index = idx+1
            print(f"Case #{test_case}: {min_index} {min_distance}")
    threading.Thread(target=solve).start()

if __name__ == "__main__":
    main()