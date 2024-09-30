from collections import defaultdict
import sys
input = sys.stdin.read

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def main():
    data = input().strip().splitlines()
    idx = 0
    T = int(data[idx])
    idx += 1
    results = []
    
    for case_number in range(1, T + 1):
        N = int(data[idx])
        idx += 1
        
        points = []
        for _ in range(N):
            x, y = map(int, data[idx].split())
            points.append((x, y))
            idx += 1
        
        if N <= 2:
            # If there are 2 or fewer ants, all ants are already collinear
            results.append(f"Case #{case_number}: 0")
            continue
        
        max_collinear = 1
        
        for i in range(N):
            slopes = defaultdict(int)
            for j in range(N):
                if i != j:
                    delta_x = points[j][0] - points[i][0]
                    delta_y = points[j][1] - points[i][1]
                    if delta_x == 0:  # vertical line
                        slope = ('inf', 0)
                    else:
                        g = gcd(delta_x, delta_y)
                        slope = (delta_y // g, delta_x // g)
                        if slope[0] < 0:  # ensure unique representation
                            slope = (-slope[0], -slope[1])
                    slopes[slope] += 1
            
            current_max = max(slopes.values(), default=0)
            max_collinear = max(max_collinear, current_max + 1)  # +1 to count the base point
            
        # The minimum number of ants to move
        ants_to_move = N - max_collinear
        results.append(f"Case #{case_number}: {ants_to_move}")

    print("\n".join(results))

if __name__ == "__main__":
    main()