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
            while len(N_G) <2:
                N_G += sys.stdin.readline().strip().split()
            N, G = map(int, N_G)
            E_list = [0]
            count =0
            while count < N:
                e_line = sys.stdin.readline()
                if not e_line:
                    break
                e_vals = e_line.strip().split()
                for e in e_vals:
                    E_list.append(int(e))
                    count +=1
                    if count ==N:
                        break
            # Initialize
            occupied = []
            pos_to_stone = {}
            final_positions = [0] * (N +1)
            for s in range(1, N+1):
                E_i = E_list[s]
                stack = [ (s, 0, E_i) ]
                while stack:
                    current_s, start_p, residual_e = stack.pop()
                    p_new = start_p + residual_e
                    # Find first p >=start_p +1 and <=p_new that is occupied
                    idx = bisect.bisect_left(occupied, start_p +1)
                    if idx < len(occupied) and occupied[idx] <= p_new:
                        p_hit = occupied[idx]
                        existing_s = pos_to_stone[p_hit]
                        # Assign p_hit to current_s
                        pos_to_stone[p_hit] = current_s
                        final_positions[current_s] = p_hit
                        # Calculate residual_energy
                        residual_energy_new = residual_e - (p_hit - start_p)
                        if residual_energy_new >0:
                            # Existing_s needs to be moved to p_hit + residual_energy_new
                            stack.append( (existing_s, p_hit, residual_energy_new) )
                    else:
                        # Assign p_new to current_s
                        bisect.insort(occupied, p_new)
                        pos_to_stone[p_new] = current_s
                        final_positions[current_s] = p_new
            # Now, find the stone closest to G
            min_distance = None
            min_s = None
            for s in range(1, N+1):
                distance = abs(final_positions[s] - G)
                if (min_distance is None) or (distance < min_distance) or (distance == min_distance and s < min_s):
                    min_distance = distance
                    min_s = s
            print(f"Case #{test_case}: {min_s} {min_distance}")

    threading.Thread(target=process).start()

if __name__ == "__main__":
    main()