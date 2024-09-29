from sys import stdin, stdout
from math import gcd
from collections import defaultdict

def count_ants_to_move(ants):
    n = len(ants)
    if n <= 2:
        return 0  # If there are 2 or fewer ants, they are always collinear.
    
    max_on_line = 1
    for i in range(n):
        slopes = defaultdict(int)
        x1, y1 = ants[i]
        for j in range(n):
            if i == j:
                continue
            x2, y2 = ants[j]
            dx = x2 - x1
            dy = y2 - y1
            
            if dx == 0:
                # Vertical line, use a special representation for the slope
                slope = ('inf', 0)  # Infinite slope
            elif dy == 0:
                # Horizontal line
                slope = (0, 'inf')  # Zero slope
            else:
                # Normal slope
                g = gcd(dx, dy)
                slope = (dy // g, dx // g)
                if slope[1] < 0:  # Normalize direction
                    slope = (-slope[0], -slope[1])
            
            slopes[slope] += 1
        
        if slopes:
            max_on_line = max(max_on_line, max(slopes.values()) + 1)  # +1 to include the fixed ant
    
    move_needed = n - max_on_line
    return move_needed

def main():
    input = stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    output = []
    idx = 1
    
    for case_number in range(1, T + 1):
        N = int(data[idx])
        ants = []
        
        for j in range(N):
            x, y = map(int, data[idx + 1 + j].split())
            ants.append((x, y))
        
        idx += N + 1
        
        moves = count_ants_to_move(ants)
        output.append(f"Case #{case_number}: {moves}")
    
    stdout.write("\n".join(output) + "\n")

if __name__ == "__main__":
    main()