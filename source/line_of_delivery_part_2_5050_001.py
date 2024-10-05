import sys
import threading
def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    T = int(sys.stdin.readline())
    for case_num in range(1, T + 1):
        N, G = map(int, sys.stdin.readline().split())
        E = []
        for _ in range(N):
            E.append(int(sys.stdin.readline()))
        positions = {}  # position: stone index
        stones_energy = [0] * N  # To keep track of stones' energies if needed
        def move(stone_index, position, energy):
            while energy > 0:
                position += 1
                if position in positions:
                    # Collision
                    # Stone stops at position -1
                    positions[position -1] = stone_index
                    # Transfer remaining energy to the stone at position
                    next_stone = positions[position]
                    # Recursively move the stone at position with remaining energy
                    move(next_stone, position, energy)
                    return
                else:
                    energy -=1
                    if energy ==0:
                        positions[position] = stone_index
                        return
        for i in range(N):
            move(i, 0, E[i])
        min_distance = float('inf')
        min_stone = None
        for pos, idx in positions.items():
            dist = abs(pos - G)
            if dist < min_distance or (dist == min_distance and idx+1 < min_stone):
                min_distance = dist
                min_stone = idx+1
        print(f"Case #{case_num}: {min_stone} {min_distance}")
threading.Thread(target=main).start()