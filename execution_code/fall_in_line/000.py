def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def normalize(dx, dy):
    g = gcd(abs(dx), abs(dy))
    dx //= g
    dy //= g
    return (dx, dy) if dx >= 0 else (-dx, -dy) if dy > 0 else (dx, dy)

def count_collinear_ants(ants):
    n = len(ants)
    if n < 3:
        return 0  # If there are 2 or less, they are trivially collinear.

    line_counts = {}
    for i in range(n):
        x1, y1 = ants[i]
        for j in range(i + 1, n):
            x2, y2 = ants[j]
            dx = x2 - x1
            dy = y2 - y1
            slope = normalize(dx, dy)
            intercept = y1 * dx - x1 * dy  # We can use any form for uniqueness

            # Store the line by its slope and intercept
            key = (slope, intercept)
            if key not in line_counts:
                line_counts[key] = set()
            line_counts[key].add(i)
            line_counts[key].add(j)

    # Finding the maximum number of ants on any line
    max_coplanar = max(len(ants_set) for ants_set in line_counts.values())
    return n - max_coplanar  # Ants to move is total minus those not on the best line

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    T = int(data[0])
    results = []
    index = 1
    
    for case in range(1, T + 1):
        N = int(data[index])
        index += 1
        ants = []
        
        for _ in range(N):
            x, y = map(int, data[index].split())
            ants.append((x, y))
            index += 1
        
        moves_needed = count_collinear_ants(ants)
        results.append(f"Case #{case}: {moves_needed}")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()